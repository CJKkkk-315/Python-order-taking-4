import matplotlib.pyplot as plt
import datetime
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
alltime = 360
data = open('data2.txt').read().split('\n')
non = []
res = []
for i in data:
    if '误码率' in i:
        l = float(i.split('误码率：')[1])
        if l != 0:
            if l not in non:
                non.append(l)
                res.append(datetime.datetime.strptime(i.split('时间：')[1].split()[0],"%H时%M分%S秒"))
# print(res)
non = len(non)
x = [alltime-non,non]
plt.pie(labels=[f'非误码持续时间({alltime-non})',f'误码持续时间({non})'],x=x,labeldistance=0.1)
plt.title('无信道编码系统')
plt.show()

x = [alltime]
plt.pie(labels=[f'非误码持续时间({alltime})'],x=x,labeldistance=0.1)
plt.title('10M业务速率系统')
plt.show()

x = [i for i in res]
de = int(-(x[0] - x[-1]).total_seconds())
# print(de)
sr = []
xx = []
yy = []
for i in range(de):
    if x[0] + datetime.timedelta(seconds=i) in x:
        xx.append(str(i))
        yy.append(1)
    else:
        xx.append(str(i))
        yy.append(-1)

xxx = [int(i) for i,j in zip(xx,yy) if j != -1]
rres = []
rr = [xxx[0]]
# print(xxx)
for i in range(1,len(xxx)):
    if xxx[i] == xxx[i-1] + 1:
        rr.append(xxx[i])
    else:
        rres.append(rr)
        rr = [xxx[i]]
rres.append(rr)
rres = [i for i in rres if i]
# print(rres)
for i in rres:
    if len(i) == 1:
        plt.plot([i[0]],[1],marker='*',color='red')
    else:
        plt.plot([i[0],i[-1]], [1,1],marker='*',linestyle='--',color='red')

plt.ylim(0,2)
plt.xticks([i for i in range(de)],[str(i) for i in range(de)],rotation=60)
# plt.show()