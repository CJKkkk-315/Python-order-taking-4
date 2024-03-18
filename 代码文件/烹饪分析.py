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


# ****************************随机森林************************
def random_forest():
    RF_class = ensemble.RandomForestClassifier(n_estimators=200, random_state=1234)
    RF_class.fit(X_train, y_train)
    RFclass_pred = RF_class.predict(X_test)
    print('RF模型在测试集的准确率：\n', metrics.accuracy_score(y_test, RFclass_pred))
    print('RF模型在测试集的RMSE：\n', metrics.mean_squared_error(y_test, RFclass_pred) ** 0.5)
    print('随机森林模型在测试集更新后的准确率：\n', difference(y_test, RFclass_pred, 0))
    plt.style.use("ggplot")
    fig, ax = plt.subplots(figsize=(14, 10), dpi=80)
    importance = RF_class.feature_importances_
    Impt_Series = pd.Series(importance, index=X_train.columns)
    plt.xlabel('importance', fontsize=13)
    plt.title(f'Ranking of random forest importance', fontsize=20)
    Impt_Series.sort_values(ascending=True).plot(kind='barh')
    plt.savefig(f'Ranking of random forest importance.jpg', bbox_inches='tight')
    # plt.show()
    # *********************真实值和预测值对比****************
    plt.figure()
    plt.plot([i for i in range(len(y_test))], y_test)  # 画出模型预测
    plt.plot([i for i in range(len(RFclass_pred))], RFclass_pred)
    plt.legend(['true', 'pred'], loc='upper left')
    plt.title('随机森林模型真实值和预测值对比')
    plt.ylabel("因变量")
    plt.savefig('随机森林模型真实值和预测值对比.jpg', bbox_inches='tight')
    # plt.show()



    ndpred = pd.read_excel('test.xlsx')
    ndpred.drop(['整体热感受'],axis=1,inplace=True)
    ndpred['0.1m处风速'] = ndpred['0.1m处风速'].apply(null_bu)
    ndpred['1.1m处风速'] = ndpred['1.1m处风速'].apply(null_bu)
    ndpred['1.7m处风速'] = ndpred['1.7m处风速'].apply(null_bu)
    ndpred['黑球温度（tg，℃）'] = ndpred['黑球温度（tg，℃）'].apply(null_bu)
    fina_class_pred = RF_class.predict(ndpred)
    ndpred['整体热感受'] = fina_class_pred
    ndpred.to_excel('test1.xlsx',index=False)

random_forest()


# ***********************ANN***********************
def ANN(y_train):
    lb = preprocessing.LabelBinarizer().fit(np.array(range(6)))  # 对标签进行one_hot编码 6类
    y_train = lb.transform(y_train)  # 因为是多分类任务，必须进行编码处理
    # 1、读取数据
    # 2、keras.models Sequential   /keras.layers.core Dense Activation
    # 3、Sequential建立模型
    # 4、Dense建立层
    # 5、Activation激活函数
    # 6、compile模型编译
    # 7、fit训练（学习）
    # 8、验证（测试，分类预测）
    x2 = X_train.values
    y2 = y_train
    print(y2[:10])
    # 使用人工神经网络模型
    from keras.models import Sequential
    from keras.layers.core import Dense, Activation
    model = Sequential()
    # 输入层
    model.add(Dense(10, input_dim=len(x2[0])))
    model.add(Activation("sigmoid"))
    # model.add(Activation("relu"))
    # 输出层
    model.add(Dense(6, input_dim=6))
    model.add(Activation("sigmoid"))
    # model.summary()
    # 模型的编译
    model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer="adam")

    history = model.fit(x2, y2, batch_size=10, epochs=100, validation_data=(x2, y2))  # 每个批次数据量为10
    y_pre = model.predict(X_test).argmax(axis=1)  # 开始预测，axis=1表示返回每行中数值（表示每个类别的概率）最大的下标，就是对应的标签
    print(y_pre)

    print("验证集 accuracy_score: %.4lf" % metrics.accuracy_score(y_pre, y_test))
    print("ANN模型的RMSE: %.4lf" % metrics.mean_squared_error(y_pre, y_test) ** 0.5)
    print('ANN模型在测试集更新后的准确率：\n', difference(y_pre, y_test, 1))
    # *********************真实值和预测值对比****************
    plt.figure()
    plt.plot([i for i in range(len(y_test))], y_test)  # 画出模型预测
    plt.plot([i for i in range(len(y_pre))], y_pre)
    plt.legend(['true', 'pred'], loc='upper left')
    plt.title('ANN模型真实值和预测值对比')
    plt.ylabel("因变量")
    plt.savefig('ANN模型真实值和预测值对比.jpg', bbox_inches='tight')
    plt.show()

    # 绘制训练过程的acc和loss
    # ***********************LeNet-5 Loss*******************
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['val_accuracy'])
    plt.legend(['acc', 'val_acc'], loc='upper left')
    plt.title('LeNet-5 Acc')
    plt.xlabel("Epoch")  # 横坐标名
    plt.ylabel("Accuracy")  # 纵坐标名
    plt.savefig('LeNet-5 acc.jpg', bbox_inches='tight')
    plt.show()

    # ***********************LeNet-5 Loss*******************
    plt.figure()
    plt.plot(history.history['loss'])
    plt.plot(history.history['val_loss'])
    plt.legend(['loss', 'val_loss'], loc='upper left')
    plt.title('LeNet-5 Loss')
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.savefig('LeNet-5 loss.jpg', bbox_inches='tight')
    plt.show()


# ANN(y_train)
