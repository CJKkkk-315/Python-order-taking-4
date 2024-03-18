import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# username = input('账号：')
# password = input('密码：')
username = '19072084389'
password = 'hello4389'

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

url = "https://partner.zmlearn.com/api/zmbiz-sale-crm/seller/searchSeller4Dispatch?lang=zh-CN&zone=480"
payload = "{\"dispatchSelId\":0,\"keyWord\":\"\",\"reason\":\"分配名单\",\"stuIds\":[]}"
response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))
print(response.text)

import requests

url = "https://partner.zmlearn.com/api/zmbiz-sale-crm/student/batchDispatch"

payload = "{\"dispatchSelId\":\"179610\",\"reason\":\"分配名单\",\"stuIds\":[34598689]}"

response = requests.request("POST", url, headers=headers, data=payload.encode('utf8'))

print(response.text)
