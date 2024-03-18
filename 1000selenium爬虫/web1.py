import requests
from datetime import datetime
import json
import pandas as pd
today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")

need = [i for i in open('Saxo.txt').read().split('\n') if i]
need = need[1:]
res = {i:[] for i in need}

url = "https://www.home.saxo/en-HK/rnc/hsp"

payload = {'date': formatted_today}
response = requests.request("POST", url, data=payload)
data = json.loads(response.text)['rncHistoricSwapPoints']
all_date = data['filters'][0]['options'][1:]
all_date = [i['value'] for i in all_date][1:]
print(all_date)
for date in all_date:
    print(date)
    payload = {'date': date}
    response = requests.request("POST", url, data=payload)
    body = json.loads(response.text)['rncHistoricSwapPoints']['tableData']['body']
    for item in body:
        cell = [i['name'] for i in item['cells']]
        if cell[0] in res and not res[cell[0]]:
            res[cell[0]] = cell[1:]
    flag = 1
    for key in res:
        if not res[key]:
            flag = 0
            break
    if flag:
        break

ans = [['Forex cross','From','To','Long positions','Short positions']]
for key in need:
    ans.append([key] + res[key])
df = pd.DataFrame(ans)

from openpyxl import load_workbook
# 加载已经存在的excel文件
book = load_workbook(f'swap_{formatted_today}.xlsx')

with pd.ExcelWriter(f'swap_{formatted_today}.xlsx', engine='openpyxl', mode='a') as writer:
    df.to_excel(writer, sheet_name='SAXO')
