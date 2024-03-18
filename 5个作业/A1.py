import json
q1list = json.load(open('fitness.json',encoding='utf8'))

import csv
header = ['title', 'districts', 'districtl', 'latitude', 'longitude', 'length', 'mincal', 'maxcal']
res = []
for item in q1list:
    Title = item['Title']
    DistrictS = item['DistrictS']
    DistrictL = item['DistrictL']
    Latitude = item['Latitude']
    Longitude = item['Longitude']
    Length = item['Route'].split(':')[1].strip().split()[0]
    mincal = item['Route'].split(':')[2].strip().split()[0].split('-')[0]
    maxcal = item['Route'].split(':')[2].strip().split()[0].split('-')[1]
    res.append([Title,DistrictS,DistrictL,Latitude,Longitude,Length,mincal,maxcal])
with open('Q1_fitness.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(header)
    for row in res:
        f_csv.writerow(row)
