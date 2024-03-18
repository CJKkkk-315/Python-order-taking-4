import requests
import csv
import json
url = "https://terminus.isprimefx.com/json/tomnextrates"

payload = {}
headers = {
  'Cookie': 'SENTRY_SESS_ID=c5bb1560c7fb7822fde3a502ccf082b76bef3a28lukd2f7x0a1kvw*h*v3zxl*y\'k(1dt6k)wxa0hpf(el1j~qr.u43a64k\'dk)4j\'i'
}

response = requests.request("GET", url, headers=headers, data=payload)
head = 'Currency Pair,Quote Date,Near Value Date,Far Value Date,Bid Price,Ask Price'.split(',')
print(response.text)
data = json.loads(response.text)
res = []
for i in data['data']:
    res.append([i['fxPair'],i['quoteDt'],i['nearDt'],i['farDt'],str(i['shortRate']),str(i['longRate'])])
import datetime


current_time = str(datetime.datetime.now())
year = current_time.split('-')[0]
mouth = current_time.split('-')[1]
day = current_time.split('-')[2].split()[0]
hour = current_time.split('-')[2].split()[1].split(':')[0]
mi = current_time.split('-')[2].split()[1].split(':')[1]
with open(f'Current_Tom Next Rates_{year+mouth+day}_{hour+mi}.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerows(res)
