import requests
from bs4 import BeautifulSoup
from pandas import DataFrame
response = requests.get('https://realpython.github.io/fake-jobs/')
soup = BeautifulSoup(response.text)
q4df = {'position':[],'company':[],'city':[],'state':[]}
for item in soup.find_all(class_='is-half'):
    position = item.find(class_='is-5').text
    company = item.find(class_='company').text
    city = item.find(class_='location').text.split(',')[0]
    state = item.find(class_='location').text.split(',')[1]
    q4df['position'].append(position)
    q4df['company'].append(company)
    q4df['city'].append(city)
    q4df['state'].append(state.replace('\n','').replace(' ',''))
q4df = DataFrame(q4df)
print(q4df[(q4df['state'].isin(['AA'])) & (q4df['position'].str.contains('engineer|Engineer'))])
