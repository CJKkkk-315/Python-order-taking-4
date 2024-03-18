import os
import urllib.request
import zipfile
import requests
import json

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
        urllib.request.urlretrieve(url, file_name)
        print("Download complete!")
        print("Extracting {}...".format(file_name))
        with zipfile.ZipFile(file_name, 'r') as zip_ref:
            zip_ref.extractall(os.path.dirname(os.path.abspath(__file__)))
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