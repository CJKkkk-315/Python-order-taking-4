import requests
import json
import csv
headers = {
    'Connection':'close',
}
s = requests.session()
f_csv = csv.writer(open('F:\\res.csv','w',newline=''))
urls = [i.replace('\n','') for i in open('address.txt').readlines()]
for url in urls:
    try:
        with requests.Session() as s:
            res = s.get('https://chain.api.btc.com/v3/address/' + url,headers=headers)
            data = json.loads(res.text)
            f_csv.writerow([url,data['data']['balance']])
            print([url,data['data']['balance']])
    except:
        print('https://chain.api.btc.com/v3/address/' + url)