import requests
import json
res = []
payload = {}

head = '代码	名称	最新价	涨跌幅	涨跌额	成交量(手)	成交额	振幅	最高	最低	今开	昨收	量比	换手率	市盈率(动态)	市净率'.split()
res.append(head)
idx = 1
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Connection': 'keep-alive',
    'Cookie': 'qgqp_b_id=8e09341a15c4595fdd83eaedc07727e0; websitepoptg_api_time=1697357897484; websitepoptg_show_time=1697357897559; st_si=17442831974908; st_asi=delete; st_pvi=99055018283049; st_sp=2023-10-15%2016%3A18%3A17; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=3; st_psi=20231015162251363-113200301321-5710832120',
    'Referer': 'http://quote.eastmoney.com/center/gridlist.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 Edg/118.0.2088.46'
}

for page in range(1,278):
    # print(page)
    url = f"http://94.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403910170819190202_1697358168400&pn={page}&pz=20&po=1&np=1&fltt=2&invt=2&wbp2u=|0|0|0|web&fid=f3&fs=m:0+t:6,m:0+t:80,m:1+t:2,m:1+t:23,m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f22,f11,f62,f128,f136,f115,f152"

    response = requests.request("GET", url, data=payload)
    data = json.loads(response.text[len('jQuery112403910170819190202_1697358168400('):-2])
    for i in data['data']['diff']:
        code = i['f12']
        name = i['f14']
        newprice = i['f2']
        updown = i['f3']
        uddetial = i['f4']
        hand = i['f5']
        count = i['f6']
        zf = i['f7']
        high = i['f15']
        low = i['f16']
        today = i['f17']
        ye = i['f18']
        lb = i['f10']
        hs = i['f8']
        syl = i['f9']
        sjl = i['f23']
        res.append([code, name, newprice, updown, uddetial, hand, count, zf, high, low, today, ye, lb, hs, syl, sjl])
        idx += 1
        print(res[-1])



from datetime import datetime, timedelta
import csv
import pandas as pd
today = datetime.now()
yesterday = today - timedelta(days=1)
formatted_date = yesterday.strftime('%Y%m%d')
df = pd.DataFrame(res[1:], columns=head)
df.to_excel('A' + formatted_date + '.xlsx', index=False)


