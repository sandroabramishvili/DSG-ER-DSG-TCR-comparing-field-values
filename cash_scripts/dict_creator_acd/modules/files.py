import os
import shutil
import datetime
import modules.const
import modules.conf
import modules.messages


today = datetime.datetime.today().strftime('%Y%m%d')

def create_dirs(dir_path,dict_type,venue):
    dict_dir = dir_path+'/dict_dir'
    if not os.path.exists('{}/'.format(dict_dir)):
        os.makedirs('{}/'.format(dict_dir))
    if not os.path.exists('{}/{}/'.format(dict_dir,dict_type)):
        os.makedirs('{}/{}/'.format(dict_dir,dict_type))
    if not os.path.exists('{}/{}/{}'.format(dict_dir,dict_type,venue)):
        os.makedirs('{}/{}/{}'.format(dict_dir,dict_type,venue))
    output_dir = '{}/{}/{}'.format(dict_dir,dict_type,venue)
    return output_dir

def write_from_list(d_list,parser_dict):
    ln_list = len(d_list)
    for idx,field in enumerate(d_list):
        if idx != ln_list - 1:
            parser_dict.write('\''+str(field)+'\', ')
        else:
            parser_dict.write('\''+str(field)+'\']\n\n')

def write_from_list_of_lists(d_list,parser_dict):
    ln_list = len(d_list)
    for idx,field in enumerate(d_list):
        if idx != ln_list - 1:
            parser_dict.write('\t'+str(field)+',\n')
        else:
            parser_dict.write('\t'+str(field)+'\n]\n\n')

def write_from_dict(d_dict,parser_dict):
    ln_dict = len(d_dict)
    for idx,field in enumerate(d_dict):
        if idx != ln_dict - 1:
            parser_dict.write('\t\''+field+'\': \''+str(d_dict[field])+'\',\n')
        else:
            parser_dict.write('\t\''+field+'\': \''+str(d_dict[field])+'\'\n}\n\n')

def write_from_dict_of_dicts(d_dict,parser_dict):
    ln_dict = len(d_dict)
    for idx,field in enumerate(d_dict):
        if idx != ln_dict - 1:
            parser_dict.write('\t\''+field+'\': '+str(d_dict[field])+',\n')
        else:
            parser_dict.write('\t\''+field+'\': '+str(d_dict[field])+'\n}\n\n')

def write_checker_dict(output_dir,venue,sbe_vers,msgs_dict,msgids,etypes,enums,unit_header_fields,rtf_header_fields,rtf_parser_header_fields):
    f_path = '{}/dict_{}.py'.format(output_dir,sbe_vers)
    if os.path.exists('{}'.format(f_path)):
        os.remove('{}'.format(f_path))
    with open(f_path,'a',encoding='latin-1') as check_dict:
        check_dict.write('# -*- coding: utf-8 -*-\n\n')
        check_dict.write('msgs = {}\n\n')
        check_dict.write('msgids = {\n')
        write_from_dict(msgids,check_dict)
        check_dict.write('unit_header_fields = [')
        write_from_list(unit_header_fields,check_dict)
        check_dict.write('rtf_header_fields = [')
        write_from_list(rtf_header_fields,check_dict)
        check_dict.write('rtf_parser_header_fields = [')
        write_from_list(rtf_parser_header_fields,check_dict)
        check_dict.write('enum_types = {\n')
        write_from_dict(etypes,check_dict)
        check_dict.write('enums = {\n')
#       write_from_dict(enums,check_dict)
        ln_dict = len(enums)
        for idx,enum in enumerate(enums):
            if idx != ln_dict - 1:
                check_dict.write('\t\''+enum+'\': '+str(enums[enum])+',\n')
            else:
                check_dict.write('\t\''+enum+'\': '+str(enums[enum])+'\n}\n\n')
        for msg in msgs_dict:
            check_dict.write('msgs[\''+msg+'\'] = {\n')
            ln_msg = len(msgs_dict[msg])
            for idx,field in enumerate(msgs_dict[msg]):
                if idx != ln_msg - 1:
                    check_dict.write('\t\''+field+'\': '+str(msgs_dict[msg][field])+',\n')
                else:
                    check_dict.write('\t\''+field+'\': '+str(msgs_dict[msg][field])+'\n}\n\n')

