#! /usr/bin/python3.6

import os
import shutil
import struct
import tarfile
import datetime
import importlib as imp
from kafka import KafkaConsumer, TopicPartition, KafkaClient
import modules.kafka
import modules.files
import modules.parse


today = datetime.datetime.today().strftime('%Y%m%d')
# today = '20240214'

dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.dirname(dir_path)  # Get the parent directory of the current directory (kfk directory)
input_path = os.path.join(parent_dir, 'input/')
enrichment_path = dir_path + '/enrichment'
enrichment_file = enrichment_path + '/enrichment.txt'
sbe_dict_path = dir_path+'/dict/'

group = 'MYGROUP'

from_kafka = 1
from_file = None

max_vers = -1
for sbe_dict in os.listdir(sbe_dict_path):
    if '__' in sbe_dict: continue
    v = sbe_dict.split('_')[1][:3]
    if int(v) > int(max_vers):
        max_vers = str(v)

if not os.path.exists(enrichment_path):
    os.makedirs(enrichment_path)
else:
     shutil.rmtree(enrichment_path)
     os.makedirs(enrichment_path)

topics = ["SURRND.ALL.MTXC.REF-DATA.OUT"]

servers = ['10.232.64.2:9092','10.232.64.50:9092','10.232.64.51:9092','10.232.64.52:9092','10.232.64.61:9092']
# servers = []

def parse_enr(_src, timestp, msg_vers,today):
    _msg = {}
    if str(timestp) == '-1' or datetime.datetime.fromtimestamp(float(int(timestp)/1000)).strftime('%Y%m%d') == today:
        _msg, msg_type = modules.parse.parse_enrichment(_src, _msg,msg_vers)
    if _msg is not None:
        modules.files.write_enrichment(_msg,enrichment_file)

def get_enrichment(max_vers,parse_from_kfk_flag,parse_from_file_flag,today):
    id_set = set()
    if parse_from_kfk_flag:
        consumer = modules.kafka.init_consumer(KafkaConsumer, servers, group)
        print('GET ENRICHMENT  DATA FROM KAFKA')
        for topic in sorted(topics):
            print(topic)
            parts = consumer.partitions_for_topic(topic)
            if not parts: continue
            for pdx in parts:
                part = TopicPartition(topic, pdx)
                consumer.assign([part])
                consumer.seek_to_end(part)
                consumer.commit()
                last_index = consumer.position(part)
                consumer.seek_to_beginning(part)
                consumer.commit()
                first_index = consumer.position(part)
                if first_index >= last_index: continue
                count = 0
                for idx, msg in enumerate(consumer):
                    vers = struct.unpack('<H', msg.value[8:10])[0]
                    msgid = str(struct.unpack('<H', msg.value[4:6])[0])
                    _src = msg.value
                    id_set.add(msgid)
#                    print(id_set)
                    if msgid != '12224': continue
                    dict_vers = "modules.dict.dict_"+str(vers)
                    try:
                        msg_dict = imp.import_module(dict_vers)
                    except:
                        print('WARNING! There is no dictionary for {} version. Using dictionary for {} version'.format(vers,max_vers))
                        msg_dict = imp.import_module('modules.dict.dict_{}'.format(max_vers))
                        vers = max_vers
                    parse_enr(_src,msg.timestamp,str(vers),today)
    if parse_from_file_flag:
        print('GET ENRICHMENT  DATA FROM FILES')
        tar_file = input_path+'{}.tar.gz'.format(today)
        with tarfile.open(tar_file,'r:gz') as input_tar:
            tar_files = input_tar.getnames()
            for member in list(input_tar.getnames()):
                if 'MTXC' not in member: continue
                file_name = input_tar.extractfile(member)
                while True:
                    raw_msg = file_name.readline().decode().rstrip('\n')
                    if len(raw_msg) < 2:
                        break
                    msg_time, msg_topic, msg_partition, msg_offset, version, _src = raw_msg.split(',',5)
                    src = bytes.fromhex(_src)
                    msgid = str(struct.unpack('<H', src[4:6])[0])
                    if msgid != '12224':
                        continue
                    parse_enr(src,msg_time,version,today)

#get_enrichment(max_vers,parse_from_kfk_flag,parse_from_file_flag,today)
