import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from sklearn.metrics import accuracy_score
df = pd.read_csv('March 7-April 10, 2018 - Teens and Tech Survey - CSV.csv')
age = df['AGE']
gender = df['GENDER']
gender = gender[gender != 99]
city = df['RACETHNICITY']
age_dict = Counter(age).most_common()
age_dict.sort()
plt.bar([i[0] for i in age_dict],[i[1] for i in age_dict])
plt.show()


gender_dict = Counter(gender).most_common()
plt.pie([i[1] for i in gender_dict],labels=[i[0] for i in gender_dict])
plt.show()

city_dict = Counter(city).most_common()
city_dict.sort()
plt.bar([str(i[0]) for i in city_dict],[i[1] for i in city_dict])
plt.show()
