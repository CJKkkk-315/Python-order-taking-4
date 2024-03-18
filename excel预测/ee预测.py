import os
import pandas as pd
import warnings
from sklearn.linear_model import LinearRegression
warnings.filterwarnings('ignore')
# 找到当前目录下唯一的xlsx文件
file = [f for f in os.listdir() if f.endswith('.xlsx') and not f.startswith('~$')][0]

# 使用pandas读取xlsx文件
df = pd.read_excel(file, usecols="B:E")


# 使用BCD列作为特征，E列作为目标
X = df.iloc[:, 0:3]  # Features: B, C, D columns
y = df.iloc[:, 3]    # Target: E column

# 构建一个F特征，每一行的F特征即为上一行的E，第一行就为本行的E
df['F'] = df.iloc[:, 3].shift(1)
df.loc[0, 'F'] = df.iloc[0, 3]

# 将新的F列添加到特征中
X['F'] = df['F']

# 分割数据集为训练集和测试集
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 使用线性回归进行训练
regressor = LinearRegression()
regressor.fit(X, y)
print(regressor.coef_)
while True:
    a,b,c,d = [float(i) for i in input('承贴比	交易金额（亿元）	6M同业存单利率（AAA）（%）	6M国股利率（%）').split()]
    res = regressor.predict([[a,b,c,d]])
    print(res[0])
