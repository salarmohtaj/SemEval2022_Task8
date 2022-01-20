import pandas as pd
import os
import json

data_dir = '../Data'
input_data_name = 'semeval-2022_task8_train-data_batch_v0.2.csv'
output_data_name = 'URLs.DIC'

df = pd.read_csv(os.path.join(data_dir,input_data_name))
doc_dic = {}
counter = 0

for index, row in df.iterrows():
    ids = row["pair_id"]
    ids = ids.split("_")
    id1 = ids[0]
    id2 = ids[1]
    url1_1 = row["link1"]
    url1_2 = row["ia_link1"]
    url2_1 = row["link2"]
    url2_2 = row["ia_link2"]
    try:
        doc_dic[id1]
        counter += 1
    except KeyError:
        doc_dic[id1] = {"url_original" : url1_1,
                        "url_backup" : url1_2}
    try:
        doc_dic[id2]
        counter += 1
    except KeyError:
        doc_dic[id2] = {"url_original": url2_1,
                        "url_backup": url2_2}

input_data_name = 'semeval-2022_task8_eval_data_202201.csv'
df = pd.read_csv(os.path.join(data_dir,input_data_name))
for index, row in df.iterrows():
    ids = row["pair_id"]
    ids = ids.split("_")
    id1 = ids[0]
    id2 = ids[1]
    url1_1 = row["link1"]
    url1_2 = row["ia_link1"]
    url2_1 = row["link2"]
    url2_2 = row["ia_link2"]
    try:
        doc_dic[id1]
        counter += 1
    except KeyError:

        doc_dic[id1] = {"url_original" : url1_1,
                        "url_backup" : url1_2}
    try:
        doc_dic[id2]
        counter += 1
    except KeyError:
        doc_dic[id2] = {"url_original": url2_1,
                        "url_backup": url2_2}

print(f'The number of documents that repeated more than one time is {counter} documents.')
print(f'There are the total number of {len(doc_dic)} documents to scrap.')
with open(os.path.join(data_dir, output_data_name), "w") as f:
    json.dump(doc_dic, f)
