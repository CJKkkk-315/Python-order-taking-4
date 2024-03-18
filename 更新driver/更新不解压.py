import os
import shutil
import urllib.request
import zipfile
import requests
import json
# 获取脚本所在的目录

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
