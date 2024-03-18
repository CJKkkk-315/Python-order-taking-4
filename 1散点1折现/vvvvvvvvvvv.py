import matplotlib.pyplot as plt
data = [i.split(',') for i in open('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_5358347.csv',encoding='UTF8').read().split('\n') if i]
res = []
x = [i.replace('"','') for i in data[2][-13:] if i]
data = data[4:]

for i in data:
    if 'africa' in i[0].lower():
        row = []
        for j in i[-13:-1]:
            if j != '""' and j != '':
                row.append(float(j.replace('"','')))
            else:
                row.append(0)
        res.append([i[0],row])
for i in res:
    plt.plot(x,i[1],label=i[0])
plt.xticks(rotation=45)
plt.ylabel('CO2 concentration')
plt.legend()
plt.show()



x = []
y = []
gh = [i.split(',') for i in open('Greenhouse_Gas.csv',encoding='UTF8').read().split('\n') if i][1:]
for i in gh:
    print([j for j in i[-11:]])
for i in gh:
    if i[1] == 'Advanced Economies' or i[1] == 'Emerging and Developing Economies':
        y.append(i[1])
        x.append(sum([float(j) for j in i[-11:]]))
plt.scatter(x,y)
plt.show()

