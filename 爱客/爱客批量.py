import requests
import json
import _thread
import time
kid_map = {'1':'189081','2':'214917'}
kid_c = input('公海：1 洛阳：2 \n')
kid = kid_map[kid_c]
start_time = input('请输入起始日期(2023-05-15)：')
end_time = input('请输入截至日期：')
all_data = []
flagaa = 0
payload = {}
headers = {
  'authorization': 'Token token="cbcb3ea779a540c6d5be737fa67072be",device="web"',
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
print(len(page_list))
def get_all(xpage):
    global flagaa
    for page in xpage:
        print(page)
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
    print(i)
    try:
        if i['status_mapped'] == '新名单':
            pass
        elif i['status_mapped'] == '废名单池':
            fmd.append(i)
        else:
            no_new.append(i)
    except:
        print(False)
print(len(no_new))
print(len(fmd))
xid = [[] for _ in range(10)]
for i in range(len(no_new)):
    xid[i%10].append(no_new[i])
flagaa = 0
def put_new(xid):
    global flagaa

    for i in range(0,len(xid),100):
        url = f"https://e.ikcrm.com/api/customer_commons/batch_update?common_id={kid}"
        headers = {
            'authority': 'e.ikcrm.com',
            'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; aliyungf_tc=adba541c78182ebece41a59d58a16950712743623512c11321384aff0bcdb428; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; _vcooline_ikcrm_production_ikcrm.com_session_=OFNSOHZxKzY3TFhISEVtTVR3a1BRMlhkS2pXUmtYckpFdTZBaU4yYmNVWDBSd1EwR3hQcGN1Nk9lenVNMXE4WnZOYTRIR1hlNXlseW1yYk5pMXNNYzY0bHQvNmZlNzJNQXp6eXA1NjIrR1JBVGFaclJMMnpmVVNFa1FReUhYS2huNW9JTnExcjdCRmgxSHlONGcwRmJubWhneXAvc2t3QnphMHpVbElkTW4yVVkwUDNZbnYxQTVVbllEK0JDRm5Dd2FjUEJFTTZobXJ6Y1pYeHJqN3hqdXhQWHdPZDgvSU9UNS9yZzgySHdQNkt4QnVpWXJNdHFtT1N1bkdybzlMSFhjUGQvRFlrKzNtdFpVR0c1NUNseUZUUWZhbTg5bUpreVprUkEwR3RKMTVEWFIydnRxNmg3VEFPZGRkYXBqYVZ6cUVQNVNLY3NBeHU4eCtUOC9DRTN1ZHFLSm5TeVd4dWFaVk5yY29ERmFRNUdjTllOU2RlRU4xaVVuSkpJL2t4dEY4c05hMVR0SnhtbTUwSmhzOXZFNXZvREtMbGFCTHZsZitydUsybmpiZz0tLTJOVjQzamQ2QmQxZjhwVnphTUIxbFE9PQ%3D%3D--9a2cd020994a88d056dbd41d8d1f3db43d29ab62',
            'origin': 'https://e.ikcrm.com',
            'referer': 'https://e.ikcrm.com/pioneers',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-csrf-token': 'y3+wmr+Tk1xCm2l+S4jLUO+0b0k9heoVvbELHCWKdqTWd/jK7ZEM5gCdNFYQXcBC2wZYsPLe6VpRX3Pz3xnzKg==',
            'x-requested-with': 'XMLHttpRequest',
            'x-tingyun': 'c=B|XKUyACVWCWU;x=8d58cd85abb14f42'
        }
        bstr = [f'&ids%5B%5D={ss["id"]}' for ss in xid[i:i+100]]
        tail = ''.join(bstr)
        payload = "utf8=%E2%9C%93&authenticity_token=NTuOTqMXe7j3WppQdgMZvopSrPewRkLJrnYlJvWFlgwvBY%2B%2BEeudzTpTmCZhuS%2FI8UbafFudsnDgvmAZDgGvOA%3D%3D&field_choice=status&customer%5Bstatus%5D=10193075" + tail

        response = requests.request("PUT", url, headers=headers, data=payload)
        try:
            tid = response.text.split('"task_id":"')[1].split('"')[0]
        except:
            print(response.text)
            break
        # print(tid)
        url = "https://e.ikcrm.com/api/batch_operation/perform"

        payload = "task_id=" + tid
        headers = {
            'authority': 'e.ikcrm.com',
            'accept': '*/*',
            'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; aliyungf_tc=adba541c78182ebece41a59d58a16950712743623512c11321384aff0bcdb428; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; _vcooline_ikcrm_production_ikcrm.com_session_=ME5XK09KaXh5dWMrZ0FJT3J3aFBudmUrSEpsZVBtdnQyN1FoKzQ3MkJkVThCbVBUWEF3ZFpYMUFsMXNnWG1hRmFDVU9EZ0ZCQmFyR2JJbXNvRkR1a3MzQXhZTGtQZmFEVFN2WXZpZ0pESXpWdmRHTXIvV2E3NWh6S2FLMzNLUjRsTlJDRXQ2SVlLQVR0dER4MjRPYUhiNjEvV05FUTFyc0V2RzFZTldSd0VlMDNWdnRkeG85NHJtemFxdVFpQ1phL1A3cjdiOGJ2UEtMT3lqV1FZaFV1dzR6SFUvVTFkMGY5clVJSjhUMll6Z0M2M3Y0Y1lUUDIzZ3VZaEI5NXVEMGdUYWVhUTRpanZmQmZ4L1lXaGRFMk1zRThBa24yeUlsSy8xWTJpekozVmtOTkw2RHdPM0hYWVJsUzRKQkhEZHFncWZqQjdua2gzb0gwZzY2eHFSN08vWU1xayt6YjFuY1FWNTkyUytnRkMwTXRUSDQxd1E1SHE1NU55bGw4YVpIU295MVRGYmlqYlN2Vy80Szc3QmZJTktwRGFkYUMrcXJxbWFJRW9jaG5ndz0tLWNVVDlNbStrL1JRb290SXdwTlo3MUE9PQ%3D%3D--bb84d0be7a7e7287c10e80c5f02186bf9cfa943f',
            'origin': 'https://e.ikcrm.com',
            'referer': 'https://e.ikcrm.com/pioneers',
            'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
            'x-csrf-token': 'y3+wmr+Tk1xCm2l+S4jLUO+0b0k9heoVvbELHCWKdqTWd/jK7ZEM5gCdNFYQXcBC2wZYsPLe6VpRX3Pz3xnzKg==',
            'x-requested-with': 'XMLHttpRequest',
            'x-tingyun': 'c=B|XKUyACVWCWU;x=874422228b894021'
        }

        response = requests.request("POST", url, headers=headers, data=payload)

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
  'cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2212624608%22%2C%22first_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fuc.weiwenjia.com%2F%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg5Mjk4MzhhZWZmYTYtMDNmMjRkZjU3NzBiOTZhLTdlNTY1NDdmLTE4MjEzNjktMTg5Mjk4MzhhZjAxNjA2IiwiJGlkZW50aXR5X2xvZ2luX2lkIjoiMTI2MjQ2MDgifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%24identity_login_id%22%2C%22value%22%3A%2212624608%22%7D%2C%22%24device_id%22%3A%2218929838aeffa6-03f24df5770b96a-7e56547f-1821369-18929838af01606%22%7D; aliyungf_tc=adba541c78182ebece41a59d58a16950712743623512c11321384aff0bcdb428; x-lx-gid=wwjiVhsWsQ2R4M9JwNlA; _vcooline_ikcrm_production_ikcrm.com_session_=ZEVvRzA1U05QbThPNUswS2ZuZ3NkazAreUhrQmRTbTV6SWVuK0dKRXRqWmlTMERrZEdHK1NjSnVSZGVuTEtna3Y2S29pYnBDQzdPSmFsQzdjRENFaWw0MU9hWHY2RjBmeFBJWFpGck8yT2M5MmtJVmxaSzRIZ05PWmZQWmtjZGJnVGFmcUg1cVpNOFR1SDFNY1JpL2NDTUZkSG13eGt6bVhydmFVRXBZcldsbUdFQ1BtK0YxVWwwZ28wbzZrUk5ZRjlaMGY4VkIybUFhdmwvc1BVeTZxaG5EWS96TGpuMFNIRk1UaGZRUnlLOUQ4VGt2WUVKeEdNQ1dvM1Q5WDRZLzUxRnJKWWk0cHEyNjE0S21LM0hSVU8zcXpPNHZuazV4TGdyTS9DM1VxRm1hYlJBMlpjL3dCTVhGVFI5OG9TMUh6WGJ3VUQydmNzZjZ6dTkxUjFmRHhaVmdadDF4TG8xWVljUHNtOGdiczI5bFd2MW9MMURrVEtMZGExUzdCNmp0UUNhcGZ4VTYyOGg3S0k4NTM3SEU3aVhIV3NCcUtCeWZJMFhFWXdNbllRUT0tLWNXV0xEcXRRL1BVTndNejhiODlmVlE9PQ%3D%3D--45b742173d50c1a49f70c43be3efe0ac4794268f',
  'origin': 'https://e.ikcrm.com',
  'referer': 'https://e.ikcrm.com/pioneers',
  'sec-ch-ua': '"Microsoft Edge";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0',
  'x-csrf-token': 'y3+wmr+Tk1xCm2l+S4jLUO+0b0k9heoVvbELHCWKdqTWd/jK7ZEM5gCdNFYQXcBC2wZYsPLe6VpRX3Pz3xnzKg==',
  'x-requested-with': 'XMLHttpRequest',
  'x-tingyun': 'c=B|XKUyACVWCWU;x=8d0c2b300f0347bd'
}
for i in fmd:
    payload += f'&customer_ids%5B%5D={i["id"]}'
response = requests.request("PUT", url, headers=headers, data=payload)
print(response.text)

