#! /usr/bin/python3.6

import os, time
import datetime
from kafka import KafkaConsumer, TopicPartition, KafkaClient
import modules.kafka
import modules.files
import modules.parse
import modules.dict
import modules.make_enrichment
import shutil
import argparse
import struct
import importlib as imp
from operator import itemgetter
import tarfile
import subprocess
import binascii as ba


#modules.make_enrichment.get_enrichment()

start_time = datetime.datetime.today()
parse_from_file_flag = 1
write_input_flag = None
parse_from_kfk_flag = None
enr_flag = 1
clean_directory_flag = 1

not_parsed = 0

a_parser = argparse.ArgumentParser()
a_parser.add_argument('path',action = 'store', type = str,help = 'Path to the script')
script_path = a_parser.parse_args()

today = datetime.datetime.today().strftime('%Y%m%d')
today = '20230926'
output_dir = script_path.path+'/output/{}'.format(today)
output_tmp = script_path.path+'/output/{}/tmp'.format(today)
input_dir = script_path.path+'/input/{}'.format(today)
print(output_dir)

sbe_dict_path = script_path.path+'/modules/dict/'
enrichment_path = script_path.path+'/modules/enrichment/'

try:
    modules.make_enrichment.get_enrichment()
except:
    print('Using old enrichment')
    enrichment_path = script_path.path+'/enrichment/'

if clean_directory_flag:
  if os.path.exists('{}/'.format(output_dir)):
    shutil.rmtree('{}/'.format(output_dir))
  os.makedirs('{}/'.format(output_dir))

  if not parse_from_file_flag:
    if os.path.exists('{}/'.format(input_dir)):
      shutil.rmtree('{}/'.format(input_dir))
    os.makedirs('{}/'.format(input_dir))

topics = ["SURRND.ALL.MTXC.REF-DATA.OUT",
          "OPTIQv2.EQU.FULLMSG.PACK-FULLORD.OUT",
          "OPTIQv2.EQU.FULLMSG.PACK-FULLTRAD.OUT",
          "OPTIQv2.EQU.MECONSUMR.PACK-TOL.OUT",
          "OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT",
          "OPTIQv2.ETF.FULLMSG.PACK-FULLTRAD.OUT",
          "OPTIQv2.ETF.MECONSUMR.PACK-TOL.OUT",
          "OPTIQv2.FXI.FULLMSG.PACK-FULLORD.OUT",
          "OPTIQv2.FXI.FULLMSG.PACK-FULLTRAD.OUT",
          "OPTIQv2.FXI.MECONSUMR.PACK-TOL.OUT",
          "OPTIQv2.WAR.FULLMSG.PACK-FULLORD.OUT",
          "OPTIQv2.WAR.FULLMSG.PACK-FULLTRAD.OUT",
          "OPTIQv2.WAR.MECONSUMR.PACK-TOL.OUT",
          "OPTIQv2.BLK.FULLMSG.PACK-FULLORD.OUT",
          "OPTIQv2.BLK.FULLMSG.PACK-FULLTRAD.OUT",
          "OPTIQv2.BLK.MECONSUMR.PACK-TOL.OUT",
          "SURRND.ALL.TCS.OUT",
          "SURRND.ALL.TCS.IN",
          "SURRND.ANY.TCS.PACK-FULLTRAD.OUT",
          "SURRND.OTC.SATURN.PACK-FULLTRAD.OUT",
          "SURRND.IDX.GIS.PACK-IDX.OUT",
          "SURRND.ETF.TCS.PACK-PRIC.OUT",
          "OPTIQv2.RECOVERY.FULLTRAD.OUT",
          "SURRND.WAR.GBOX.PACK-STATE.OUT",
          "SURRND.CASH.PTB.PACK-POSTTRAD.BOTH",
          "SURRND.ANY.LPMON.MM-ALERTS.OUT",
          "RECON.EQU.FULLMSG.PACK-FULLTRAD.OUT",
          "RECON.ETF.FULLMSG.PACK-FULLTRAD.OUT",
          "RECON.BLK.FULLMSG.PACK-FULLTRAD.OUT",
          "RECON.FXI.FULLMSG.PACK-FULLTRAD.OUT",
          "RECON.WAR.FULLMSG.PACK-FULLTRAD.OUT"
          ]
