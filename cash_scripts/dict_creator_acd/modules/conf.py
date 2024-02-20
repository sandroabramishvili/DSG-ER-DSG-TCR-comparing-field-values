import os
import re
import shutil
import importlib as imp


def old_round_robin(all_partitions,topic_split,part_num):
    lists = [[] for _ in range(int(topic_split))]
    max_number = int(part_num/topic_split)
    for idx,part in enumerate(all_partitions):
        current_list = int(idx/max_number)
        lists[current_list].append(part)
    return lists

def round_robin(all_partitions,topic_split,part_num):
    topic_split = int(topic_split)
    lists = [[] for _ in range(int(topic_split))]
    for idx,part in enumerate(all_partitions):
        current_list = idx%topic_split
        lists[current_list].append(part)
    return lists

def get_threadid():
    dir_path = '/app/opdssacd/argocdw/env/'
    env_config_file = '/app/opdssacd/argocdw/env/environment.cfg'
    part_dict = {}
    threadid = {}
    thread = ''
    for csv_file in os.listdir('/app/opdssacd/argocdw/files/csvout/'):
        if '_file_part.csv' in csv_file:
            part_list_file = '/app/opdssacd/argocdw/files/csvout/'+csv_file
    with open(part_list_file,'r') as part:
        all_part = part.readlines()
        for line in all_part:
            if 'topic_id' in line:  continue
            line = line.strip()
            line = re.sub('\s+','',line)
            line = re.sub('"','',line)
            if len(line) == 0: continue
            if '#' in line:
                comment_start = line.find('#')
                if comment_start == 0: continue
                line = line[:comment_start]
            if line.endswith(';'): line = line[:-1]
            top_id,prt = line.split(';')
            part_dict.update({top_id:prt})
    with open(env_config_file,'r') as env:
        all_conf = env.readlines()
        for line in all_conf:
            line = line.strip()
            line = line.strip(';')
            line = re.sub('\s+','',line)
            line = re.sub('"','',line)
            if len(line) == 0: continue
            if '#' in line:
                comment_start = line.find('#')
                if comment_start == 0: continue
                line = line[:comment_start]
            if line.endswith(';'): line = line[:-1]
            if line.startswith('K2CDW'):
                all_partitions = []
                thread = re.sub('[^0-9A-Z]','',line)
                if thread not in threadid:
                    threadid[thread] = []
                continue
            elif line.startswith('topic='):
                topic = line.split('=')[1]
                if topic in ('RECOBLKT','RECOETFT','RECOFXIT') and topic not in part_dict:
                    topic_split = 1
                    instance_number = 1
                    part_num = 15
                elif topic == 'RECOEQUT' and topic not in part_dict:
                    topic_split = 1
                    instance_number = 1
                    part_num = 60
                elif topic == 'RECOWART' and topic not in part_dict:
                    topic_split = 1
                    instance_number = 1
                    part_num = 30
                else:
                    part_num = int(part_dict[topic])
#                all_partitions = [par for p in range(part_num) par.append(p)]
                for p in range(part_num):
                    all_partitions.append(str(p))
            elif line.startswith('topic_split'):
                topic_split = int(line.split('=')[1])
            elif line.startswith('instance_number'):
                instance_number = int(line.split('=')[1])
                part_split = round_robin(all_partitions,topic_split,part_num)
                threadid[thread] = part_split[instance_number-1]
    return threadid
