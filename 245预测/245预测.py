import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import csv
df = pd.read_csv('global_hist.csv')
date = df['global_date']
date = [i for i in date.apply(lambda x:x.split('.')).values]
year = []
mouth = []
day = []
for i in date:
    year.append(int(i[0]))
    mouth.append(int(i[1]))
    day.append(int(i[2]))
df['day'] = day
df['mouth'] = mouth
df['year'] = year
certain = df['certain']
uncertain = df['uncertain']
die = df['die']
X = df.drop(['global_date','certain','uncertain','die','updatetime'],axis=1)
RF = RandomForestRegressor()
RF.fit(X,certain)
y_certain = RF.predict(X)
RF = RandomForestRegressor()
RF.fit(X,uncertain)
y_uncertain = RF.predict(X)
RF = RandomForestRegressor()
RF.fit(X,die)
y_die = RF.predict(X)
head = ['certain','uncertain','die']
with open('res.csv','w',newline='') as f:
    f_csv = csv.writer(f)
    f_csv.writerow(head)
    for i,j,k in zip(y_certain,y_uncertain,y_die):
        f_csv.writerow([int(i),int(j),int(k)])
