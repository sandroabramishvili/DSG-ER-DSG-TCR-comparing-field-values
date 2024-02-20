import modules.dict
import importlib as imp
import struct
import copy
from datetime import datetime

tst = True

warn_msg = []

def byte2type(ftype, value):
    return {
        'Void': lambda x: x
    ,   'String': lambda x: x.split('\x00')[0]
    #,   'Char': lambda x: x.decode('latin-1').rstrip('\x00')
    ,   'Char': lambda x: x.decode('latin-1')#.strip().strip('\x00').strip('\x01').strip('\x02').strip('\x00')#.strip('\x00\x01').strip('\x01\x00').strip('\x02\x00')
    #,   'Char': lambda x: x#.decode('latin-1')
    #,   'Char': lambda x: x.decode('utf-8').strip().strip('\x00').strip('\x01').strip('\x02').strip('\x00')
    ,   'Alpha': lambda x: chr(struct.unpack('<B', x)[0])
    ,   'Byte': lambda x: chr(struct.unpack('<B', x)[0])
    ,   'Price': lambda x: str(Decimal(str(struct.unpack('<q', x)[0])) / 100000000)
    ,   'Int8': lambda x: str(struct.unpack('<b', x)[0])
    ,   'UInt8': lambda x: str(struct.unpack('<B', x)[0])
    ,   'Int16': lambda x: str(struct.unpack('<h', x)[0])
    ,   'UInt16': lambda x: str(struct.unpack('<H', x)[0])
    ,   'Int32': lambda x: str(struct.unpack('<i', x)[0])
    ,   'UInt32': lambda x: str(struct.unpack('<I', x)[0])
    ,   'Int64': lambda x: str(struct.unpack('<q', x)[0])
    ,   'UInt64': lambda x: str(struct.unpack('<Q', x)[0])
    }[ftype](value)


def null_values(value,tag_type):
  if tag_type == 'UInt8' and str(value) == '255':
    return None
  elif tag_type == 'Int8' and str(value) == '-128':
    return None
  elif tag_type == 'UInt16' and str(value) == '65535':
    return None
  elif tag_type == 'UInt32' and str(value) == '4294967295':
    return None
  elif tag_type == 'Int32' and str(value) == '-2147483648':
    return None
  elif tag_type == 'UInt64' and str(value) == '18446744073709551615':
    return None
  elif tag_type == 'Int64' and str(value) == '-9223372036854775808':
    return None
  else:
    return value

