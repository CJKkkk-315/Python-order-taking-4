import base64
import requests
import json
import os
import time
# 你的 API Key 和 Secret Key
API_KEY = 'PkALfQZqAA0I4AV0zl4kSbAy'
SECRET_KEY = 'bbOChyCkGBMBTYWsyq8ScGMZ9XcLw34u'

# 获取 access token
auth_url = "https://aip.baidubce.com/oauth/2.0/token"
params = {
    'grant_type': 'client_credentials',
    'client_id': API_KEY,
    'client_secret': SECRET_KEY
}
headers = {'Content-Type': 'application/json; charset=UTF-8'}
response = requests.get(auth_url, params=params, headers=headers)
access_token = response.json()['access_token']

# 调用 OCR API
ocr_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
params = {'access_token': access_token}
files = os.listdir('res_mix_images2')
idx = 0
while idx < len(files):
    file = files[idx]
    print(file)
    try:
        # 打开你的图片文件，将其转换为 base64 编码
        with open('res_mix_images2/' + file, 'rb') as f:
            img_data = f.read()
            img_base64 = base64.b64encode(img_data).decode()

        data = {'image': img_base64}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 发送请求
        response = requests.post(ocr_url, params=params, headers=headers, data=data)

        # 解析结果
        result = response.json()
        with open('res_str2/' + file.split('.')[0] + '.txt','w',encoding='utf8') as f:
            for item in result['words_result']:
                f.write(item['words'] + '\n')
        idx += 1
    except:
        pass
