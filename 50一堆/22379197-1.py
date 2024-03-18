import matplotlib.pyplot as plt
years = ['2019','2020','2021','2022']
distance = [357.70,242.85,403.35,451.30]
plt.bar(years,distance)
plt.xlabel('Year')
plt.ylabel('Distance(m)')
plt.title('Yutu rover')
for i, j in zip(years,distance):
    plt.text(i,j,j)
#保存图
plt.savefig('22379197-1.png')

#显示统计图
plt.show()
