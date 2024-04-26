import csv
import os.path
import struct
import importlib as imp


def read_csv(name):
  msgs = []
  with open('{}'.format(name), encoding='latin-1') as csvfile:
    reader  = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
      msgs.append(row)
  return msgs

def read_csv_keys(name):
  msgs = []
  with open('{}'.format(name), encoding='latin-1') as csvfile:
    reader  = csv.DictReader(csvfile, delimiter=';')
    for idx,row in enumerate(reader):
      if idx == 0:
        msgs.append(row)
        break
  return msgs

def read_enr(name):
  enrichment = {}
  count = 0
  index_name = 'symbolIndex'
  with open('{}'.format(name), encoding='latin-1') as csvfile:
    reader  = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
      if row['batchID'] == '1':
        if row[index_name] not in enrichment:
          enrichment[row[index_name]] = []
          enrichment[row[index_name]].append(row)
        else:
          count += 1
          enrichment[row[index_name]].append(row)
#  print(count)
  return enrichment

def write_csv(f_path, msg, msgid,topic):
    if 'RECO' not in topic:
        f_name = '{}/Kafka_{}.csv'.format(f_path, msgid)
    else:
        f_name = '{}/Kafka_{}_hai.csv'.format(f_path, msgid)
    if os.path.exists(f_name):
        with open(f_name, 'a', encoding='latin-1') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=msg.keys(), delimiter=';')
            writer.writerow(msg)
    else:
        with open(f_name, 'a', encoding='latin-1') as csvfile:
            writer = csv.DictWriter(csvfile,fieldnames=msg.keys(), delimiter=';')
            writer.writeheader()
            writer.writerow(msg)

def write_enrichment(enrichment,enrichment_file):
    with open(enrichment_file,'a') as enr:
        for symbol in list(enrichment.keys()):
            enr_values = str(list(enrichment.values())[0])[1:-1]
            enr.write('\''+symbol+'\':'+enr_values+'\n')

# def write_enrichment(enrichment, enrichment_file):
#     with open(enrichment_file, 'a') as enr:
#         for symbol, values in enrichment.items():
#             enr_values = ', '.join([f"'{key}': '{value}'" for key, value in values.items()])
#             enr.write(f"'{symbol}': {enr_values}\n")
