import requests
import json
import time
import threading
import csv
res = []
flag = 0


def thread_func(hqdata):
    global flag
    url = 'https://gbm.wanda.cn/member-rights/coupon/receivedCinemaCoupon'
    headers = {
        'Host': 'gbm.wanda.cn',
        'Connection': 'keep-alive',
        'Content-Length': '306',
        'Pragma': 'no-cache',
        'Cache-Control': 'no-cache',
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0.1; MuMu Build/V417IR; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.120 Mobile Safari/537.36 HQZLWEB/0.0.1(4.4.0)',
        'Content-Type': 'application/json; charset=UTF-8',
        'Origin': 'https://gbm.wanda.cn',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://gbm.wanda.cn/h5/',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cookie': 'sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218530203768351-0ae597a22b1f89-5355860-410774-185302037693a3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22identities%22%3A%22eyIkaWRlbnRpdHlfY29va2llX2lkIjoiMTg1MzAyMDM3NjgzNTEtMGFlNTk3YTIyYjFmODktNTM1NTg2MC00MTA3NzQtMTg1MzAyMDM3NjkzYTMifQ%3D%3D%22%2C%22history_login_id%22%3A%7B%22name%22%3A%22%22%2C%22value%22%3A%22%22%7D%2C%22%24device_id%22%3A%2218530203768351-0ae597a22b1f89-5355860-410774-185302037693a3%22%7D'
    }
    body = json.dumps({
        "hqData": hqdata})
    while True:
        last_r = json.loads(requests.post(url, data=body, headers=headers).text)
        time_tuple = time.localtime(time.time())
        now_time = str(time_tuple[3]) + '.' + str(time_tuple[4]) + '.' + str(time_tuple[5])
        if now_time in end_time:
            break
    res.append([hqdata.split('=')[0] + '=', last_r['message']])
    flag += 1


threads = []
hqdatas = [i for i in open('hqdata.txt').read().split('\n') if i]
print(hqdatas)
for hqdata in hqdatas:
    threads.append(threading.Thread(target=thread_func,kwargs={'hqdata':hqdata}))
target_time = ['23.59.59','9.59.59','14.59.59','19.59.59','12.46.0']
end_time = ['0.0.3','10.0.3','15.0.3','20.0.3','12.46.3']
while True:
    time_tuple = time.localtime(time.time())
    now_time = str(time_tuple[3]) + '.' + str(time_tuple[4]) + '.' + str(time_tuple[5])
    if now_time in target_time:
        for i in threads:
            i.start()
        while True:
            if flag == 10:
                with open('res.csv','w',newline='') as f:
                    f_csv = csv.writer(f)
                    for j in res:
                        f_csv.writerow(j)
                flag = 0
                break

