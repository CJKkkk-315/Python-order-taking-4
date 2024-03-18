from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
import numpy as np
import datetime

train_data = 'spam_train.txt'
test_data = 'spam_test.txt'
vectoring = TfidfVectorizer(input='content', tokenizer=lambda line: [li for li in line.split() if li],analyzer='word')
content = open(train_data, 'r', encoding='utf8').read().split('\n')[:5000]
x_train = [' '.join(i.split()[1:]) for i in content]
y_train = [int(i.split()[0]) for i in content]
content = open(test_data, 'r', encoding='utf8').read().split('\n')[:500]
x_test = [' '.join(i.split()[1:]) for i in content]
y_test = [int(i.split()[0]) for i in content]
X = x_train + x_test
X = vectoring.fit_transform(X)
x_train,x_test = X[:5000],X[5000:5500]

y_train, y_test = np.array(y_train), np.array(y_test)
y = np.r_[y_train, y_test]
print('先验概率:',len(y[y == 0])/len(y))
startTime = datetime.datetime.now()
bayes = MultinomialNB()
bayes.fit(x_train, y_train)
y_pred = bayes.predict(x_test)
y_pro = bayes.predict_proba(x_test)
# print('先验概率:',y_pro[:,0])
print('朴素贝叶斯准确度:', metrics.accuracy_score(y_test, y_pred))
endTime = datetime.datetime.now()
durTime = 'funtion time use:%dms' % ((endTime -startTime ).seconds * 1000 + (endTime -startTime ).microseconds / 1000)
print('朴素贝叶斯用时:', durTime)
