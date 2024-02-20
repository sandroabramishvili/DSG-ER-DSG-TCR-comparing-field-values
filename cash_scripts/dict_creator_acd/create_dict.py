#!/usr/bin/python3.6

import os
import re
import shutil
import argparse
import importlib as imp
import xml.etree.ElementTree as ET
import modules.messages as mes
import modules.const
import modules.conf
import modules.files as files


a_parser = argparse.ArgumentParser()
a_parser.add_argument('-v','--vers',action = 'store', type = str,help = 'SBE version or all to create dictionaries for all versions in modules/xml directory')
a_parser.add_argument('-e','--env',action = 'store', type = str,choices = ['cdw','bi','ptc'],help = 'Venue: cdw, bi or ptc')
a_parser.add_argument('-s','--sourse', action = 'store',required = False, type = str,choices = ['kfk', 'rtf','db'], help = 'Choose the data source: kfk, rtf,db')
a_parser.add_argument('-t','--type', action = 'store', type = str,choices = ['parser','checker','msgs_maker'], help = 'Choose dictionary type: parser, checker')
#a_parser.add_argument('-m','--messages', action = 'store', type = str,nargs = '+',help = 'Message ids')
args = a_parser.parse_args()

sbe_vers = args.vers
venue = args.env
data_source = args.sourse
dict_type = args.type

dir_path = os.path.dirname(os.path.realpath(__file__))
output_dir = modules.files.create_dirs(dir_path,dict_type,venue)

all_dicts = []

if sbe_vers == 'all':
    for xml_dict in os.listdir(dir_path+'/modules/xml/'):
        all_dicts.append(re.sub('[^0-9]','',xml_dict))
else:
    all_dicts.append(sbe_vers)

def field_type(f):
    if f.attrib['type'].startswith('char'):
        if f.attrib['type'] == 'char':
            type_info = ('1','Char')
        else:
            type_info = (f.attrib['type'][4:], 'Char')
    elif f.attrib['type'].endswith('_enum') or f.attrib['type'].endswith('_set'):
        if etypes[f.attrib['type']].startswith('char'):
            type_info = (etypes[f.attrib['type']][4:], 'Char')
        else:
            type_info = modules.const.types[etypes[f.attrib['type']]]
    else:
        type_info = modules.const.types[f.attrib['type']]
    return type_info


def  add_field(f,r_name,r_gr_name,m):
    type_info = field_type(f)
    if r_name:
        for r in range(1,int(modules.const.rg_cnt[r_gr_name][1])+1):
            fields[r_name+f.attrib['name']+'_{}'.format(r)] = [type_info[0],type_info[1],f.attrib['type']]
    else:
        fields[f.attrib['name']] = [type_info[0],type_info[1],f.attrib['type']]
    return fields


for vers in all_dicts:
    xml_file = dir_path+'/modules/xml/sbe_input_{}.xml'.format(vers)

    tree = ET.parse(xml_file)
    root = tree.getroot()
    message_tag = root.tag[:-6]

#msgids = id:msg name
    msgids = {}
#full_msgs = msgid:field name: [length,type, original type]
    full_msgs = {}
#msgs = msg_name/rg_name:[field name,length,type]
    msgs = {}
#null_values = {type: null value}
    null_values = {}
# enums = enum/set field name: [possible values]
    enums = {}
# etypes = enum/set field name:type
    etypes = {}

    if venue =='cdw' and dict_type != 'msgs_maker':
        msgids['12224A'] = 'RG_12224_EMMPR'
        msgids['12233A'] = 'RG_12233_TGEMMP'
        if int(vers) > 324:
          msgids['12224B'] = 'RG_12224_BR'
          msgids['12224C'] = 'RG_12224_SPR'

# Define null values and and enums/sets
    for idx,t in enumerate(root[0]):
        if t.attrib['name'].startswith('int') or t.attrib['name'].startswith('uint') or t.attrib['name'] in ('unsigned_char','time_t'):
            null_values[t.attrib['name']] = t.attrib['nullValue']
        elif '_enum' in t.attrib['name'] or '_set' in t.attrib['name']:
            for en in t.iter('enum'):
                if en.attrib['encodingType'] == 'char':
                    etypes[en.attrib['name']] ='char1'
                else:
                    etypes[en.attrib['name']] = en.attrib['encodingType']
                vvalues = []
                for a in en.iter('validValue'):
                    vvalues.append(a.text)
                enums[en.attrib['name']] = vvalues
            for en in t.iter('set'):
                if en.attrib['encodingType'] == 'char':
                    etypes[en.attrib['name']] = 'char1'
                else:
                    etypes[en.attrib['name']] = en.attrib['encodingType']
                vvalues = []
                for a in en.iter('choice'):
                    vvalues.append(a.text)
                enums[en.attrib['name']] = vvalues

