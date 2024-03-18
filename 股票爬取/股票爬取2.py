import requests
from datetime import datetime, timedelta
import json
import pandas as pd
res = []
today = datetime.now()

yesterday = today - timedelta(days=1)
ftoday = yesterday.strftime('%Y-%m-%d')
page = 1
while True:
    try:
        url = f"https://datacenter-web.eastmoney.com/api/data/v1/get?sortColumns=SECURITY_CODE%2CTRADE_DATE&sortTypes=1%2C-1&pageSize=50&pageNumber={page}&reportName=RPT_DAILYBILLBOARD_DETAILSNEW&columns=SECURITY_CODE%2CSECUCODE%2CSECURITY_NAME_ABBR%2CTRADE_DATE%2CEXPLAIN%2CCLOSE_PRICE%2CCHANGE_RATE%2CBILLBOARD_NET_AMT%2CBILLBOARD_BUY_AMT%2CBILLBOARD_SELL_AMT%2CBILLBOARD_DEAL_AMT%2CACCUM_AMOUNT%2CDEAL_NET_RATIO%2CDEAL_AMOUNT_RATIO%2CTURNOVERRATE%2CFREE_MARKET_CAP%2CEXPLANATION%2CD1_CLOSE_ADJCHRATE%2CD2_CLOSE_ADJCHRATE%2CD5_CLOSE_ADJCHRATE%2CD10_CLOSE_ADJCHRATE%2CSECURITY_TYPE_CODE&source=WEB&client=WEB" \
              f"&filter=(TRADE_DATE%3C%3D%27{ftoday}%27)(TRADE_DATE%3E%3D%27{ftoday}%27)"

        payload = {}
        response = requests.request("GET", url,  data=payload)

        data = json.loads(response.text)
        for item in data['result']['data']:
            code = item['SECURITY_CODE']
            name = item['SECURITY_NAME_ABBR']
            exp = item['EXPLAIN']
            close = item['CLOSE_PRICE']
            updown = item['CHANGE_RATE']
            net = item['BILLBOARD_NET_AMT']
            buy = item['BILLBOARD_BUY_AMT']
            sell = item['BILLBOARD_SELL_AMT']
            deal = item['BILLBOARD_DEAL_AMT']
            amount = item['ACCUM_AMOUNT']
            netr = item['DEAL_NET_RATIO']
            amountr = item['DEAL_AMOUNT_RATIO']
            hand = item['TURNOVERRATE']
            lt = item['FREE_MARKET_CAP']
            expe = item['EXPLANATION']
            res.append([code, name, ftoday, exp, close, updown, net, buy, sell, deal, amount, netr, amountr, hand, lt, expe])
        page += 1
    except:
        break
head = """代码
名称
日期
解读 
收盘价	
涨跌幅	
净买额(万)	
买入额(万)	
卖出额(万)	
成交额(万)	
市场总成交额(万)	
净买额占总成交比	
成交额占总成交比	
换手率	
流通市值(亿)	
上榜原因""".split('\n')
formatted_date = yesterday.strftime('%Y%m%d')
df = pd.DataFrame(res, columns=head)
df.to_excel('d:\\sj\lhb\lhb' + formatted_date + '.xlsx', index=False)