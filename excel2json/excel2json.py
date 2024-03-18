import json

import pandas as pd
import datetime as dt
import random
import string
df = pd.read_excel('宁上A4梁场与桥面系施工台账2023-10-9.xlsx', sheet_name='智慧梁场(溪南港)', engine='openpyxl')
df = df.head(355)
df2 = pd.read_excel('宁上A4梁场与桥面系施工台账2023-10-9.xlsx', sheet_name='智慧梁场(甘棠) ', engine='openpyxl')
df2 = df2.head(8)
df = pd.concat([df,df2],ignore_index=True)
new_columns = list(string.ascii_uppercase)[:len(df.columns)]
column_mapping = dict(zip(df.columns, new_columns))
df.rename(columns=column_mapping, inplace=True)
df['name'] = df['B'].astype(str) + df['C'].astype(str)
df['pourtime'] = pd.to_datetime(df['G'].astype(str) + ' ' + df['H'].str.split('-').str[0], format='%Y-%m-%d %H:%M')
df['steamtime'] = pd.to_datetime(df['I'].str.split('～').str[0])
df['tietime'] = df['pourtime'] - pd.to_timedelta(pd.Series([random.randint(2,3) for _ in range(len(df))]).astype(str) + ' hours')
df['tietime'] = pd.to_datetime(df['E'].astype(str) + ' ' + df['tietime'].dt.strftime('%H:%M'))
# print(df['tietime'])
time_columns = ['pourtime', 'steamtime', 'tietime']
for col in time_columns:
    df[col] = df[col] + pd.to_timedelta(pd.Series([random.randint(0,59) for _ in range(len(df))]).astype(str) + ' seconds')
    df[col] = df[col].dt.floor('S')
    df[col] = (df[col].astype('int64') // 10 ** 9).astype('int64')
res = {'data':[]}
df = df[['name','pourtime','steamtime','tietime']]
for row in df.values:
    res['data'].append({'name':row[0],'pourtime':row[1],'steamtime':row[2],'tietime':row[3]})
import json
with open('res.json','w') as f:
    json.dump(res, f, ensure_ascii=False)
