import requests
import json
import _thread
import time
kid_map = {'1':'189081','2':'214917'}
kid_c = '2'
kid = kid_map[kid_c]
start_time = '2023-07-03'
end_time = '2023-07-05'
all_data = []
flagaa = 0
payload = {}
headers = {
  'authorization': 'Token token="08cb17a98df078b285d629a51188bf8e",device="web"',
}
url = f"https://e.ikcrm.com/api/pc/customer_commons?common_id={kid}&filters%5B%5D%5Bname%5D=flow_into_at&filters%5B%5D%5Boperator%5D=within&filters%5B%5D%5Bquery%5D%5B%5D={start_time}&filters%5B%5D%5Bquery%5D%5B%5D={end_time}&page=1&per_page=200"
response = requests.request("GET", url, headers=headers, data=payload)
data = json.loads(response.text)
total_page = data['data']['total_pages']
page_list = list(range(1,total_page+1))
# print(page_list)
xpage = [[] for _ in range(10)]
for i in range(len(page_list)):
    xpage[i%10].append(page_list[i])
def get_all(xpage):
    global flagaa
    for page in xpage:
        # print(page)
        url = f"https://e.ikcrm.com/api/pc/customer_commons?common_id={kid}&filters%5B%5D%5Bname%5D=flow_into_at&filters%5B%5D%5Boperator%5D=within&filters%5B%5D%5Bquery%5D%5B%5D={start_time}&filters%5B%5D%5Bquery%5D%5B%5D={end_time}&page={page}&per_page=200"
        page += 1
        response = requests.request("GET", url, headers=headers, data=payload)
        data = json.loads(response.text)
        all_data.extend(data['data']['list'])
    flagaa += 1
for i in range(10):
    _thread.start_new_thread(get_all, (xpage[i],))
while 1:
    time.sleep(1)
    if flagaa == 10:
       break

headers = {
    'authority': 'e.ikcrm.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'authorization': 'Token token="08cb17a98df078b285d629a51188bf8e",device="web"',
    'content-type': 'application/json',
    'cookie': 'aliyungf_tc=0600ed58f79a1f97a36d2d25ce0314366f2cc781eea0bf8954032fc831dacf51; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2221711784%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjE3MTE3ODQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2221711784%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=dC9XYkw5SVhuUXB3Y2VJSGIzaWlxUGsxS0Y5RmRmUDlaajlUa1FxYStPS0oyU3gyM1NuOWdORUtzS2ZUbHpuUjFTVmFwMGZSWlFGaXhwQzY0M04veDJRRHRrbU40SWFoaGxyMTZHK05GQ05kdEUrdGxHZTBFQ3A3Q1RVR3BBcHlvdXovRy9CeEtTNnpLMkk3YThoRVVuZnFJSysxWkhockFZa0I1U0FuN3pLVjdiNlhyQ1BkeUJIKzBvY0tPNFpHV2tOU1o4c0IxNitXZDcxaFFqNmRIdFUvVFFpTTl4NlNDRlpzK2wzUklhdnAzTDZ5M1QwRTlseEl5ZURUR2JoTnRQbXQ2UHhVSFRqQWNLZTJtd3p4WEdMMS9oUUhEYlRFaG5WTmYzMjk5ZnZ6ZGkxQ0llU0ZvRWZhVzd5SENGc2hpMldscHlmK3Y3QkdEVVBWWldQSU96ZEs5VFI4WWo5ZU1WSndKbVluQ3I4RlhIckg5cms4TXRrRWYzUFBScitURnMvQXBjd3BiMTd3blpNYURqMGdXemo5cVpmNG44WEJzM2dPR0hUQVFTUT0tLUhjMk43VFVGdzhteHE5M2VkUHdsREE9PQ%3D%3D--904060b99ec2a9b0bebc288de3d14d49348ddd71; _vcooline_ikcrm_production_ikcrm.com_session_=ZFpUenlwYWZMeEEwUDlUWW5wT3puWitEcWF5V1ROaG1KSVRMcGlJTm02Y2M1b2h1QTdmc09wUDA4T3A1N25wbHVSYnVlZ0Jac3R2SFoxK3dwcFEyUzVwSGFMNDVxR05rOTdOMnhCdEJsR3U0bDlvM3poT1BlZXJXckc3enB6UFBiVm5NdFE1bFV0VFIyTzhXNWM1WjJOS1E3a2UzSngxcFhZMkt6MHVXQnBmSU5oWDFEYndZTHpZZEEyc2d3aDgyR05sc3RVMmRaSUF4dXVTQVFySkR0dm04MzRvdHdibHI1c21seFFpeTdjVVlLYjBSbzFoWk9ZWkpqWFBOblRYemZuWkdPWDBCZGdnUVZsaXFONXdycGpFS2dtbWxJU0plci9DeHJMZXdBUlRuYUNNeHZFTUowMVpVQlkwQ0pralhyL1dabkdiNXFma3lDd0E5Z29KRkloZ0JrU1dsUlp1ekdCQ3l6dkZLN0lkc1lYNVdNRS9jQ2RPdmUxMkFvN1Z1NTVNNWVVMTZpTjFPbDFEZTJ5d2lvWlZIRGZxK2xNRVNhbm5VM1BVdlBuND0tLUx0MUg4d1J5ZWxvWmNLWWJ0N0t2WFE9PQ%3D%3D--d2ec5be2238c8316fe6a1ef809c496f650365c5e',
    'origin': 'https://e.ikcrm.com',
    'referer': 'https://e.ikcrm.com/pioneers',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
    'x-lx-gid': 'wwjiVhsWsQ2R4M9JwNlA',
    'x-tingyun': 'c=B|XKUyACVWCWU;x=d86731ebacd8431d'
}
fmd = []
no_new = []

