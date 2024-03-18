import csv
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime, timedelta
import traceback


username = input('请输入账号：')
password = input('请输入密码：')
sleep_time = float(input('请输入每条数据间隔秒数：'))
day_time = input('请输入日期(2024-03-01)：')



driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get('https://partner.zmlearn.com/#/login')
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div[1]/input'))
)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[1]/div/div[1]/input').send_keys(username)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[3]/div/div[1]/input').send_keys(password)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/form/div[5]/div/button[1]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/ul/div[2]/a'))
)
driver.find_element(by=By.XPATH, value='//*[@id="app"]/div/ul/div[2]/a').click()
cookies = driver.get_cookies()
acw_tc = cookies[1]['value']
driver.quit()
PARTNER_TOKEN = cookies[0]['value']
headers = {
      'Cookie': f'acw_tc={acw_tc}; PARTNER_TOKEN={PARTNER_TOKEN};',
      'Content-Type': 'application/json;charset=UTF-8',
      'Connection': 'close'
    }

url = "https://partner.zmlearn.com/api/seller/seller/getSeller"

payload = {}

response = requests.request("GET", url, headers=headers, data=payload)
seller = json.loads(response.text)
districtId = seller['data']['districtId']
teamId = seller['data']['teamId']
sellerId = seller['data']['sellerId']
page = 1
flag = 1
start_flag = 0
res = []
while flag:
    try:
        url = "https://partner.zmlearn.com/api/student-tag/student/queryForPage"

        payload = '{' + f'\"sellerId\":"{sellerId}",\"teamId\":"{teamId}",\"districtId\":"{districtId}",\"stuMobile\":\"\",\"sortField\":\"responseTime\",\"sortType\":\"desc\",\"pageNo\":{page},\"pageSize\":50,\"state\":\"\",\"tmkRemoveList\":false,\"isImport\":false,\"isTodayTodo\":false,\"studentName\":\"\",\"is7DaysUnContacted\":false,\"is14DaysUnTranslated\":false,\"is14DaysUnTranslatedFinished\":false,\"isPlanTodayFinished\":false,\"isTrialType\":false,\"todoNameList\":[],\"accountNumber\":\"\",\"tagIds\":[],\"recordedClassTagId\":\"\",\"buId\":102,\"positionCode\":\"CR_LEADER\"' + '}'

        response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'), timeout=10)
        slist = json.loads(response.text)['data']['list']
        for s in slist:
            try:
                print(s['responseTime'])
                if s['responseTime'].split()[0] < day_time:
                    flag = 0
                    break
                # formatted_date = '2024-02-29'

                if start_flag == 0 and s['responseTime'].split()[0] == day_time:
                    start_flag = 1
                elif start_flag == 1 and s['responseTime'].split()[0] != day_time:
                    start_flag = 0
                    flag = 0
                    break
                if start_flag == 0:
                    continue
                sid = s['studentId']
                skey = s['stuKey']
                sname = s['studentName']
                sgrade = s['grade']
                sprovice = s['provice']
                scity = s['city']
                phone_url = f'https://partner.zmlearn.com/api/student/getMobile?stuKey={skey}&stuId={sid}&type=1&&lang=zh-CN&zone=480'
                sphone_response = requests.request("GET",phone_url,headers=headers).text
                print(sphone_response)
                sphone = json.loads(sphone_response)['data']['mobile']

                payload = '{' + f'\"pageNo\":1,\"pageSize\":15,\"stuKey\":"{skey}"' + '}'
                gj_url = 'https://partner.zmlearn.com/api/zmbiz-sale-comment/todo/queryCommentHistory/V3?lang=zh-CN&zone=480'
                response = requests.request("POST", gj_url, headers=headers, data=payload.encode('utf8'))
                gj_detials = json.loads(response.text)['data']['list']
                gj_content = ''
                for i in gj_detials:
                    gj_content += i['createdAt'] + '\n' + i['commentBody'] + '\n'
                row = [sname, sphone, sgrade, sprovice, scity, gj_content]
                res.append(row)
                time.sleep(sleep_time)
            except:
                pass

        page += 1
    except Exception as e:
        error_message = f"发生异常：{str(e)}\n"
        error_message += traceback.format_exc()
        with open('error_log.txt', 'a+') as file:
            file.write(datetime.now().strftime("%Y-%m-%d") + '\n' + username + '\n' + password + '\n' + day_time.strftime("%Y-%m-%d") + '\n' + error_message + '\n')
        print(error_message)
        break

with open('res.csv', 'w', newline='', encoding='utf8') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(res)




