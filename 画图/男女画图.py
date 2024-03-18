import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('census2000.csv')
man = [0,0]
woman = [0,0]
data = df.values.tolist()
for i in data:
    if i[0] == 'M':
        if i[1] == 1900:
            man[0] += i[-1]
        else:
            man[1] += i[-1]
    else:
        if i[1] == 1900:
            woman[0] += i[-1]
        else:
            woman[1] += i[-1]
plt.figure(figsize=(6, 6))
plt.plot(['1900','2000'],man,'r',marker='o',label='M')
plt.plot(['1900','2000'],woman,'b',marker='o',label='F')
plt.ylim(min(man)/2,max(man)*1.2)
plt.title('Man vs. Woman')
plt.xlabel('Year')
plt.ylabel('People')
plt.legend()
plt.show()