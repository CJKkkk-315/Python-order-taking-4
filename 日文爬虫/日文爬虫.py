import requests
from bs4 import BeautifulSoup
for y in range(1,1000):
    res = requests.get(f'https://www.jigsaw.jp/shop/c/c1003_p{y}/')
    soup = BeautifulSoup(res.text)
    for line in soup.find(class_='StyleP_Frame_').find_all(class_='StyleP_Line_'):
        for item in line.find_all(class_='StyleP_Item_'):
            print(item.find(class_='goods_name_')['href'])