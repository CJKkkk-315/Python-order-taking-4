import pandas as pd
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

# 获取所有的sheet名字
xls = pd.ExcelFile('人口数据.xlsx')
sheet_names = xls.sheet_names

# 读取并拼接所有的sheet
df = pd.concat(pd.read_excel('人口数据.xlsx', sheet_name=None), ignore_index=True)

# 计算人均GDP
df['人均gdp'] = df['gdp(万元)'] / df['人口'] * 10000 # 转换为人均GDP(元)

# 根据人均GDP划分发展地区
df['发展地区'] = pd.cut(df['人均gdp'], bins=[0, 50000, 100000, float('inf')], labels=['低发展地区', '中发展地区', '高发展地区'], right=False)
df['占地面积'] = df['占地面积'].apply(lambda x:float(x.split('平')[0]))
# 打印处理后的数据

model = GaussianNB()
X = df.drop(['地区','发展地区'],axis=1)
y = df['发展地区']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(X_train, y_train)
score = model.score(X_test, y_test)
print(score)
y_pred = model.predict(X)
df_pred = pd.DataFrame({'地区': df['地区'], '预测发展地区': y_pred})
for area in df_pred['预测发展地区'].unique():
    print(area + ' 包括以下地区:')
    print(df_pred[df_pred['预测发展地区'] == area]['地区'])
import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 读取所有的sheet并拼接到一个df里
xls = pd.ExcelFile('人口数据.xlsx')
df_list = []
for sheet_name in xls.sheet_names:
    df_temp = pd.read_excel('人口数据.xlsx', sheet_name=sheet_name)
    df_temp['城市'] = df_temp.values[0,0]  # 添加城市列
    df_temp = df_temp.drop([0])
    df_list.append(df_temp)
    # print(df_temp)
df = pd.concat(df_list, ignore_index=True)

# 计算人均GDP
df['人均gdp'] = df['gdp(万元)'] / df['人口'] * 10000

# 根据人均GDP划分发展地区
df['发展地区'] = pd.cut(df['人均gdp'], bins=[0, 50000, 100000, float('inf')],
                        labels=['低发展地区', '中发展地区', '高发展地区'], right=False)

# 遍历所有城市，为每个城市绘制图表
for city in df['城市'].unique():
    df_city = df[df['城市'] == city]

    # 绘制人均GDP柱状图
    plt.figure(figsize=(10, 5))
    sns.barplot(x=df_city['地区'], y=df_city['人均gdp'])
    plt.title(city + '人均GDP')
    plt.show()

    # 绘制发展地区饼图
    plt.figure(figsize=(5, 5))
    df_city['发展地区'].value_counts().plot(kind='pie', autopct='%1.1f%%')
    plt.title(city + '发展地区占比')
    plt.show()