def write_parser_dict(output_dir,venue,parser_source, sbe_vers, msgs,msgids):
    f_path = '{}/dict_{}.py'.format(output_dir,sbe_vers)
    if os.path.exists(f_path):
        os.remove(f_path)
    with open(f_path,'a',encoding='latin-1') as parser_dict:
        parser_dict.write('# -*- coding: utf-8 -*-\n\n')
        parser_dict.write('msgs = {}\n\n')
        parser_dict.write('msgids = {\n')
        write_from_dict(msgids,parser_dict)
        parser_dict.write('topicid = {\n')
        write_from_dict(modules.const.topicid,parser_dict)
        threadid = modules.conf.get_threadid()
        parser_dict.write('threadid = {\n')
#        write_from_dict(modules.const.threadid,parser_dict)
        write_from_dict_of_dicts(threadid,parser_dict)
        parser_dict.write('unit_header = [\n')
        write_from_list_of_lists(modules.const.unit_header,parser_dict)
        parser_dict.write('ENR = {\n')
        write_from_dict(modules.const.ENR,parser_dict)
        parser_dict.write('ENR_list = [\n')
        write_from_list_of_lists(modules.const.ENR_list,parser_dict)
        if venue in ('cdw','bi'):
            parser_dict.write('splitted_msgs = [\n')
            write_from_list(modules.const.splitted_msgs,parser_dict)
            parser_dict.write('alpha_msgs = [\n')
            write_from_list(modules.const.alpha_msgs,parser_dict)
        if venue == 'cdw':
#            parser_dict.write('unit_header = [\n')
#            write_from_list_of_lists(modules.const.unit_header,parser_dict)
            parser_dict.write('HDR_list = [\n')
            write_from_list_of_lists(modules.const.HDR_list,parser_dict)
#            parser_dict.write('splitted_msgs = [\n')
#            write_from_list_of_lists(modules.const.splitted_msgs,parser_dict)
#            parser_dict.write('alpha_msgs = [\n')
#            write_from_list_of_lists(modules.const.alpha_msgs,parser_dict)
        elif venue == 'bi':
            parser_dict.write('rtf_header = [\n')
            if parser_source == 'kfk':
                write_from_list_of_lists(modules.const.rtf_header,parser_dict)
            elif parser_source == 'rtf':
                write_from_list_of_lists(modules.const.rtf_parser_header,parser_dict)
            parser_dict.write('HDR_list = [\n')
            write_from_list_of_lists(modules.const.rtf_HDR_list,parser_dict)
        elif venue == 'ptc':
#            parser_dict.write('unit_header = [\n')
#            write_from_list_of_lists(modules.const.unit_header,parser_dict)
            parser_dict.write('HDR_list = [\n')
            write_from_list_of_lists(modules.const.HDR_list,parser_dict)
        for msg in msgs:
            parser_dict.write('msgs[\''+msg+'\'] = [\n')
            write_from_list_of_lists(msgs[msg],parser_dict)

def write_msgs_maker_dict(output_dir,sbe_vers,msgs_dict,msgids,etypes,enums):
    f_path = '{}/dict_{}.py'.format(output_dir,sbe_vers)
    if os.path.exists('{}'.format(f_path)):
        os.remove('{}'.format(f_path))
    with open(f_path,'a',encoding='latin-1') as check_dict:
        check_dict.write('# -*- coding: utf-8 -*-\n\n')
        check_dict.write('msgs = {}\n\n')
        check_dict.write('msgids = {\n')
        write_from_dict(msgids,check_dict)
        check_dict.write('enum_types = {\n')
        write_from_dict(etypes,check_dict)
        check_dict.write('enums = {\n')
        ln_dict = len(enums)
        for idx,enum in enumerate(enums):
            if idx != ln_dict - 1:
                check_dict.write('\t\''+enum+'\': '+str(enums[enum])+',\n')
            else:
                check_dict.write('\t\''+enum+'\': '+str(enums[enum])+'\n}\n\n')
        for msg in msgs_dict:
            check_dict.write('msgs[\''+msg+'\'] = {\n')
            ln_msg = len(msgs_dict[msg])
            for idx,field in enumerate(msgs_dict[msg]):
                if idx != ln_msg - 1:
                    check_dict.write('\t\''+field+'\': '+str(msgs_dict[msg][field])+',\n')
                else:
                    check_dict.write('\t\''+field+'\': '+str(msgs_dict[msg][field])+'\n}\n\n')

