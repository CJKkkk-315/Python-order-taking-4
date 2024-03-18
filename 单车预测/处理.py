import csv
import numpy as np
import random
import os
files = os.listdir('data/cu_')
for file in files:
    tianqi = ['晴天','阴天','雨天']
    def process_data(file):
        data = []
        time_data = {}
        with open(file) as f:
            f_csv = csv.reader(f)
            for i in f_csv:
                data.append(i)
        data = data[1:]
        for i in data:
            if i[-2] in ['6','7']:
                continue
            if int(i[-1]) < 6 or int(i[-1]) > 22:
                continue
            day = int(i[3].split()[0].split('/')[-1])
            if day not in time_data:
                time_data[day] = [0 for _ in range(24)]
            time_data[day][int(i[-1])] += 1
        return time_data

    res_data = []
    time_data = process_data(f'data/cu_/{file}')
    print(time_data)
    tianqi_d = {key:random.choices(tianqi,weights=(20,4,4),k=1)[0] for key in time_data.keys()}
    for key in time_data:
        for i in range(len(time_data[key])):
            res_data.append([i,tianqi_d[key],random.randint(170,220)/10,file.split('_')[1].split('.')[0],time_data[key][i]])
    with open('res_data.csv','a+',newline='') as f:
        f_csv = csv.writer(f)
        for i in res_data:
            if int(i[0]) < 6 or int(i[0]) > 22:
                continue
            f_csv.writerow(i)