#topics = ["SURRND.ALL.MTXC.REF-DATA.OUT"]
#topics = ["OPTIQv2.WAR.MECONSUMR.PACK-TOL.OUT","SURRND.ALL.MTXC.REF-DATA.OUT"]
#topics = ["SURRND.ALL.MTXC.REF-DATA.OUT","SURRND.ALL.TCS.OUT","SURRND.OTC.SATURN.PACK-FULLTRAD.OUT","SURRND.IDX.GIS.PACK-IDX.OUT","SURRND.CASH.PTB.PACK-POSTTRAD.BOTH"]
#topics = ["OPTIQv2.EQU.FULLMSG.PACK-FULLTRAD.OUT"]
#topics = ["SURRND.ALL.MTXC.REF-DATA.OUT","OPTIQv2.EQU.FULLMSG.PACK-FULLORD.OUT"]
#topics = ["OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT"]
#topics = ["OPTIQv2.EQU.MECONSUMR.PACK-TOL.OUT","OPTIQv2.ETF.MECONSUMR.PACK-TOL.OUT","OPTIQv2.FXI.MECONSUMR.PACK-TOL.OUT","OPTIQv2.WAR.MECONSUMR.PACK-TOL.OUT","OPTIQv2.BLK.MECONSUMR.PACK-TOL.OUT"]#, "SURRND.ALL.MTXC.REF-DATA.OUT"]
#topics = ["OPTIQv2.EQU.FULLMSG.PACK-FULLORD.OUT","OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT","OPTIQv2.FXI.FULLMSG.PACK-FULLORD.OUT","OPTIQv2.WAR.FULLMSG.PACK-FULLORD.OUT","OPTIQv2.BLK.FULLMSG.PACK-FULLORD.OUT"]

#topics = ['SURRND.WAR.GBOX.PACK-STATE.OUT']
group = 'MYGROUP'
#servers = ['10.232.64.23:9092','10.232.64.24:9092','10.232.64.54:9092']
servers = ['10.232.64.2:9092','10.232.64.50:9092','10.232.64.51:9092','10.232.64.52:9092','10.232.64.61:9092','qsdpespy25501v-int:9092']

def enrichment_prep():
    enr_flag = 1
    enrichment = {}
    line = 1
    if enr_flag:
        if os.path.exists(enrichment_path+'enrichment.txt'):
            print('Enrichment exists')
            with open(enrichment_path+'enrichment.txt','r',encoding = 'latin-1') as enr:
                while line:
                    line = enr.readline()
                    if not line: break
                    enr_symbol = line.split(':',1)[0][1:-1]
                    enrichment[enr_symbol] = {}
                    enr_v = line.split(':',1)[1]
                    enr_split = str(enr_v.split(':'))[1:-3].replace(' \'','').replace(' None','').replace('\'','').replace(' \"','').replace('\"','').split(',')
                    len_split = len(enr_split)
                    for idx,val in enumerate(enr_split):
                        if 'ENR_' in  val or 'HDR_MIC' in val:
                            enr_field = val
                        else:
                            if idx != len_split - 1:
                                enrichment[enr_symbol].update({enr_field:val})
                            else:
                                enrichment[enr_symbol].update({enr_field:val[:-1]})
        else:
            enr_flag = None
            print('Enrichment doesn\'t exists')
    return enrichment

def parse_topic(_src, timestp,msg_topic,msg_partition,msg_offset,msg_vers,max_vers,enrichment):
  _msg = {}
  if str(timestp) == '-1' or datetime.datetime.fromtimestamp(float(int(timestp)/1000)).strftime('%Y%m%d') == today:
    _msg, msg_type = modules.parse.parse_msg(_src, _msg,msg_topic,msg_partition,msg_offset,msg_vers,max_vers,enrichment)
  msg_dict = imp.import_module('modules.dict.dict_'+str(max_vers))
  if _msg is not None:
    if 'HDR_MESSAGETYPE' in _msg:
        modules.files.write_csv('{}/'.format(output_dir), _msg, msg_type,msg_topic)
    else:
      for s_msg in _msg:
        split_msg = _msg[s_msg]
        if 'HDR_MESSAGETYPE' in split_msg:
          if msg_type in msg_dict.splitted_msgs or msg_type in msg_dict.alpha_msgs:
              modules.files.write_csv('{}/'.format(output_dir), split_msg, split_msg['HDR_MESSAGETYPE'],msg_topic)


def get_data_from_kafka():
  enrich_prep_start_time = datetime.datetime.today()
  enrichment = enrichment_prep()
  enrich_prep_endtime = datetime.datetime.today()
  enrich_prep_time = str(enrich_prep_endtime - enrich_prep_start_time)
  print('Enrichment preparation time {}'.format(enrich_prep_time))
  max_vers = -1
  for sbe_dict in os.listdir(sbe_dict_path):
      if '__' in sbe_dict: continue
      v = sbe_dict.split('_')[1][:3]
      if int(v) > max_vers:
          max_vers = int(v)
  if parse_from_file_flag:
    print('GET DATA FROM FILES')
    tar_file = input_dir+'.tar.gz'
    with tarfile.open(tar_file,'r:gz') as input_tar:
#      input_tar = tarfile.open(input_dir+'.tar.gz')
      tar_files = input_tar.getnames()
