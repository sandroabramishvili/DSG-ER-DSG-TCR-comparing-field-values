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
#today = '20230420'

dir_path = os.path.dirname(os.path.realpath(__file__))
input_path = dir_path+'/input/'
enrichment_path = dir_path + '/enrichment'
enrichment_file = enrichment_path + '/enrichment.txt'

group = 'MYGROUP'

from_kafka = 1
from_file = None

if not os.path.exists(enrichment_path):
    os.makedirs(enrichment_path)
else:
     shutil.rmtree(enrichment_path)
     os.makedirs(enrichment_path)

topics = ["SURRND.ALL.MTXC.REF-DATA.OUT"]

servers = ['10.232.64.2:9092','10.232.64.50:9092','10.232.64.51:9092','10.232.64.52:9092','10.232.64.61:9092']

def parse_enr(_src, timestp, msg_vers):
    _msg = {}
    if str(timestp) == '-1' or datetime.datetime.fromtimestamp(float(int(timestp)/1000)).strftime('%Y%m%d') == today:
        _msg, msg_type = modules.parse.parse_enrichment(_src, _msg,msg_vers)
    if _msg is not None:
        modules.files.write_enrichment(_msg,enrichment_file)

def get_enrichment():
    id_set = set()
    if from_kafka:
        consumer = modules.kafka.init_consumer(KafkaConsumer, servers, group)
        print('GET DATA FROM KAFKA')
        for topic in sorted(topics):
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
                    msg_dict = imp.import_module(dict_vers)
                    parse_enr(_src,msg.timestamp,str(vers))
    if from_file:
        print('GET DATA FROM FILES')
        tar_file = input_path+'{}.tar.gz'.format(today)
        with tarfile.open(tar_file,'r:gz') as input_tar:
            tar_files = input_tar.getnames()
            for member in list(input_tar.getnames()):
                if 'MTXC' not in member: continue
                file_name = input_tar.extractfile(member)
                while True:
                    raw_msg = file_name.readline()
                    if len(raw_msg) < 2:
                        break
                    _src = str(raw_msg)[2:-1].split(',',5)
                    msg_time = _src[0]
                    version = _src[4]
                    src = _src[5][2:-13].encode().decode('unicode_escape').encode('raw_unicode_escape').decode('unicode_escape').encode('raw_unicode_escape')
                    msgid = str(struct.unpack('<H', src[4:6])[0])
                    parse_enr(src,msg_time,version)

get_enrichment()
