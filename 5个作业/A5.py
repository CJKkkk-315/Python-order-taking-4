import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
response = requests.get('https://www.peakbagger.com/list.aspx?lid=5651')
soup = BeautifulSoup(response.text)
t = 0
names = []
regions = []
elevs = []
ids = []
lats = []
longs = []
domain = 'https://www.peakbagger.com/'
for tr in soup.find(class_='gray').find_all(name='tr'):
    t += 1
    if t <= 2:
        continue
    names.append(tr.find_all(name='td')[1].text)
    regions.append(tr.find_all(name='td')[2].text)
    elevs.append(int(tr.find_all(name='td')[3].text))
    href = tr.find_all(name='td')[1].find(name='a')['href']
    ids.append(href.split('=')[1])
    url = domain + href
    response = requests.get(url)
    sub_soup = BeautifulSoup(response.text)
    for content in sub_soup.find(class_='gray').find_all(name='tr'):
        if 'Latitude/Longitude' in content.text:
            lat,long = str(content).split('<br/>')[1].replace(' (Dec Deg)','').split(', ')
            break
    lats.append(lat)
    longs.append(long)
q5df = {'name':names,'region':regions,'elev':elevs,'id':ids,'lat':lats,'long':longs}
q5df = DataFrame(q5df)
print(q5df.loc[(q5df['elev'] >= 2000) & (q5df['elev'] <= 2500) & (q5df['region'] == 'Kanto')])
q5df.to_csv('Q5_mountains.csv',index=False)