def msg_dict_prep(_dict, message,msg_dict):
  for tag in _dict:
    if tag[0][0:3] != 'RG_':
      message[tag[0]] = ''
    else:
      for rg_tag in msg_dict.msgs[tag[0]]:
        for rdx in range(1, int(tag[1])+1):
            message['{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx)] = ''
  return message

def tag_paarse(_src, _dict, message, tag_name):
  tag_len = int(_dict[1])
  tag_type = _dict[2]
  tag_src = _src[0:tag_len]
  newline = bytes('\n','latin-1')
  n = bytes('\x00','latin-1')
  if newline in tag_src and tag_type == 'Char':
    print("WARNING!!Replaced \\n with null")
    tag_src = tag_src.replace(newline,n)
  message[tag_name] = byte2type(tag_type, tag_src).replace('\0', '')
  if null_values(message[tag_name],tag_type) == None:
    message[tag_name] = None
  return message, _src[tag_len:]

def tags_parse(_src, _dict, message, msgid,msg_dict,real_fields):
  split_msgs = {}
  splitted_ms = {}
  end_msg = {}
  count = 0
#  warn_msg = []
  for tag in _dict:
    if len(_src) == 0 : continue
    if 'RG_' not in tag[0]:
      if tag[0] not in real_fields:
        continue
      message, _src = tag_paarse(_src, tag, message, tag[0])
      if 'produceTime' in message:
          message['HDR_PRODUCETIME'] = message['produceTime']
      if 'consumeTime' in message:
          message['HDR_CONSUMETIME'] = message['consumeTime']
    else:
      count += 1
      if len(_src) == 0: continue
      if modules.parse.tst:
        modules.parse.tst = False
      rg_len = int(byte2type('UInt8', _src[0:1]))
      rg_cnt = int(byte2type('UInt8', _src[1:2]))
#      if int(rg_cnt) > int(tag[1]) and msgid not in msg_dict.splitted_msgs and msgid not in msg_dict.alpha_msgs:
#        print('Max number of repetitions for rep group {} is {}, actual number of rep groups is {}'.format(tag[0],tag[1],rg_cnt))
      if rg_cnt > 0:
        if tag[0] in msg_dict.msgs:
            if str(msgid) not in  msg_dict.splitted_msgs:
              _src = _src[2:]
#              mes = copy.deepcopy(message)
              mes = {}
              for rdx in range(1, int(rg_cnt)+1):
#              for rdx in range(1, int(tag[1])+1):
                for rg_tag in msg_dict.msgs[tag[0]]:
                  if '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx) not in real_fields:
                      continue
                  if rdx <= int(tag[1]):
#                    try:
#                      print(_src)
                    mes, _src = tag_paarse(_src, rg_tag, mes, '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx))
#                      print(mes)
#                    except:
#                      print(msgid)
#                      print(tag)
                  else:
                    _src = _src[int(rg_tag[1]):]
              message.update(mes)
            elif str(msgid) != '12005':
              _src = _src[2:]
              for rdx in range(int(rg_cnt)):
                split_msgs[rdx] = copy.deepcopy(message)
                for rg_tag in msg_dict.msgs[tag[0]]:
                  if '{}_{}_1'.format(tag[0][9:],rg_tag[0]) not in real_fields:
                      continue
                  split_msgs[rdx], _src = tag_paarse(_src, rg_tag, split_msgs[rdx], '{}_{}_1'.format(tag[0][9:],rg_tag[0]))
            elif str(msgid) == '12005':
              _src = _src[2:]
              if tag[0] == 'RG_12005_STOIDS':
                for rdx in range(int(rg_cnt)):
                  split_msgs[rdx] = copy.deepcopy(message)
                  for rg_tag in msg_dict.msgs[tag[0]]:
                    if '{}_{}_1'.format(tag[0][9:],rg_tag[0]) not in real_fields:
                      continue
                    split_msgs[rdx], _src = tag_paarse(_src, rg_tag, split_msgs[rdx], '{}_{}_1'.format(tag[0][9:],rg_tag[0]))
              else:
                for rdx in range(1, int(rg_cnt)+1):
                  for rg_tag in msg_dict.msgs[tag[0]]:
                    if '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx) not in real_fields:
                      continue
                    end_msg,_src = tag_paarse(_src, rg_tag, end_msg, '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx))
              for i in split_msgs:
                split_msgs[i].update(end_msg)
      elif rg_cnt == 0:
         _src = _src[2:]
         if msgid in  msg_dict.splitted_msgs:
             split_msgs[0] = message
      else:
          if msgid not in warn_msg:
            warn_msg.append(msgid)
            print('WARNING! Repiting group count = {} for {}'.format(rg_cnt,msgid))
          _src = _src[2:]
  if msgid not in  msg_dict.splitted_msgs:
    return message, _src
  else:
    return split_msgs, _src

def tags_parse_alpha(_src, _dict, _dict_alpha, message, msgid,msg_dict,msg_vers):
  alphanum_msgs = {}
  rg_number = 0
  idx = 0
  new_idx = 0
  if msgid == '12224' and int(msg_vers) > 324:
    _dict_12224b = msg_dict.msgs[msg_dict.msgids['{}B'.format(msgid)]]
    _dict_12224c = msg_dict.msgs[msg_dict.msgids['{}C'.format(msgid)]]
#  warn_msg = []
  for tag in _dict:
    if 'RG_' not in tag[0]:
      message, _src = tag_paarse(_src, tag, message, tag[0])
      message['HDR_PRODUCETIME'] = message['produceTime']
      message['HDR_CONSUMETIME'] = message['consumeTime']
      if msgid == '12233':
          message['HDR_MIC'] = '-'
      alphanum_msgs[0] = message
#      alphanum_msgs[0] = copy.deepcopy(message)
    else:
      if msgid == '12224':
        enrichment = {}
        for enr in msg_dict.ENR:
          enrichment[enr] =  alphanum_msgs[0][msg_dict.ENR[enr]]
#          alphanum_msgs[0][msg_dict.ENR[enr]] = alphanum_msgs[0][enr]
        alphanum_msgs[0]['HDR_BATCHID'] = alphanum_msgs[0]['batchID']
        alphanum_msgs[0].update(enrichment)
      if modules.parse.tst:
        modules.parse.tst = False
      rg_len = int(byte2type('UInt8', _src[0:1]))
      rg_cnt = int(byte2type('UInt8', _src[1:2]))
      rg_number += 1
      if rg_cnt > 0:
        _src =  _src[2:]
        new_idx += rg_cnt
#        for idx in range(1, int(rg_cnt)+1):
        while new_idx > 0:
          idx += 1
          alphanum_msgs[idx] = {}
          if msgid == '12233':
              alphanum_msgs[idx]['HDR_MIC'] = '-'
          if tag[0] == 'RG_12224_EMMPR':
            alphanum_msgs[idx]['HDR_MESSAGETYPE'] = '{}A'.format(message['HDR_MESSAGETYPE'])
          elif tag[0] == 'RG_12224_BR' and int(msg_vers) > 324:
            alphanum_msgs[idx]['HDR_MESSAGETYPE'] = '{}B'.format(message['HDR_MESSAGETYPE'])
          elif tag[0] == 'RG_12224_SPR' and int(msg_vers) > 324:
            alphanum_msgs[idx]['HDR_MESSAGETYPE'] = '{}C'.format(message['HDR_MESSAGETYPE'])
          elif tag[0] == 'RG_12233_TGEMMP':
            alphanum_msgs[idx]['HDR_MESSAGETYPE'] = '{}A'.format(message['HDR_MESSAGETYPE'])
          alphanum_msgs[idx]['HDR_TOPICID'] = message['HDR_TOPICID']
          alphanum_msgs[idx]['HDR_PARTITIONID'] = message['HDR_PARTITIONID']
          alphanum_msgs[idx]['HDR_OFFSETID'] = message['HDR_OFFSETID']
          alphanum_msgs[idx]['HDR_THREADID'] = message['HDR_THREADID']
          alphanum_msgs['HDR_PRODUCETIME'] = message['produceTime']
          alphanum_msgs['HDR_CONSUMETIME'] = message['consumeTime']
          alphanum_msgs[idx]['produceTime'] = message['produceTime']
          alphanum_msgs[idx]['consumeTime'] = message['consumeTime']
          alphanum_msgs[idx]['versionID'] = message['versionID']
          if msgid == '12224':
            alphanum_msgs[idx]['HDR_BATCHID'] = alphanum_msgs[0]['batchID']
            alphanum_msgs[idx].update(enrichment)
            alphanum_msgs[idx]['symbolIndex'] = message['symbolIndex']
          if msgid != '12224' or tag[0] == 'RG_12224_EMMPR':
            for a_tag in _dict_alpha:
              alphanum_msgs[idx][a_tag[0]] = ''
              alphanum_msgs[idx], _src = tag_paarse(_src, a_tag, alphanum_msgs[idx], a_tag[0])
          elif msgid == '12224' and tag[0] == 'RG_12224_BR':
              for a_tag in _dict_12224b:
                  alphanum_msgs[idx][a_tag[0]] = ''
                  alphanum_msgs[idx], _src = tag_paarse(_src, a_tag, alphanum_msgs[idx], a_tag[0])
          elif msgid == '12224' and tag[0] == 'RG_12224_SPR':
              for a_tag in _dict_12224c:
                  alphanum_msgs[idx][a_tag[0]] = ''
                  alphanum_msgs[idx], _src = tag_paarse(_src, a_tag, alphanum_msgs[idx], a_tag[0])
          new_idx = new_idx - 1
      elif rg_cnt == 0:
        _src =  _src[2:]
      else:
          if msgid not in warn_msg:
              warn_msg.append(msgid)
              print('WARNING! Number of repeating groups for {} is {}'.format(msgid,rg_cnt))
          _src = _src[2:]
  return  alphanum_msgs, _src


def parse_msg(line, msg_parsed,topic,partition,offset,msg_vers,max_vers,enrichment):
#  print(line)
  msg_parsed = {}
  alpha_msg = {}
  alpha_group = {}
  real_fields = {}
  msg_dict = imp.import_module('modules.dict.dict_'+str(msg_vers))
  msg_dict_max = imp.import_module('modules.dict.dict_'+str(max_vers))
  header_dict = msg_dict.unit_header
  h = ['msgLen','blockLen','HDR_MESSAGETYPE','schemaID','versionID']
  msg_parsed, line = tags_parse(line, header_dict, msg_parsed,'-1',msg_dict,h)
#  print(msg_parsed)
  msgid = msg_parsed['HDR_MESSAGETYPE']
  msgbody_len = msg_parsed['blockLen']
  if str(msg_vers) == '324' and msgid == '12006' and msgbody_len == '295':
    msg_dict = imp.import_module('modules.dict.dict_000_324')
  msg_parsed = msg_dict_prep(msg_dict.HDR_list, msg_parsed,msg_dict)
  msg_parsed["HDR_TOPICID"] = topic
  msg_parsed["HDR_PARTITIONID"] = partition
  msg_parsed["HDR_OFFSETID"] = str(offset)
#  msg_parsed["HDR_THREADID"] = msg_dict.threadid[topic]
  for thread in msg_dict.threadid:
        if topic not in thread: continue
        if len(msg_dict.threadid[thread][0]) > 0:
            if str(partition) in msg_dict.threadid[thread]:
                msg_parsed['HDR_THREADID'] = thread
        else:
            msg_parsed['HDR_THREADID'] = thread
  msg_parsed = msg_dict_prep(msg_dict_max.ENR_list, msg_parsed,msg_dict_max)
  count = 0
  header_parsed = msg_parsed
  unknown_msgs = {}
  topic_id = msg_dict.topicid
  if msgid in msg_dict.msgids: #  and msgid in ('12007','12006','12224'):
    if msg_dict.msgids[msgid] not in msg_dict.msgs:
      print('AHTUNG!!! {} not in dictionary'.format(msg_dict.msgids[msgid]))
      return None, msgid
    elif msgid in msg_dict.alpha_msgs:
      msga_dict = msg_dict.msgs[msg_dict.msgids['{}A'.format(msgid)]]
      msg_parsed = msg_dict_prep(msg_dict.msgs[msg_dict.msgids[msgid]], msg_parsed,msg_dict)
      msg_parsed,line = tags_parse_alpha(line, msg_dict.msgs[msg_dict.msgids[msgid]],msga_dict, msg_parsed, msgid,msg_dict,msg_vers)
#      for idx in msg_parsed.keys():
#        if msgid != '12224':
#          msg_parsed[idx]['HDR_MIC'] = '-'
      return msg_parsed, msgid
    else:
      real_fields = msg_dict_prep(msg_dict.msgs[msg_dict.msgids[msgid]], real_fields,msg_dict)
      msg_parsed = msg_dict_prep(msg_dict_max.msgs[msg_dict_max.msgids[msgid]], msg_parsed,msg_dict_max)
      msg_parsed, line = tags_parse(line, msg_dict_max.msgs[msg_dict_max.msgids[msgid]], msg_parsed, msgid,msg_dict_max,real_fields)
#      print(msg_parsed)
      if msgid not in msg_dict.splitted_msgs:
        msg_parsed['HDR_MIC'] = '-'
        if topic != 'MTXCREFD': msg_parsed["HDR_BATCHID"] = '0'
      else:
#        for ms in list(msg_parsed.values()):
          for idx in msg_parsed.keys():
            msg_parsed[idx]['HDR_MIC'] = '-'
            if topic != 'MTXCREFD': msg_parsed[idx]["HDR_BATCHID"] = '0'
      msg_parsed = enrich_msg(msg_parsed,enrichment,msgid,msg_dict)
    return msg_parsed, msgid
  else:
    return None, msgid

def parse_enrichment(line,enr_msg,msg_vers):
    msg_parsed = {}
    enrichment = {}
    msg_dict = imp.import_module("modules.dict.dict_"+str(msg_vers))
    header_dict = msg_dict.unit_header
    h = ['msgLen','blockLen','HDR_MESSAGETYPE','schemaID','versionID']
    msg_parsed, line = tags_parse(line, header_dict, msg_parsed,'-1',msg_dict,h)
    msgid = msg_parsed['HDR_MESSAGETYPE']
    msg_parsed = msg_dict_prep(msg_dict.HDR_list, msg_parsed,msg_dict)
    _dict_alpha = msg_dict.msgs[msg_dict.msgids['{}A'.format(msgid)]]
    msg_parsed = msg_dict_prep(msg_dict.msgs[msg_dict.msgids[msgid]], msg_parsed,msg_dict)
    _dict = msg_dict.msgs[msg_dict.msgids[msgid]]
    msg_parsed,line = tags_parse_alpha(line, _dict, _dict_alpha, msg_parsed, msgid,msg_dict,msg_vers)
    msg = msg_parsed[0]
    if msg['batchID'] != '1':
        return None,None
    symbol = msg['symbolIndex']
    enrichment[symbol] = {}
    for enr in list(msg_dict.ENR):
        enrichment[symbol].update({enr:msg[enr]})
    return enrichment,msgid

def enrichment_field(msg):
    enr_field = 'symbolIndex'
    if enr_field in msg:
        return enr_field
    else:
        for field in msg:
            if '_symbolIndex_1' not in field:
                continue
            else:
                return field


def enrich_msg(msg,enrichment,msgid,msg_dict):
    if msgid not in msg_dict.splitted_msgs:
        enr_field = enrichment_field(msg)
        if enr_field not in msg:
            return msg
        else:
            if msg[enr_field] not in enrichment:
                return msg
            else:
                for enr in enrichment[msg[enr_field]]:
                    msg[enr] = enrichment[msg[enr_field]][enr]
                return msg
    else:
        enr_field = enrichment_field(msg[0])
        if enr_field not in msg[0]:
            return msg
        elif msg[0][enr_field] not in enrichment:
            return msg
        else:
            for m in msg.values():
                for enr in enrichment[m[enr_field]]:
                    m[enr] = enrichment[m[enr_field]][enr]
            return msg

