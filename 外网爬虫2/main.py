import csv
import pymysql
import requests
import json
import time
from selenium.webdriver.chrome.options import Options
import warnings
from selenium import webdriver
import openpyxl
import random
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from pymysql.converters import escape_string
from datetime import datetime
from dateutil.relativedelta import relativedelta
from selenium.webdriver.chrome.options import Options

uas = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',

    # Edge
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38',
    # 2021.09
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.44',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.47',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.31',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.37',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36 Edg/94.0.992.38',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.47',
    # 2021.10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.40',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.44',
    # 2021.11
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36 Edg/96.0.1054.29',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.41',
    # 2021.12
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.43',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55',
    # 2022.01
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.76',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.43',
    # 2022.02
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36 Edg/98.0.1108.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.55',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.56',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36 Edg/98.0.1108.62',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.30',
    # 2022.03
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36 Edg/99.0.1150.39',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.52',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.55',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36 Edg/100.0.1185.29',
    # 2022.04
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.44',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 Edg/100.0.1185.50',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39',
    # 2022.05
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.30',
    # 2022.06
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.33',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.41',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.124 Safari/537.36 Edg/102.0.1245.44',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44',
    # 2022.07
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36 Edg/103.0.1264.49',

    # Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.54 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    # 2021.10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
    # 2021.11
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',
    # 2021.12
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36',
    # 2022.01
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.81 Safari/537.36',
    # 2022.02
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 2022.03
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.60 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    # 2022.04
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    # 2022.05
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.115 Safari/537.36',
    # 2022.06
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36',
    # 2022.07

    # Chrome Beta
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.41 Safari/537.36',
    # 2021.09
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.17 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.32 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.40 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.49 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.18 Safari/537.36',
    # 2021.10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.27 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.35 Safari/537.36',
    # 2021.11
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',

    # Firefox
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',  # 2021.09
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:93.0) Gecko/20100101 Firefox/93.0',  # 2021.10
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',  # 2021.11
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0',  # 2021.12
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0',  # 2022.01
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0',  # 2022.02
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:98.0) Gecko/20100101 Firefox/98.0',  # 2022.03
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0',  # 2022.04
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:100.0) Gecko/20100101 Firefox/100.0',  # 2022.05
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:101.0) Gecko/20100101 Firefox/101.0',  # 2022.06
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',  # 2022.06
]
headers = {
    'User_Agent': random.choice( uas ),
    'accept': 'application/json, text/plain, */*',
    'x-request-id': 'c9b044b568414eb98af8d292024eed88',
    'connection':'close',
    'referer': 'https://coinmarketcap.com/',
    'platform': 'web',
    'accept-encoding': 'gzip, deflate',
}
ex = openpyxl.open('data.xlsx')
sheet = ex.active
data = sheet.values
wb = openpyxl.Workbook()
sheet_ = wb.active
db = pymysql.connect(port=3306,user='ccc',password='123456',host = 'localhost',database='ww')
cursor = db.cursor()

def get(url,table_name):
        warnings.filterwarnings('ignore')
        while True:
            try:
                resp = requests.get(url,headers=headers,verify=False)
                data_ = json.loads(resp.text)
                break
            except:
                continue
        if data_['data']['quotes'] == []:
            pass
            # print('这玩意儿没东西')
        else:
            for i in data_['data']['quotes']:
                date = i['timeOpen'].split('T')[0]
                open = i['quote']['open']
                high = i['quote']['high']
                low = i['quote']['low']
                close = i['quote']['close']
                volume = i['quote']['volume']
                market_cap = i['quote']['marketCap']
                # print( f'{date}---{open}---{high}---{low}---{close}---{volume}---{market_cap}')
                cursor.execute(f'insert into {escape_string(table_name)}(date,open,high,low,close,volume,market_cap) values({date},{open},{high},{low},{close},{volume},{market_cap})')
                db.commit()

