import requests
requests.packages.urllib3.disable_warnings()
from bs4 import BeautifulSoup
from pandas import DataFrame
response = requests.get('https://www.fbe.hku.hk/msba/about-us/our-faculty',verify=False)
soup = BeautifulSoup(response.text)
names = []
universitys = []
countrys = []
urls = []
domain = 'https://fbeo.fbe.hku.hk/'
for row in soup.find_all(class_='rte-tpl'):
    for item in row.find_all(class_='cke-list-block'):
        name = ''.join(str(item.find(class_='flexible-row-col__title').text.replace('\n','').replace('"','')).split())
        names.append(name)
        universitys.append(''.join(str(item.find(class_='flexible-row-col__txt').text).split()).split(',')[1])
        countrys.append(''.join(str(item.find(class_='flexible-row-col__txt').text).split()).split(',')[2])
        url = domain + item.find(name='img')['src']
        urls.append(url)
        ext = url.split('.')[-1]
        r = requests.get(url,verify=False)
        with open('images/'+name+'.'+ext, 'wb') as handle:
            handle.write(r.content)
q6df = DataFrame({'name':names,'university':universitys,'country':countrys,'url':urls})
q6df.to_csv('Q6_teachers.csv',index=False)