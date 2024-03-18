#coding=utf8

import requests
import json
import csv

url = "https://finance.pae.baidu.com/vapi/v1/hotrank?tn=wisexmlnew&dsp=iphone&product=stock&day=20220929&hour=13&pn=0&rn=10&market=ab&type=day&finClientType=pc"

payload={}
headers = {
  'authority': 'finance.pae.baidu.com',
  'accept': 'application/vnd.finance-web.v1+json',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'cookie': 'BIDUPSID=FA91E9F86B5E503D4D49E6FAFFDFD0E9; PSTM=1664278458; BAIDUID=6BDB8893CF013A14725BB15494DA894D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=6BDB8893CF013A14725BB15494DA894D:FG=1; BA_HECTOR=218524al042h8k84ak2gf2ha1hj83931a; ZFY=QqgL:B90TevytRaBZKdaj7aKbORvrvLZ:BbmlM:AF3wI2M:C; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=8bdwgt3g6vy&ss=l8mgrobe&sl=4&tt=2c4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=baz&ul=10ek2&hd=10elw"',
  'origin': 'https://gushitong.baidu.com',
  'referer': 'https://gushitong.baidu.com/',
  'sec-ch-ua': '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
}

response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)


head = ['名称','代码','最新价','涨跌幅']
with open('data1.csv','w',newline='',encoding='gbk') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in data['Result']['body']:
        f_csv.writerow([i[0],i[3],i[4],i[1]])




url = "https://finance.pae.baidu.com/selfselect/getmarketrank?sort_type=1&sort_key=15&from_mid=1&pn=0&rn=100&group=pclist&type=ab&finClientType=pc"

payload={}
headers = {
    'authority': 'finance.pae.baidu.com',
    'accept': 'application/vnd.finance-web.v1+json',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cookie': 'BIDUPSID=FA91E9F86B5E503D4D49E6FAFFDFD0E9; PSTM=1664278458; BAIDUID=6BDB8893CF013A14725BB15494DA894D:FG=1; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BAIDUID_BFESS=6BDB8893CF013A14725BB15494DA894D:FG=1; BA_HECTOR=218524al042h8k84ak2gf2ha1hj83931a; ZFY=QqgL:B90TevytRaBZKdaj7aKbORvrvLZ:BbmlM:AF3wI2M:C; ariaDefaultTheme=undefined; RT="z=1&dm=baidu.com&si=8bdwgt3g6vy&ss=l8mgrobe&sl=4&tt=2c4&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=baz&ul=10ek2&hd=10elw"',
    'origin': 'https://gushitong.baidu.com',
    'referer': 'https://gushitong.baidu.com/',
    'sec-ch-ua': '"Microsoft Edge";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.53'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = response.text

s = json.loads(data)
res = []
head = ['名称','代码','最新价','涨跌幅','换手率','成交额','成交量','振幅','总市值']
for i in s['Result']['Result'][0]['DisplayData']['resultData']['tplData']['result']['rank']:
    row = []
    row.append(i['name'])
    row.append(i['code'])
    row.append(i['list'][0]['value'])  # 最新价
    row.append(i['list'][1]['value'])  # 涨跌幅
    row.append(i['list'][2]['value'])  # 换手率
    row.append(i['list'][3]['value'])  # 成交额
    row.append(i['list'][4]['value'])  # 成交量
    row.append(i['list'][5]['value'])  # 振幅
    row.append(i['list'][6]['value'])  # 总市值
    res.append(row)
with open('data2.csv','w',newline='',encoding='gbk') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i in res:
        f_csv.writerow(i)



