import dict
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

def msg_dict_prep(_dict, message,msg_vers,idx):
    msg_dict = imp.import_module('modules.dict.dict_'+str(msg_vers))
    rg_list = []
    for tag in _dict:
        if tag[0][0:3] != 'RG_':
            message[tag[0]] = ''
        else:
            if 'HDR_MESSAGETYPE' in message:
                if tag[0] not in rg_list and message['HDR_MESSAGETYPE'].isdigit():
                    rg_list.append(tag[0])
                    message['{}_{}'.format(tag[0][9:],'count')] = ''
                elif message['HDR_MESSAGETYPE'].isalpha() and message['HDR_MESSAGETYPE'] not in rg_list:
                    rg_list.append(message['HDR_MESSAGETYPE'])
                    message['RG_{}cnt'.format(message['HDR_MESSAGETYPE'])] = ''
            if int(tag[1]) == 0:
                continue
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

def tags_parse(_src, _dict, message, msgid,msg_vers,real_fields,parse_enr,enrichment):
    msg_dict = imp.import_module('modules.dict.dict_'+msg_vers)
    split_msgs = {}
    alphanum_msgs = {}
    mes = {}
    rg_list = []
    new_idx = 0
    idx = 0
    symbol = ''
    for n_tag,tag in enumerate(_dict):
        if len(_src) == 0 : continue
        if 'RG_' not in tag[0]:
            if tag[0] not in real_fields: continue
            message[0], _src = tag_paarse(_src, tag, message[0], tag[0])
            if msgid == '12224':
                for e in msg_dict.ENR:
                    message[0][e] = message[0][msg_dict.ENR[e]]
            if 'produceTime' in message[0]:
                message[0]['HDR_PRODUCETIME'] = message[0]['produceTime']
            if 'consumeTime' in message[0]:
                message[0]['HDR_CONSUMETIME'] = message[0]['consumeTime']
            if 'batchID' in message[0]:
                message[0]['HDR_BATCHID'] = message[0]['batchID']
        elif parse_enr:
            _src = ''
            break
        else:
            rg_len = int(byte2type('UInt8', _src[0:1]))
            rg_cnt = int(byte2type('UInt8', _src[1:2]))
            if tag[0] not in rg_list and not tag[3]:
                rg_list.append(tag[0])
                cnt_name = '{}_count'.format(tag[0][9:])
                message[0][cnt_name] = str(rg_cnt)
            _src = _src[2:]
            new_msgid = ''
            if rg_cnt > 0 and tag[0] in msg_dict.msgs:
                if not tag[2] and not tag[3]:
                    mes = {}
                    if 'HDR_PRODUCETIME' in message[0]:
                        mes['HDR_PRODUCETIME'] = message[0]['HDR_PRODUCETIME']
                    for rdx in range(1, int(rg_cnt)+1):
                        for rg_tag in msg_dict.msgs[tag[0]]:
                            if '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx) not in real_fields:
                                continue
                            if rdx <= int(tag[1]):
                                mes, _src = tag_paarse(_src, rg_tag, mes, '{}_{}_{}'.format(tag[0][9:],rg_tag[0], rdx))
                            else:
                                _src = _src[int(rg_tag[1]):]
                    for m in message:
                        if m['HDR_MESSAGETYPE'].isdigit():
                            m.update(mes)
                elif tag[2]:                            #if tag[2] is 1 repeating group is splitted
                    for rdx in range(rg_cnt):
                        if len(message) < rdx+1 and rdx != 0:
                            message.append(copy.deepcopy(message[0]))
                        split_msgs[rdx] = copy.deepcopy(message[rdx])
                        for rg_tag in msg_dict.msgs[tag[0]]:
                            if '{}_{}_1'.format(tag[0][9:],rg_tag[0]) not in real_fields:
                                continue
                            split_msgs[rdx], _src = tag_paarse(_src, rg_tag, split_msgs[rdx], '{}_{}_1'.format(tag[0][9:],rg_tag[0]))
                            message[rdx].update(split_msgs[rdx])
                elif tag[3]:             #if tag[3] is 1 repeating group is alphanumeric
                    if msg_dict.msgids[msgid + 'A'] == tag[0]:
                        new_msgid = msgid + 'A'
                        new_msg_name = msg_dict.msgids[new_msgid]
                    elif msgid + 'B' in msg_dict.msgids:
                        if msg_dict.msgids[msgid + 'B'] == tag[0]:
                            new_msgid = msgid + 'B'
                            new_msg_name = msg_dict.msgids[new_msgid]
                    elif msgid + 'C' in msg_dict.msgids:
                        if msg_dict.msgids[msgid + 'C'] == tag[0]:
                            new_msgid = msgid + 'C'
                            new_msg_name = msg_dict.msgids[new_msgid]
                    new_idx += rg_cnt
                    while new_idx > 0:
                        message.append({})
                        alpha_enriched = 0
                        idx = len(message) - 1
                        message[idx] = msg_dict_prep(msg_dict.HDR_list, message[idx],str(msg_vers),1)
                        cnt_name = 'RG_{}cnt'.format(new_msgid)
                        message[idx][cnt_name] = str(rg_cnt)
                        message[idx]['HDR_MESSAGETYPE'] = new_msgid
                        message[idx]['HDR_TOPICID'] = message[0]['HDR_TOPICID']
                        message[idx]['HDR_PARTITIONID'] = message[0]['HDR_PARTITIONID']
                        message[idx]['HDR_OFFSETID'] = message[0]['HDR_OFFSETID']
                        message[idx]['HDR_THREADID'] = message[0]['HDR_THREADID']
                        message[idx]['HDR_PRODUCETIME'] = message[0]['HDR_PRODUCETIME']
                        message[idx]['HDR_BATCHID'] = message[0]['HDR_BATCHID']
                        new_dict = msg_dict.msgs[new_msg_name]
                        message[idx] = msg_dict_prep(msg_dict.ENR_list, message[idx],str(msg_vers),1)
                        for e in msg_dict.ENR:
                            message[idx][e] = message[0][e]
                        message[idx] = msg_dict_prep(msg_dict.msgs[new_msg_name], message[idx],msg_vers,idx)
                        for new_tag in new_dict:
                            message[idx], _src = tag_paarse(_src, new_tag, message[idx], new_tag[0])
                        if msgid == '12044':
                            message[idx].update({'messageType':message[0]['messageType']})
                        new_idx = new_idx - 1
                if mes:
                    for m in message:
                        if m['HDR_MESSAGETYPE'].isdigit():
                            m.update(mes)
            elif rg_cnt < 0 :
                if msgid not in warn_msg:
                    warn_msg.append(msgid)
                    print('WARNING! Repiting group count = {} for {}'.format(rg_cnt,msgid))
    return message, _src

