import pandas as pd
import os
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
pdvi = pd.read_excel('PDVI.xlsx',skiprows=1)
ev = {}
for i in pdvi.values:
    ev[(i[0], i[1])] = i[2]
files = os.listdir('data')
for file in files:
    if file[0] == '~':
        continue
    ename = file.split()[0]
    data = pd.read_excel('data/' + file)
    data['Date & Time'] = data['Date & Time'].astype('str')
    data['Date & Time'] = data['Date & Time'].str.split(' ', 1).str[0]
    data['Date & Time'] = pd.to_datetime(data['Date & Time'])
    data = data.sort_values(by='Date & Time')
    print(data)