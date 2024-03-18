import re
from sklearn import ensemble
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
import numpy as np
from sklearn import model_selection, metrics
import warnings

warnings.filterwarnings("ignore")

data = pd.read_excel('训练模型数据2.xlsx')
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']  # 中文
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['xtick.labelsize'] = 14
plt.rcParams['ytick.labelsize'] = 14
plt.rcParams['axes.labelsize'] = 16
plt.rcParams['legend.fontsize'] = 16
plt.rcParams['figure.figsize'] = [12, 10]
plt.style.use("ggplot")

# 缺失值处理
data.fillna(value={'烹饪持续时长': data['烹饪持续时长'].mode()[0]}, inplace=True)

#存在类似于4 5的数据
def null_bu(item):
    a = re.findall('\d \d+', str(item), re.S)
    if a:
        a = a[0].split(' ')
        return float(f'{a[0]}.{a[1]}')
    if item == '(空)':
        return None
    else:
        return float(item)


data['0.1m处风速'] = data['0.1m处风速'].apply(null_bu)
data['1.1m处风速'] = data['1.1m处风速'].apply(null_bu)
data['1.7m处风速'] = data['1.7m处风速'].apply(null_bu)
data['黑球温度（tg，℃）'] = data['黑球温度（tg，℃）'].apply(null_bu)
data['整体热感受'] = data['整体热感受'].apply(lambda x: x + 1)
data = data.fillna(method='pad')
print(data.head())
# print(data.apply(lambda x: np.sum(x.isnull())))#查看空缺值
print(data['整体热感受'].unique())
data.to_csv('fsdfsd.csv')


# 预测值与相同或者相差绝对值为1，计入真实值
def difference(true, pred, sign):
    sum = 0
    if sign == 0:
        true = true.values.tolist()
    else:
        true = true
        pred = pred.values.tolist()
    for i in range(len(true)):
        if true[i] == pred[i] or abs(true[i] - pred[i]) < 1.1:
            sum += 1
        else:
            pass
    score = round(sum / len(true), 4)
    return score


# 切分数据集70% ，30%
data_column = data.columns.tolist()
sensation = data_column.pop(-1)
X = data[data_column]
y = data[sensation]
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.05, random_state=1234)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
y_train = le.fit_transform(y_train)

# **********************xgboost***************************
# 构建XGBoost分类器
def XGBoost():
    import xgboost
    xgboost = xgboost.XGBClassifier(max_depth=3, learning_rate=0.1)
    xgboost.fit(X_train, y_train)
    resample_pred = xgboost.predict(np.array(X_test))
    # 返回模型的预测效果
    print('xgboost模型的准确率为：\n', metrics.accuracy_score(y_test, resample_pred))
    print('xgboost模型的RMSE为：\n', metrics.mean_squared_error(y_test, resample_pred))
    print('xgboost模型的更新后的准确率为为：\n', difference(y_test, resample_pred, 0))
    print('xgboost模型的评估报告：\n', metrics.classification_report(y_test, resample_pred))
    plt.figure()
    plt.plot([i for i in range(len(y_test))], y_test)  # 画出模型预测
    plt.plot([i for i in range(len(resample_pred))], resample_pred)
    plt.legend(['true', 'pred'], loc='upper left')
    plt.title('xgboost模型真实值和预测值对比')
    plt.ylabel("因变量")
    plt.savefig('xgboost模型真实值和预测值对比.jpg', bbox_inches='tight')
    # plt.show()

    ndpred = pd.read_excel('test.xlsx')
    ndpred.drop(['整体热感受'], axis=1, inplace=True)
    ndpred['0.1m处风速'] = ndpred['0.1m处风速'].apply(null_bu)
    ndpred['1.1m处风速'] = ndpred['1.1m处风速'].apply(null_bu)
    ndpred['1.7m处风速'] = ndpred['1.7m处风速'].apply(null_bu)
    ndpred['黑球温度（tg，℃）'] = ndpred['黑球温度（tg，℃）'].apply(null_bu)
    fina_class_pred = xgboost.predict(ndpred)
    ndpred['整体热感受'] = fina_class_pred
    ndpred.to_excel('test1.xlsx', index=False)
XGBoost()
