import requests
import re
html = requests.get('https://www.imdb.com/chart/top').text
html = html.replace('\n','')
from pandas import DataFrame
pattern_1 = '<tbody class="lister-list">(.*?)</tbody>'
ret_1 = re.findall(pattern_1, html)[0]
pattern_2 = '<tr>(.*?)</tr>'
ret_2 = re.findall(pattern_2, ret_1)
ids = []
names = []
years =[]
users = []
ratings = []
for i in ret_2:
    pattern_3 = '<td class="titleColumn"> (.*?)</td>'
    ret_3 = re.findall(pattern_3, i)
    id = re.findall("<a href=(.*?)>",ret_3[0])[0].split('/')[2]
    name = re.findall(">(.*?)</a>",ret_3[0])[0]
    year = re.findall('secondaryInfo">(.*?)</span>',ret_3[0])[0].replace('(','').replace(')','')
    user = re.findall('<strong title="(.*?)">', i)[0].split()[3]
    content = re.findall('<td class="ratingColumn imdbRating">(.*?)</td>', i)[0]
    rating = re.findall('">(.*?)</strong>',content)[0]
    ids.append(id)
    names.append(name)
    years.append(year)
    users.append(user)
    ratings.append(rating)
q3df = DataFrame({'id':ids,'name':names,'year':years,'user':users,'rating':ratings})
print(q3df)
