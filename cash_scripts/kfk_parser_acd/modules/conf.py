import os
import re
import shutil
import importlib as imp


def get_brokers():
    env_config_file = '/app/opdssacd/argocdw/env/environment.cfg'
    brokers = []
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
            if line.startswith('brokers='):
                broker_list = str(line.split('=')[1]).split(',')
                for broker in broker_list:
                    if broker not in brokers:
                        brokers.append(broker)
    return brokers

