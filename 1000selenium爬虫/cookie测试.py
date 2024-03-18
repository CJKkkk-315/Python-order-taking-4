from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import zipfile
import requests
import json
import csv
from datetime import datetime, timedelta
import shutil
def delete_file(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print(f'文件 {filename} 已删除。')
    else:
        print(f'未找到文件 {filename}。')

delete_file("chromedriver.exe")

def download_and_extract_zip(url):
    try:
        file_name = os.path.basename(url)
        print("Downloading {}...".format(file_name))
        res = requests.get(url)
        with open(file_name,'wb') as f:
            f.write(res.content)
        print("Download complete!")
        print("Extracting {}...".format(file_name))
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(file_name.split('.')[0])
        print("Extraction complete!")
        os.remove(file_name)
    except Exception as e:
        print("An error occurred: ", e)
url = "https://googlechromelabs.github.io/chrome-for-testing/last-known-good-versions-with-downloads.json"
response = requests.get(url)
js_data = json.loads(response.text)
download_urls = js_data['channels']['Stable']['downloads']['chromedriver']
for url in download_urls:
    if url['platform'] == 'win64':
        download_url = url['url']
download_and_extract_zip(download_url)




def copy_and_delete_folder(folder_name):
    if os.path.exists(folder_name):
        for filename in os.listdir(folder_name):
            shutil.copy(os.path.join(folder_name, filename), '.')
        shutil.rmtree(folder_name)
        print(f'文件夹 {folder_name} 中的文件已复制并删除该文件夹。')
    else:
        print(f'未找到文件夹 {folder_name}。')

copy_and_delete_folder("chromedriver-win64/chromedriver-win64")
shutil.rmtree('chromedriver-win64')
driver = webdriver.Chrome('chromedriver.exe')

# 导航到已经登录的页面
driver.get("https://terminus.isprimefx.com/dashboard")
driver.find_element(By.XPATH,'//*[@id="username"]').send_keys('frankywong@emperorgroup.com')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[2]/input').send_keys('garageheadlineswing')
driver.find_element(By.XPATH,'//*[@id="loginForm"]/div[3]/div[2]/button').click()
# 获取当前浏览器中的所有Cookie
cookies = driver.get_cookies()

# 打印Cookie信息
cookie = cookies[0]['value']

# 关闭浏览器
driver.quit()

url = "https://terminus.isprimefx.com/json/tomnextrates"

payload = {}
headers = {
  'Cookie': 'SENTRY_SESS_ID=' + cookie
}

response = requests.request("GET", url, headers=headers, data=payload)
head = 'Currency Pair,Quote Date,Near Value Date,Far Value Date,Bid Price,Ask Price'.split(',')
print(response.text)
data = json.loads(response.text)
res = []
for i in data['data']:
    res.append([i['fxPair'],i['quoteDt'],i['nearDt'],i['farDt'],f'{i["shortRate"]:.6f}',f'{i["longRate"]:.6f}'])
for i in res:
    print(i)


current_time = str(datetime.now())
year = current_time.split('-')[0]
mouth = current_time.split('-')[1]
day = current_time.split('-')[2].split()[0]
hour = current_time.split('-')[2].split()[1].split(':')[0]
mi = current_time.split('-')[2].split()[1].split(':')[1]
with open(f'Current_Tom Next Rates_{year+mouth+day}_{hour+mi}.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerows(res)

today = datetime.now() + timedelta(days=1)
seven_days_later = today + timedelta(days=7)
today_formatted = today.strftime('%Y-%m-%d')
seven_days_later_formatted = seven_days_later.strftime('%Y-%m-%d')
url = f'https://terminus.isprimefx.com/json/dividends?fromDate={today_formatted}&toDate={seven_days_later_formatted}'

response = requests.request("GET", url, headers=headers, data=payload)
head = 'Currency Pair,Quote Date,Near Value Date,Far Value Date,Bid Price,Ask Price'.split(',')
print(response.text)
data = json.loads(response.text)
res = []
for i in data['data']:
    res.append([i['instrument'],i['symbol'],i['exDividendDt'],f'{i["dividend"]:.6f}'])
res.sort(key=lambda x:x[2])
head = 'Instrument,Symbol,Ex Dividend Date,Dividend'.split(',')
with open(f'Projected_Dividends_{year+mouth+day}_{hour+mi}.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    f_csv.writerows(res)