import requests
import json
import pandas as pd

# 你的百度云应用的 AppID、API Key、Secret Key
APP_ID = '35732874'
API_KEY = 'UV6pMYUDUBC2zM3IG0z7xYGg'
SECRET_KEY = 'aEWNLV5Va2OO65wS7PS4Rr2A1Wokz48H'

# 通过上面3个参数，可以获取到一个token，本质就是一个加密字符串
def get_access_token():
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={}&client_secret={}'.format(API_KEY, SECRET_KEY)
    response = requests.get(url)
    if response:
        return response.json()['access_token']

def sentiment_analysis(text):
    # 获取到token以后，对百度云的url发送一个post请求，带上你要分析的文本和token，就可以得到结果
    token = get_access_token()
    url = 'https://aip.baidubce.com/rpc/2.0/nlp/v1/sentiment_classify?charset=UTF-8&access_token={}'.format(token)
    data = {
        "text": text,
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    if response:
        # 将结果返回
        return response.json()

if __name__ == "__main__":
    # 读取文件中的数据
    df = pd.read_excel("data/抓取数据合集.xlsx")
    idx = 0
    texts = df["发布内容"].tolist()
    confidences = []
    positives = []
    sentiments = []
    # 遍历每一条文本
    now_stop = 0
    while idx < len(texts):
        res = sentiment_analysis(texts[idx])
        try:
            # 数据存在items中，以列表形式，下面三个参数分别为置信度，正面得分，情感分类
            res = res['items'][0]
            confidences.append(res['confidence'])
            positives.append(res['positive_prob'])
            sentiments.append(res['sentiment'])
            idx += 1
            now_stop = 0
        # 有的时候会触发每秒申请限制，重新发一次就好了
        except:
            print(res)
            now_stop += 1
            if now_stop >= 10:
                idx += 1
                confidences.append(0)
                positives.append(0)
                sentiments.append(0)

        print(idx)
    # 保存为结果excel
    df['confidence'] = confidences
    df['score'] = positives
    df['sentiment'] = sentiments
    df.to_excel('情感分析结果.xlsx')
