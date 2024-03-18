import requests
import os
import json
import xlrd2
import warnings
warnings.filterwarnings('ignore')
ress = []
dataset = [i for i in os.listdir() if i.split('.')[-1] == 'xlsx'][0]
data = []
du_set = set()
wb = xlrd2.open_workbook(dataset)
sh = wb.sheet_by_name('Sheet1')
for i in range(sh.nrows):
    row = sh.row_values(i)
    data.append(row)
    du_set.add(row[0])
key_words = data[::]
flagaa = 0
xcs = 10
xwords = [[] for _ in range(xcs)]
for i in range(len(key_words)):
    xwords[i%xcs].append(key_words[i])
import threading

# 创建一个 Condition 对象
condition = threading.Condition()

# 创建一个全局变量
flag = 0
all_flag = 0
def my_function(thread_name,key_words):
    global flag, all_flag
    for xxword in key_words:

        try:
            word = str(xxword[0])
            url = "https://www.tmdn.org/tmview/api/search/results"

            payload = "{\"page\":\"1\",\"pageSize\":\"1\",\"criteria\":\"I\",\"basicSearch\":\"" + word + "\",\"fOffices\":[\"US\",\"CA\",\"MX\"],\"fTMStatus\":[\"Registered\"],\"newPage\":true,\"fields\":[\"ST13\",\"markImageURI\",\"tmName\",\"tmOffice\",\"applicationNumber\",\"applicationDate\",\"tradeMarkStatus\",\"niceClass\"]}"
            headers = {
                'Accept': 'application/json',
                'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
                'Connection': 'keep-alive',
                'Content-Type': 'application/json; charset=utf-8',
                'Origin': 'https://www.tmdn.org',
                'Referer': 'https://www.tmdn.org/tmview/welcome',
                'Sec-Fetch-Dest': 'empty',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Site': 'same-origin',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.43',
                'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"'
            }

            response = requests.request("POST", url, verify=False, headers=headers, data=payload)
            try:
                dd = json.loads(response.text)
                if dd['totalResults']:
                    ress.append(xxword + [0])
                    print(xxword + [0])
                else:
                    ress.append(xxword + [1])
                    print(xxword + [1])
            except:
                ress.append(xxword + [-1])
                if 'Please enable JavaScript to view the page content.' in response.text:
                    flag = 1
                else:
                    print(xxword, response.text)
        except Exception as ex:
            ress.append(xxword + [-1])
            print(ex)
            print(xxword, 'failed')
        with condition:
            while flag == 1:
                print(f'{thread_name} 暂停执行')
                all_flag += 1
                condition.wait()  # 这会让当前线程暂停，并释放锁



def main():
    global flag, all_flag
    threads = []

    # 创建 10 个线程
    for i in range(10):
        thread = threading.Thread(target=my_function, args=(f'线程{i}',xwords[i]))
        thread.start()
        threads.append(thread)

    while True:
        # 检查所有线程是否都已经结束
        if not any(thread.is_alive() for thread in threads):
            print("所有线程都已结束")
            break

        # 等待用户输入，如果输入的是 'q'，则跳出循环
        if flag:
            while True:
                if all_flag == 10:
                    user_input = input('按下回车键来唤醒所有线程\n')
                    all_flag = 0
                    break

        # 将 flag 设为 0 并唤醒所有线程
        with condition:
            flag = 0
            condition.notify_all()

    # 等待所有线程执行完毕
    for thread in threads:
        thread.join()

    import csv
    with open('res2.csv', 'w', newline='', encoding='utf8') as f:
        f_csv = csv.writer(f)
        for i in ress:
            try:
                f_csv.writerow(i)
            except:
                f_csv.writerow(i[:-1] + [''])


main()