# Create dictionary with message id
    for child in root:
        for m in child.iter(message_tag):
            if m.attrib['id'] not in mes.dict_venue['{}'.format(venue)]:
                continue
            if m.attrib['id'] in ('12002','12224') and dict_type == 'checker' and venue == 'bi':
                for i in range(1,6):
                    msgids[m.attrib['id']+'_{}'.format(i)] = m.attrib['name']
            else:
                msgids[m.attrib['id']] = m.attrib['name']
            fields = {}
            n_gr = 0
            for f in m.iter():
                rep_group = []
                if f.tag == message_tag:
                    continue
                if f.tag != 'group':
                    if m.attrib['name'] not in msgs and n_gr == 0:
                        msgs[m.attrib['name']] = []
                    if n_gr == 0:
                        field_name = f.attrib['name']
                        if venue == 'cdw' and f.attrib['name'].lower() == 'session' and dict_type != 'msgs_maker':
                            field_name = 'session_'
                        type_info = field_type(f)
                        msgs[m.attrib['name']].append([field_name,type_info[0],type_info[1]])
                    add_field(f,None,None,m)
                else:
                    r_gr_name = 'RG_'+m.attrib['id']+'_'+re.sub('[^A-Z0-9]','',f.attrib['name'])
                    r_name = re.sub('[^A-Z0-9]','',f.attrib['name']) + '_'
                    if r_gr_name not in rep_group and (f.attrib['name'] != 'CommercialFields' and m.attrib['id'] not in ('12006','12007')):
                        rep_group.append(r_gr_name)
                    elif f.attrib['name'] == 'CommercialFields' and m.attrib['id'] in ('12006','12007'):
                        r_gr_name = 'RG_{}_CF1'.format(m.attrib['id'])
                        rep_group.append(r_gr_name)
                        r_name = re.sub('[^A-Z0-9]','',f.attrib['name']) + '1_'
                    if r_gr_name  not in msgs:
                        n_gr += 1
                        msgs[r_gr_name] = []
                        if venue == 'cdw' and dict_type != 'msgs_maker':
                            msgs[m.attrib['name']].append([r_gr_name,modules.const.rg_cnt[r_gr_name][0]])
                        elif venue == 'bi' or dict_type == 'msgs_maker':
                            msgs[m.attrib['name']].append([r_gr_name,modules.const.rg_cnt[r_gr_name][1]])
                        elif venue == 'ptc':
                            msgs[m.attrib['name']].append([r_gr_name,modules.const.rg_cnt[r_gr_name][2]])
                    for g in f.iter('field'):
                        field_name = g.attrib['name']
                        if venue == 'cdw' and g.attrib['name'].lower() == 'session'  and dict_type != 'msgs_maker':
                            field_name = 'session_'
                        type_info = field_type(g)
                        msgs[r_gr_name].append([field_name,type_info[0],type_info[1]])
                        add_field(g, r_name,r_gr_name,m)
            if m.attrib['id'] in ('12002','12224') and dict_type == 'checker' and venue == 'bi':
                for i in range(1,6):
                    full_msgs[m.attrib['id']+'_{}'.format(i)] = fields
            else:
                full_msgs[m.attrib['id']] = fields

    unit_header_fields = []
    rtf_header_fields = []
    rtf_parser_header_fields = []

    for u_field in modules.const.unit_header:
        unit_header_fields.append(u_field[0])
    for r_field in modules.const.rtf_header:
        rtf_header_fields.append(r_field[0])
    for rp_field in modules.const.rtf_parser_header:
        rtf_parser_header_fields.append(rp_field[0])

    if dict_type == 'checker':
        files.write_checker_dict(output_dir,venue,vers,full_msgs,msgids,etypes,enums,unit_header_fields,rtf_header_fields,rtf_parser_header_fields)
    elif dict_type == 'parser':
        files.write_parser_dict(output_dir,venue,data_source, vers, msgs,msgids)
    elif dict_type == 'msgs_maker':
        files.write_msgs_maker_dict(output_dir,vers,full_msgs,msgids,etypes,enums)
