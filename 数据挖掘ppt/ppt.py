import pandas as pd
import random
sex = ['男','女']
city = ['北京','上海','广州','杭州','深圳','武汉','福州','重庆','成都','苏州','南京','长沙','西安','郑州']
data = {'性别':[],'年龄':[],'城市':[],'浏览次数':[],'是否购买':[]}
for i in range(1000):
    data['性别'].append(sex[random.randint(0,1)])
    data['城市'].append(random.sample(city,1)[0])
    data['年龄'].append(random.randint(18,50))
    data['浏览次数'].append(random.randint(10,1000))
    if random.random() > 0.9:
        data['是否购买'].append(1)
    else:
        data['是否购买'].append(0)
df = pd.DataFrame(data)
print(df)