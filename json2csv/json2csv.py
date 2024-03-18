# import json
# res = [['question','answers']]
# data = json.load(open('200421_covidQA.json',encoding='utf8'))
# print(len(data['data'][0]['paragraphs'][0]['qas']))
# for i in data['data']:
#     for j in i['paragraphs'][0]['qas']:
#         res.append([])
#         res.append([j['question'],j['answers'][0]['text']])
# import csv
# res = [i for i in res if i]
# with open('200421_covidQA.csv','w',newline='',encoding='utf8') as f:
#     fcsv = csv.writer(f)
#     for i in res:
#         fcsv.writerow(i)


import json
res = []
data = json.load(open('kaggle-lit-review-0.2.csv', encoding='utf8'))
for i in data['categories']:
    for j in i['sub_categories']:
        q = j['nq_name']
        for k in j['answers']:
            res.append([q,k['exact_answer']])
import csv
with open('kaggle-lit-review-0.2.csv', 'w', newline='', encoding='utf8') as f:
    fcsv = csv.writer(f)
    for i in res:
        fcsv.writerow(i)
