import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
name_hash = {int(i.split('—')[0]):i.split('—')[1] for i in """1—北京邮电大学
2—北京大学
3—北京科技大学
4—北京师范大学
5—北京理工大学
6—北京林业大学
7—北京航空航天大学
8—北京中医药大学
9—北京交通大学
10—北京联合大学""".split('\n')}
location = pd.read_excel('各高校坐标.xlsx')
location = location.values[:,1:]
res = [8,0,3,7,9,2,6,5,1,4,8]
route_x = [location[i][0] for i in res]
route_y = [location[i][1] for i in res]
for x,y,t in zip(route_x, route_y, res):
    plt.text(x,y,name_hash[t+1])
plt.scatter(route_x, route_y, s=10, c='k')
plt.plot(route_x, route_y, 'r-')
plt.show()