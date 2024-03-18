import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

username = input('账号：')
password = input('密码：')
start_page = int(input('起始页码：'))
end_page = int(input('结束页码：'))
def get_time():
    from datetime import datetime, timedelta
    current_time = datetime.now()
    time_after_7_days = current_time + timedelta(days=7)
    current_time_str = current_time.strftime("%Y-%m-%d %H:%M:%S")
    time_after_7_days_str = time_after_7_days.strftime("%Y-%m-%d %H:%M:%S")
    return current_time_str, time_after_7_days_str


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
url = "https://partner.zmlearn.com/api/zmbiz-sale-crm/seller/searchSeller4Dispatch?lang=zh-CN&zone=480"
payload = "{\"dispatchSelId\":0,\"keyWord\":\"\",\"reason\":\"分配名单\",\"stuIds\":[]}"
response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))
select_base = json.loads(response.text)
select_lists = [(i['sellerName'] + '(' + i['mobile'][-4:] + ')', i['id']) for i in select_base['data']]
print('所有库如下：')
for i in range(len(select_lists)):
    print(i+1,select_lists[i][0])
A = int(input('请输入有价值库:'))
B = int(input('请输入无价值库:'))
useful_id = select_lists[A-1][1]
useless_id = select_lists[B-1][1]
while True:
    try:
        for pageless in range(start_page, end_page+1):
            page = 1
            url = "https://partner.zmlearn.com/api/student-tag/student/queryForPage"

            payload = '{' + f'\"sellerId\":"{sellerId}",\"teamId\":"{teamId}",\"districtId\":"{districtId}",\"stuMobile\":\"\",\"sortField\":\"responseTime\",\"sortType\":\"desc\",\"pageNo\":{page},\"pageSize\":50,\"state\":\"\",\"tmkRemoveList\":false,\"isImport\":false,\"isTodayTodo\":false,\"studentName\":\"\",\"is7DaysUnContacted\":false,\"is14DaysUnTranslated\":false,\"is14DaysUnTranslatedFinished\":false,\"isPlanTodayFinished\":false,\"isTrialType\":false,\"todoNameList\":[],\"accountNumber\":\"\",\"tagIds\":[],\"recordedClassTagId\":\"\",\"buId\":102,\"positionCode\":\"CR_LEADER\"' + '}'

            response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'), timeout=10)
            slist = json.loads(response.text)['data']['list']
            all_info = []
            for s in slist:

                if s['provice'] in ['上海','北京','江苏','浙江','广东']:
                    all_info.append([s['studentId'], s['studentName'], 1])
                else:
                    all_info.append([s['studentId'], s['studentName'], 0])
            useful = []
            useless = []
            comment = '通过群呼激活'
            t_now, t_seven = get_time()
            for info in all_info:
                sid = info[0]
                name = info[1]

                if info[2]:
                    url = "https://partner.zmlearn.com/api/zmbiz-sale-comment/access/saveAccess"
                    payload = '{"returnTime":"' + t_now + '","returnWay":"1001","returnResult":"已接通","relateNumber":"*******1292-本人","nextReturnWay":"1001","freeTime":"' + t_seven + '","stuId":' + str(sid) + ',"context":"' + comment + '","warnFlage":true,"version":"3.0","groupId":"","extraData":{},"tagIds":[10],"tagNames":["常规回访"],"tmkFollowInfo":null}'
                    response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'), timeout=10)
                    print('添加成功', name)
                    useful.append(str(sid))
                else:
                    print('无价值', name)
                    useless.append(str(sid))

            url = "https://partner.zmlearn.com/api/zmbiz-sale-crm/student/batchDispatch"
            payload = "{" + f"\"dispatchSelId\":\"{useful_id}\",\"reason\":\"分配名单\",\"stuIds\":[{','.join(useful)}]" + "}"
            response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'), timeout=10)
            print(response.text)

            url = "https://partner.zmlearn.com/api/zmbiz-sale-crm/student/batchDispatch"
            payload = "{" + f"\"dispatchSelId\":\"{useless_id}\",\"reason\":\"分配名单\",\"stuIds\":[{','.join(useless)}]" + "}"
            response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'), timeout=10)
            print(response.text)
            time.sleep(10)
    except:
        print('网络错误，重新运行')
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
        time.sleep(5)