date = ['2012-01-01 8:00:00','2012-01-31 08:00:00', '2012-03-01 08:00:00', '2012-03-31 08:00:00', '2012-04-30 08:00:00', '2012-05-30 08:00:00', '2012-06-29 08:00:00', '2012-07-29 08:00:00', '2012-08-28 08:00:00', '2012-09-27 08:00:00', '2012-10-27 08:00:00', '2012-11-26 08:00:00', '2012-12-26 08:00:00', '2013-01-25 08:00:00', '2013-02-24 08:00:00', '2013-03-26 08:00:00', '2013-04-25 08:00:00', '2013-05-25 08:00:00', '2013-06-24 08:00:00', '2013-07-24 08:00:00', '2013-08-23 08:00:00', '2013-09-22 08:00:00', '2013-10-22 08:00:00', '2013-11-21 08:00:00', '2013-12-21 08:00:00', '2014-01-20 08:00:00', '2014-02-19 08:00:00', '2014-03-21 08:00:00', '2014-04-20 08:00:00', '2014-05-20 08:00:00', '2014-06-19 08:00:00', '2014-07-19 08:00:00', '2014-08-18 08:00:00', '2014-09-17 08:00:00', '2014-10-17 08:00:00', '2014-11-16 08:00:00', '2014-12-16 08:00:00', '2015-01-15 08:00:00', '2015-02-14 08:00:00', '2015-03-16 08:00:00', '2015-04-15 08:00:00', '2015-05-15 08:00:00', '2015-06-14 08:00:00', '2015-07-14 08:00:00', '2015-08-13 08:00:00', '2015-09-12 08:00:00', '2015-10-12 08:00:00', '2015-11-11 08:00:00', '2015-12-11 08:00:00', '2016-01-10 08:00:00', '2016-02-09 08:00:00', '2016-03-10 08:00:00', '2016-04-09 08:00:00', '2016-05-09 08:00:00', '2016-06-08 08:00:00', '2016-07-08 08:00:00', '2016-08-07 08:00:00', '2016-09-06 08:00:00', '2016-10-06 08:00:00', '2016-11-05 08:00:00', '2016-12-05 08:00:00', '2017-01-04 08:00:00', '2017-02-03 08:00:00', '2017-03-05 08:00:00', '2017-04-04 08:00:00', '2017-05-04 08:00:00', '2017-06-03 08:00:00', '2017-07-03 08:00:00', '2017-08-02 08:00:00', '2017-09-01 08:00:00', '2017-10-01 08:00:00', '2017-10-31 08:00:00', '2017-11-30 08:00:00', '2017-12-30 08:00:00', '2018-01-29 08:00:00', '2018-02-28 08:00:00', '2018-03-30 08:00:00', '2018-04-29 08:00:00', '2018-05-29 08:00:00', '2018-06-28 08:00:00', '2018-07-28 08:00:00', '2018-08-27 08:00:00', '2018-09-26 08:00:00', '2018-10-26 08:00:00', '2018-11-25 08:00:00', '2018-12-25 08:00:00', '2019-01-24 08:00:00', '2019-02-23 08:00:00', '2019-03-25 08:00:00', '2019-04-24 08:00:00', '2019-05-24 08:00:00', '2019-06-23 08:00:00', '2019-07-23 08:00:00', '2019-08-22 08:00:00', '2019-09-21 08:00:00', '2019-10-21 08:00:00', '2019-11-20 08:00:00', '2019-12-20 08:00:00', '2020-01-19 08:00:00', '2020-02-18 08:00:00', '2020-03-19 08:00:00', '2020-04-18 08:00:00', '2020-05-18 08:00:00', '2020-06-17 08:00:00', '2020-07-17 08:00:00', '2020-08-16 08:00:00', '2020-09-15 08:00:00', '2020-10-15 08:00:00', '2020-11-14 08:00:00', '2020-12-14 08:00:00', '2021-01-13 08:00:00', '2021-02-12 08:00:00', '2021-03-14 08:00:00', '2021-04-13 08:00:00', '2021-05-13 08:00:00', '2021-06-12 08:00:00', '2021-07-12 08:00:00', '2021-08-11 08:00:00', '2021-09-10 08:00:00', '2021-10-10 08:00:00', '2021-11-09 08:00:00', '2021-12-09 08:00:00', '2022-01-08 08:00:00', '2022-02-07 08:00:00', '2022-03-09 08:00:00', '2022-04-08 08:00:00', '2022-05-08 08:00:00', '2022-06-07 08:00:00', '2022-07-07 08:00:00', '2022-08-06 08:00:00', '2022-09-05 08:00:00', '2022-10-05 08:00:00', '2022-11-04 08:00:00', '2022-12-04 08:00:00', '2023-01-03 08:00:00', '2023-02-02 08:00:00']

def get_id(id,table_name):
    header = {
        'User_Agent': random.choice( uas ),
        'cookie': 'cmc-language=en; gtm_session_first=%222023-01-18T12%3A12%3A13.216Z%22; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185c4cb448239-04c1b401f76e7a-17525635-1296000-185c4cb448393f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1YzRjYjQ0ODIzOS0wNGMxYjQwMWY3NmU3YS0xNzUyNTYzNS0xMjk2MDAwLTE4NWM0Y2I0NDgzOTNmIn0%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%22185c4cb448239-04c1b401f76e7a-17525635-1296000-185c4cb448393f%22%7D; _ga=GA1.2.735143844.1674043936; _gid=GA1.2.1267459485.1674043936; _fbp=fb.1.1674043943793.871278570; _tt_enable_cookie=1; _ttp=qn5tjJtb6KskkRN1t8ImNArS59f; bnc-uuid=dbbada5f-9f1d-4ed0-8292-8c1f1c8ee95f; cmc_gdpr_hide=1; gtm_session_last=%222023-01-18T15%3A14%3A06.626Z%22; _dc_gtm_UA-40475998-1=1'
    }
    num=0
    with ThreadPoolExecutor(10) as p:
        for i in range(len(date)-1):
                start = int(time.mktime(time.strptime(date[num], "%Y-%m-%d %H:%M:%S")))
                end = int(time.mktime(time.strptime(date[num+1], "%Y-%m-%d %H:%M:%S")))
                # print(f'{date[num]}  --  {date[num+1]}')
                num+=1
                href = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/historical?id={id}&convertId=2781&timeStart={start}&timeEnd={end}"
                p.submit(get,href,table_name)



for i in data:
    print(i)
    if i[0] == 'None':
        exit()
    else:
        warnings.filterwarnings( 'ignore' )
        id = i[0].split( '/' )[-1].replace( '.png', '' )
        name = i[1]
        table_name = name.replace(' ','_').replace('*','').replace('-','').replace('.','_').replace('(','').replace(')','').replace('[','').replace(']','').replace('&','').replace('+','').replace(':','')  +'_' + id
        db.ping( reconnect=True )
        cursor.execute( f'drop table if exists {table_name}' )
        cursor.execute(f'''CREATE TABLE `{escape_string(table_name)}` (
      `date` text,
      `open` text,
      `high` text,
      `low` text,
      `close` text,
      `volume` text,
      `market_cap` text
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8''')

        cursor.execute(f"insert into {escape_string(table_name)}(date,open,high,low,close,volume,market_cap) values('date','open','high','low','close','volume','market_cap')")
        db.commit()
        # print(table_name)
        get_id(id,table_name)





