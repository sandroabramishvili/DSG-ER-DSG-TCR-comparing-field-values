import os
import sys
import json
import shutil
##from kafka import KafkaConsumer, TopicPartition, KafkaClient
import multiprocessing as mp
from json import loads
import datetime
import struct

def init_consumer(consumer, servers, group):
  return consumer(bootstrap_servers = servers,
                       group_id = group,
                       auto_offset_reset='earliest',
                       consumer_timeout_ms=1000,
                       enable_auto_commit=False,
                       )

def get_topics(consumer):
  return consumer.topics()

def get_data_by_topic(Consumer, Topic, topic, partitions, servers, group):
  for pdx in partitions:
    consumer = init_consumer(Consumer, servers, group)
    part = Topic(topic, pdx)
    consumer.assign([part])
    consumer.seek_to_end(part)
    consumer.commit()
    last_index = consumer.position(part)
    consumer.seek_to_beginning(part)
    consumer.commit()
    first_index = consumer.position(part)
    if first_index > 0 and first_index <= last_index:
      try:
        for idx, msg in enumerate(consumer):
          print(msg.value)
          #with open("output/{}.dat".format(topic), 'a') as f:
          #  f.write("{},{}END_OF_LINE\n".format(msg.timestamp, msg.value))
      except ValueError as e:
        print('ALARM! Topic {} can not be read due to {}'.format(topic, e))
    print('Topic {} (Part {}) Done'.format(topic, pdx))
  beginning_offset = consumer.position(part)
  consumer.close(autocommit=False)

if __name__ == "__main__":
  output_dir = 'output'
  if os.path.exists(output_dir):
    shutil.rmtree('{}/'.format(output_dir))
  os.makedirs(output_dir)
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
            "SURRND.ETF.TCS.PACK-PRIC.OUT",
            "SURRND.ALL.TCS.OUT",
            "SURRND.OTC.SATURN.PACK-FULLTRAD.OUT"]
  group = 'MYGROUP'
  servers = ['10.232.64.23:9092','10.232.64.24:9092','10.232.64.54:9092']
  consumer = init_consumer(servers, group)
  tasks = []
  pool = mp.Pool(200)
  for topic in sorted(topics):
    result = pool.apply_async(get_data_by_topic, (topic, consumer.partitions_for_topic(topic),))
    tasks.append(result)
  results = [result.get() for result in tasks]