#    file_name = "SURRND.ALL.MTXC.REF-DATA.OUT.dat"
#    if file_name:
#    for file_name in os.listdir('{}/'.format(input_dir)):
#    for file_name in ("OPTIQv2.EQU.FULLMSG.PACK-FULLORD.OUT.dat","OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT.dat","OPTIQv2.FXI.FULLMSG.PACK-FULLORD.OUT.dat","OPTIQv2.WAR.FULLMSG.PACK-FULLORD.OUT.dat","OPTIQv2.BLK.FULLMSG.PACK-FULLORD.OUT.dat"):   #"OPTIQv2.ETF.FULLMSG.PACK-FULLORD.OUT.dat"
      for member in list(input_tar.getnames()):
        if member[-8:] == today: continue
        file_name = input_tar.extractfile(member)
#        if str(member) != "20221028/SURRND.ALL.TCS.IN.dat": continue
        print("Get data from {}".format(member))
        while True:
#            raw_msg = dat.readline()
            raw_msg = file_name.readline()
            if len(raw_msg) < 2:
              break
            _src = str(raw_msg)[2:-1].split(',',5)
            msg_time = _src[0]
            msg_topic = _src[1]
            msg_partition = _src[2]
            msg_offset = _src[3]
            version = _src[4]
            src = _src[5][2:-13].encode().decode('unicode_escape').encode('raw_unicode_escape').decode('unicode_escape').encode('raw_unicode_escape')
            msgid = str(struct.unpack('<H', src[4:6])[0])
#            if str(msgid) != '12224': continue
#            if str(msgid) not in ('543','12224'): continue
            msg_dict = imp.import_module("modules.dict.dict_"+str(version))
            parse_topic(src,msg_time,msg_topic,msg_partition,msg_offset,version,str(max_vers),enrichment)
  elif parse_from_kfk_flag or write_input_flag:
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
        #try:
        count = 0
        not_parsed = 0
        for idx, msg in enumerate(consumer):
#          print(msg)
#          exit()
          vers = struct.unpack('<H', msg.value[8:10])[0]
          msgid = str(struct.unpack('<H', msg.value[4:6])[0])
#          if msgid == '12053':
#            print(msg)
#            exit()
#          else:
#            continue
          if int(vers) < 315:
            print(msg.topic,msgid,vers)
#            if msgid not in modules.dict.dict_318.msgids:
#              continue
            continue
          dict_vers = "modules.dict.dict_"+str(vers)
          try:
              msg_dict = imp.import_module(dict_vers)
          except:
              print('Dictionary for {} version does not exists'.format(vers))
              msg_dict = imp.import_module('modules.dict.dict_325')
          if write_input_flag:
              with open("{}/{}.dat".format(input_dir,topic), 'a') as f:
#                GOOD_VALUE = ba.hexlify(msg.value).decode
                f.write("{},{},{},{},{},{}END_OF_LINE\n".format(msg.timestamp,msg_dict.topicid[msg.topic],msg.partition,msg.offset,vers, msg.value))
#                f.write("{},{},{},{},{},{}END_OF_LINE\n".format(msg.timestamp,msg_dict.topicid[msg.topic],msg.partition,msg.offset,vers, GOOD_VALUE))
          if parse_from_kfk_flag: 
            _src = msg.value
            try:
              parse_topic(_src,msg.timestamp,msg_dict.topicid[msg.topic],msg.partition,str(msg.offset),vers,str(max_vers),enrichment)
            except:
              if not_parsed == 0:
                print("WARNING! Parsing went wrong for {} message".format(msgid))  
                not_parsed =1
              continue
            count+=1
        print('Topic {} (Part {}) ({} msgs) Done'.format(topic, pdx, count))
      #except ValueError as e:
      #  print('ALARM! Topic {} can not be read due to {}'.format(topic, e))
    consumer.close(autocommit=False)

def make_tarfile(today,input_dir):
#    subprocess.call(['tar','czf',today+'.tar.gz',input_dir])
    if os.path.exists('{}'.format(input_dir+'.tar.gz')):
      os.remove('{}'.format(input_dir+'.tar.gz'))
    subprocess.call(['tar','czf',input_dir+'.tar.gz',input_dir])
#    with tarfile.open(input_dir+'.tar.gz',"w:gz") as tar:
#      tar.add(input_dir,arcname = os.path.basename(input_dir))
    if os.path.exists('{}/'.format(input_dir)):
      shutil.rmtree('{}/'.format(input_dir))

get_data_from_kafka()

arch_start_time = datetime.datetime.today()
if write_input_flag:
  print('Make archive')
  make_tarfile(today,input_dir)


end_time = datetime.datetime.today()
arch_time = str(end_time - arch_start_time)
exec_time = str(end_time - start_time)
if write_input_flag:
  print("Archiving time {}".format(arch_time))
print("Complete execution time {}.".format(exec_time))
print("END")