for i in all_data:
    if i['status_mapped'] == '新名单':
        pass
    elif i['status_mapped'] == '废名单池':
        fmd.append(i)
    else:
        no_new.append(i)
print(len(no_new))
print(len(fmd))
xid = [[] for _ in range(10)]
for i in range(len(no_new)):
    xid[i%10].append(no_new[i])
flagaa = 0
def put_new(xid):
    global flagaa
    for i in xid:
        url = f"https://e.ikcrm.com/api/pc/customer_commons/{i['id']}"
        payload = json.dumps({
            "customer": {
                "status": 10193075
            },
            "common_id": int(kid)
        })
        response = requests.request("PUT", url, headers=headers, data=payload)
        print(response.text)
    flagaa += 1
for i in range(10):
    _thread.start_new_thread(put_new, (xid[i],))
while 1:
    time.sleep(1)
    if flagaa == 10:
       break


url = f"https://e.ikcrm.com/api/customer_commons/massive_transfer_to_other_customer_common?common_id={kid}"

payload = f"authenticity_token=2swkQ6tKpzos41PnAEqaCiiH3N%2FgKXZdUnMjCC8UeEbA8iWzGbZBT%2BHqUZEX8Kx8U5OqVAvyhuQcu2Y31JBBcg%3D%3D&common_id={kid}&customer_common_id=189136"
headers = {
  'authority': 'e.ikcrm.com',
  'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
  'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
  'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'cookie': 'aliyungf_tc=0600ed58f79a1f97a36d2d25ce0314366f2cc781eea0bf8954032fc831dacf51; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2221711784%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMjE3MTE3ODQifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2221711784%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; _vcooline_ikcrm_production_ikcrm.com_session_=TXgzaUxBQnNFQkVOVUtEOHdNQjNRNWtweWowcFZqK0czTzhWQW9ITnFhSVducVdBY2VXNk9FYVk1L2xlTjFBajJncVRkZ1MrWHR3UFVtUEdkRld6UGVreE9rS1ZiakN5c2ZkUDF4Yk5DemlGcFBGZENpTTZCV2E2bW0xN0lnVGhEZWNTWjF2SDF2N05YRHRKaFIxcnFFYzZwMjZqOU8ydlB0aGxHL2I1UXJMeGdwZk1mRjVKVVBISGhwcDFTNUtzZmVXcTBjRjhndFpHWTRSRkVqTXVjbFE4ajRlNm83Mm5UWmRDUEtWc3labHBqUXdFOUx6dXNCaGJFTkpXYTNaYUlzUUlTeklzQVZNRyszQ29RNFFITzVoZk5oeVYzSHg4MHE4dk9uZXN0OUJnOGVVWTExZmptekpsaGFKREk1ejdsNmlqcmUrcFBWeVovRG1kSzJVekd5WUFFc2E0Rm1MK05mOVViMWtaa0JiUmw5SnRPdWZFNlpqQStObFpIZVNhNnlwZkIyVS91Z1FzOW5rZzE0UlpyaWRzTnA4c003YzRBT0Y5aW9LaUF6ST0tLVo2eHduVEg5MCtURitEdVdLZHgrcVE9PQ%3D%3D--78accf9733c96914bd2f9d11131c7edd28695383; _vcooline_ikcrm_production_ikcrm.com_session_=ZFpUenlwYWZMeEEwUDlUWW5wT3puWitEcWF5V1ROaG1KSVRMcGlJTm02Y2M1b2h1QTdmc09wUDA4T3A1N25wbHVSYnVlZ0Jac3R2SFoxK3dwcFEyUzVwSGFMNDVxR05rOTdOMnhCdEJsR3U0bDlvM3poT1BlZXJXckc3enB6UFBiVm5NdFE1bFV0VFIyTzhXNWM1WjJOS1E3a2UzSngxcFhZMkt6MHVXQnBmSU5oWDFEYndZTHpZZEEyc2d3aDgyR05sc3RVMmRaSUF4dXVTQVFySkR0dm04MzRvdHdibHI1c21seFFpeTdjVVlLYjBSbzFoWk9ZWkpqWFBOblRYemZuWkdPWDBCZGdnUVZsaXFONXdycGpFS2dtbWxJU0plci9DeHJMZXdBUlRuYUNNeHZFTUowMVpVQlkwQ0pralhyL1dabkdiNXFma3lDd0E5Z29KRkloZ0JrU1dsUlp1ekdCQ3l6dkZLN0lkc1lYNVdNRS9jQ2RPdmUxMkFvN1Z1NTVNNWVVMTZpTjFPbDFEZTJ5d2lvWlZIRGZxK2xNRVNhbm5VM1BVdlBuND0tLUx0MUg4d1J5ZWxvWmNLWWJ0N0t2WFE9PQ%3D%3D--d2ec5be2238c8316fe6a1ef809c496f650365c5e',
  'origin': 'https://e.ikcrm.com',
  'referer': 'https://e.ikcrm.com/pioneers',
  'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67',
  'x-csrf-token': '2swkQ6tKpzos41PnAEqaCiiH3N/gKXZdUnMjCC8UeEbA8iWzGbZBT+HqUZEX8Kx8U5OqVAvyhuQcu2Y31JBBcg==',
  'x-requested-with': 'XMLHttpRequest',
  'x-tingyun': 'c=B|XKUyACVWCWU;x=c076bdcdc0454ded'
}
for i in fmd:
    payload += f'&customer_ids%5B%5D={i["id"]}'
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)

