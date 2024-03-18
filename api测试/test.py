import requests

url='https://shuhai.market.alicloudapi.com/api?type=stock&market=BS'
appcode=''

headers={"Authorization":"APPCODE "+appcode,"x-ca-nonce":"uniqid"}
response=requests.get(url,headers=headers)
print(response.status_code)
print(response.text)
