# 引入相关库
import pandas as pd
from collections import Counter
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei']
# 读取数据集
df = pd.read_csv('HCV-Egy-Data.csv')
# 读取性别占比
gender = Counter(df['Gender'].values.tolist())
# 饼图可视化
plt.pie(x=[gender[1],gender[2]],labels=['男','女'])
plt.show()

# 读取年龄占比
age = Counter(df['Age '].values.tolist())
x = [i for i in age.keys()]
y = [i for i in age.values()]
# 柱状图可视化
plt.bar(x,y)
plt.show()

# 读取BMI
age = Counter(df['BMI'].values.tolist())
x = [i for i in age.keys()]
y = [i for i in age.values()]
# 柱状图可视化
plt.bar(x,y)
plt.show()

# 计算不同症状出现次数
d = ['Fever','Nausea/Vomting','Headache','Diarrhea','Fatigue & generalized bone ache ','Jaundice ','Epigastric pain ']
r = [0 for _ in range(len(d))]
# 统计不同症状
for i in df.values:
    for j in range(3,10):
        r[j-3] += i[j] % 2
# 柱状图可视化
plt.bar(d,r)
plt.ylim(600,700)
plt.show()

# 将Epigastric pain作为y待预测，其余列作为X
X = df.drop(['Epigastric pain '],axis=1)
y = df['Epigastric pain ']
# 以8比2分割训练集和测试集
xtrain, xtest, ytrain, ytest = train_test_split(X, y, test_size=0.2)
# 构建决策树模型
DT = DecisionTreeClassifier()
# 训练模型
DT.fit(xtrain,ytrain)
# 预测测试集
ypre = DT.predict(xtest)
# 输出准确率
acc = accuracy_score(ytest,ypre)
print(acc)