def parse_msg(line, msg_parsed,topic,partition,offset,msg_vers,max_vers,enrichment,timestp):
    msg_parsed = []
    msg_parsed.append({})
    real_fields = {}
    msg_dict = imp.import_module('modules.dict.dict_'+str(msg_vers))
    msg_dict_max = imp.import_module('modules.dict.dict_'+str(max_vers))
    header_dict = msg_dict.unit_header
    h = ['msgLen','blockLen','HDR_MESSAGETYPE','schemaID','versionID']
    msg_parsed, line = tags_parse(line, header_dict, msg_parsed,'-1',str(max_vers),h,None,enrichment)
    msgid = msg_parsed[0]['HDR_MESSAGETYPE']
    msgbody_len = msg_parsed[0]['blockLen']
    msg_parsed[0] = msg_dict_prep(msg_dict.HDR_list, msg_parsed[0],msg_vers,1)
    msg_parsed[0]["HDR_TOPICID"] = topic
    msg_parsed[0]["HDR_PARTITIONID"] = partition
    msg_parsed[0]["HDR_OFFSETID"] = str(offset)
    msg_parsed[0]['HDR_MIC'] = ''
    msg_parsed[0]['HDR_PRODUCETIME'] = timestp
    for thread in msg_dict.threadid:
        if topic not in thread: continue
        if str(partition) in msg_dict.threadid[thread] and thread[5:13] == topic:
            msg_parsed[0]['HDR_THREADID'] = thread
        else:
            continue
#            msg_parsed[0]['HDR_THREADID'] = thread
    if 'MTX' not in topic:
        msg_parsed[0]['HDR_BATCHID'] = '0'
    msg_parsed[0] = msg_dict_prep(msg_dict_max.ENR_list, msg_parsed[0],str(max_vers),1)
    if msgid in msg_dict.msgids:
        if msg_dict.msgids[msgid] not in msg_dict.msgs:
            print('AHTUNG!!! {} not in dictionary'.format(msg_dict.msgids[msgid]))
            return None, msgid
        else:
            real_fields = msg_dict_prep(msg_dict.msgs[msg_dict.msgids[msgid]], real_fields,msg_vers,1)
            msg_parsed[0] = msg_dict_prep(msg_dict_max.msgs[msg_dict_max.msgids[msgid]], msg_parsed[0],max_vers,1)
            msg_parsed, line = tags_parse(line, msg_dict_max.msgs[msg_dict_max.msgids[msgid]], msg_parsed, msgid,str(max_vers),real_fields,None,enrichment)
            if msgid != '12224':
                for _msg in msg_parsed:
                    enrich_msg(_msg,enrichment,msgid,msg_dict)
            return msg_parsed, msgid
    else:
        return None,msgid

def parse_enrichment(line,enr_msg,msg_vers):
    msg_parsed = []
    msg_parsed.append({})
    enrichment = {}
    msg_dict = imp.import_module("modules.dict.dict_"+str(msg_vers))
    header_dict = msg_dict.unit_header
    h = ['msgLen','blockLen','HDR_MESSAGETYPE','schemaID','versionID']
    msg_parsed, line = tags_parse(line, header_dict, msg_parsed,'-1',msg_vers,h,1,{})
    msgid = msg_parsed[0]['HDR_MESSAGETYPE']
    msg_parsed[0] = msg_dict_prep(msg_dict.HDR_list, msg_parsed[0],msg_vers,1)
    msg_parsed[0] = msg_dict_prep(msg_dict.msgs[msg_dict.msgids[msgid]], msg_parsed[0],msg_vers,1)
    msg_parsed, line = tags_parse(line, msg_dict.msgs[msg_dict.msgids[msgid]], msg_parsed, msgid,str(msg_vers),msg_parsed[0],1,{})
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
