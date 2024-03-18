import base64
import requests
import json
import time
import os

def clear_folder(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Failed to delete {file_path}. Reason: {e}')

# 使用方法
folder_path = 'res_str'  # 将此处替换为你要清空的文件夹的路径
# clear_folder(folder_path)

import shutil
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
files = os.listdir('res_half_images')
idx = files.index('right_half_slide_68_image.png')
while idx < len(files):
    try:
        file = files[idx]
        print(file)

        # 打开你的图片文件，将其转换为 base64 编码
        with open('res_half_images/' + file, 'rb') as f:
            img_data = f.read()
            img_base64 = base64.b64encode(img_data).decode()

        data = {'image': img_base64}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        # 发送请求
        response = requests.post(ocr_url, params=params, headers=headers, data=data)

        # 解析结果
        result = response.json()
        with open('res_str/' + file.split('.')[0] + '.txt','w', encoding='utf8') as f:
            for item in result['words_result']:
                f.write(item['words'] + '\n')
        idx += 1
    except:
        continue
