from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import urllib.request
import zipfile
import requests
import json
import datetime
from webdriver_manager.chrome import ChromeDriverManager



today = datetime.date.today()
given_date = datetime.date(2025, 7, 25)


if today > given_date:
    print('program expired')
    input()
    exit(0)


def download_and_extract_zip(url):
    try:
        file_name = os.path.basename(url)
        print("Downloading {}...".format(file_name))
        urllib.request.urlretrieve(url, file_name)
        print("Download complete!")
        print("Extracting {}...".format(file_name))
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)))
        print("Extraction complete!")
        os.remove(file_name)
    except Exception as e:
        print("An error occurred: ", e)

final_res = []
ini_file = open('FXCM.txt').read().split('\n')
ini_data = [i for i in ini_file if i]
need1 = [ini_data[i] for i in range(ini_data.index('Indices')+1,ini_data.index('Commodities'))]
need2 = [ini_data[i] for i in range(ini_data.index('Commodities')+1,ini_data.index('Forex'))]
need3 = [ini_data[i] for i in range(ini_data.index('Forex')+1,len(ini_data))]
username = ini_data[0].split(':')[1]
password = ini_data[1].split(':')[1]
try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
except Exception as e:
    print(e)
    url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
    response = requests.get(url)
    js_data = json.loads(response.text)
    download_urls = js_data['channels']['Stable']['downloads']['chromedriver']
    for url in download_urls:
        if url['platform'] == 'win64':
            download_url = url['url']
    download_and_extract_zip(download_url)
    driver = webdriver.Chrome('chromedriver-win64/chromedriver.exe')
# 让浏览器打开登录页面
driver.get("https://app.fxcm.com/desktop/login")

WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID,':r3:'))

)

driver.find_element(By.XPATH, '//*[@id="demo-simple-select"]').click()
driver.find_element(By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[4]').click()

# 输入用户名和密码
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/div/div[1]/div[1]/div/div/button[1]').click()
driver.find_element(By.ID,':r3:').send_keys(username)
driver.find_element(By.ID,':r4:').send_keys(password)

# 点击登录按钮
driver.find_element(By.ID,':r5:').click()


WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'css-4fkf23'))
)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[3]/div[2]/div[1]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button'))
)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]'))
)
trlen = len(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')\
    .find_elements(By.TAG_NAME,'tr'))
print(trlen)
for trl in range(1,trlen+1):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[{trl}]/td[11]/span'))
    )
res = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')
Indices_data = [i for i in res.text.split('\n') if i]
Indices_data = [Indices_data[i:i + 6] for i in range(0, len(Indices_data), 6)]
print(res.text)
print(Indices_data)

for d in Indices_data:
    if d[0] in need1:
        final_res.append([d[0]] + d[-1].split()[3:])

driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[1]/button').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[3]/div[2]/div[2]'))
)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[3]/div[2]/div[2]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button'))
)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody'))
)
trlen = len(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')\
    .find_elements(By.TAG_NAME,'tr'))
for trl in range(1,trlen+1):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[{trl}]/td[11]/span'))
    )
res = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')
Commodities_data = [i for i in res.text.split('\n') if i]
Commodities_data = [Commodities_data[i:i + 6] for i in range(0, len(Commodities_data), 6)]
print(res.text)
print(Commodities_data)
res = ''
for d in Commodities_data:
    if d[0] in need2:
        final_res.append([d[0]] + d[-1].split()[3:])

driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[1]/button').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[3]/div[2]/div[3]'))
)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[3]/div[2]/div[3]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button'))
)
driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[1]/div/div/div[2]/div[3]/button').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody'))
)
trlen = len(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')\
    .find_elements(By.TAG_NAME,'tr'))
for trl in range(1,trlen+1):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[{trl}]/td[11]/span'))
    )
res += driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody').text


driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[2]/div/nav/ul/li[4]').click()
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody'))
)
trlen = len(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')\
    .find_elements(By.TAG_NAME,'tr'))

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[1]/td[11]/span'))
)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[2]/div/nav/ul/li[2]').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[2]/div/nav/ul/li[4]').click()

WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody'))
)
trlen = len(driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody')\
    .find_elements(By.TAG_NAME,'tr'))
for trl in range(1,trlen+1):
    WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, f'//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody/tr[{trl}]/td[11]/span'))
    )

res += '\n' + driver.find_element(By.XPATH, '//*[@id="root"]/div/div[3]/section/div[2]/div/div[2]/div/div[1]/div/table/tbody').text

Forex_data = [i for i in res.split('\n') if i]
Forex_data = [Forex_data[i:i + 6] for i in range(0, len(Forex_data), 6)]
print(res)
print(Forex_data)
for d in Forex_data:
    if d[0].replace('/','') in need3:
        final_res.append([d[0]] + d[-1].split()[3:])

for i in final_res:
    print(i)
driver.quit()
import pandas as pd
from datetime import datetime
today = datetime.now()
formatted_today = today.strftime("%Y-%m-%d")
ans = [['Symbol','Rollover (S)','Rollover (B)','Dividend (S)','Dividend (B)','Pip Cost','Entry Margin','Maintenance Margin','Time','Value Date']]
ans += final_res
df11 = pd.DataFrame(ans)

import requests
import json
import pandas as pd


need = [i for i in open('Saxo.txt').read().split('\n') if i]
need = need[1:]
res = {i:[] for i in need}

url = "https://www.home.saxo/en-HK/rnc/hsp"

payload = {'date': formatted_today}

response = requests.request("POST", url, data=payload)
data = json.loads(response.text)['rncHistoricSwapPoints']

all_date = data['filters'][0]['options'][1:]
all_date = [i['value'] for i in all_date]
print(all_date)
for date in all_date:
    print(date)
    payload = {'date': date}
    response = requests.request("POST", url, data=payload)
    body = json.loads(response.text)['rncHistoricSwapPoints']['tableData']['body']
    for item in body:
        cell = [i['name'] for i in item['cells']]
        if cell[0] in res and not res[cell[0]]:
            res[cell[0]] = cell[1:]
    flag = 1
    for key in res:
        if not res[key]:
            flag = 0
            break
    if flag:
        break

ans = [['Forex cross','From','To','Long positions','Short positions']]
for key in need:
    ans.append([key] + res[key])
df = pd.DataFrame(ans)

df.columns = df.iloc[0]
df = df.iloc[1:]
df11.columns = df11.iloc[0]
df11 = df11.iloc[1:]
with pd.ExcelWriter(f'swap_{formatted_today}.xlsx', engine='openpyxl', mode='w') as writer:
    df.apply(pd.to_numeric, errors='ignore').to_excel(writer, sheet_name='SAXO',index=False,header=True)
    df11.apply(pd.to_numeric, errors='ignore').to_excel(writer, sheet_name='FXCM',index=False,header=True)

