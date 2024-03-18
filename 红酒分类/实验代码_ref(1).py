import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import recall_score,precision_score,classification_report, accuracy_score, confusion_matrix
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings("ignore")

dataset_winered = pd.read_csv('winequality-red.csv',sep='[:,|_;]',engine='python')

#print(dataset_winered.info)
#print(dataset_winewhite.info)

wine_data = np.array(dataset_winered)
dataset_winered_factor , dataset_winered_quality = wine_data[:,:-1],wine_data[:,-1]

x_train_winered,x_test_winered,y_train_winered,y_test_winered = train_test_split(dataset_winered_factor,dataset_winered_quality,test_size=0.1)

res_accuracy_score = []
res_precision_score = []
res_recall_score = []
#SVM支持向量机
def SVM(trainX,trainY,testX,testY):

    stdScale = StandardScaler()
    x_train = stdScale.fit_transform(trainX)
    x_test = stdScale.fit_transform(testX)
    for i in range(10):
        model = SVC(C=10,kernel="rbf",decision_function_shape="ovr")
        model.fit(x_train, trainY)
        y_pred = model.predict(x_test)

        res_accuracy_score.append(accuracy_score(testY, y_pred))
        res_precision_score.append(precision_score(testY, y_pred,average='macro'))
        res_recall_score.append(recall_score(testY, y_pred,average='macro'))

    print("SVM分类器预测结果")
    print('准确率：', sum(res_accuracy_score)/len(res_accuracy_score))
    print('精确率：', sum(res_precision_score)/len(res_accuracy_score))
    print('召回率：', sum(res_recall_score)/len(res_recall_score))
    print('混淆矩阵:\n',confusion_matrix(testY,y_pred))
res_accuracy_score2 = []
res_precision_score2 = []
res_recall_score2 = []
# 随机森林
def RF(trainX, trainY, testX, testY):

    stdScale = StandardScaler()
    x_train = stdScale.fit_transform(trainX)
    x_test = stdScale.fit_transform(testX)
    for i in range(10):
        model = RandomForestClassifier()
        model.fit(x_train, trainY)
        y_pred = model.predict(x_test)

        res_accuracy_score2.append(accuracy_score(testY, y_pred))
        res_precision_score2.append(precision_score(testY, y_pred, average='macro'))
        res_recall_score2.append(recall_score(testY, y_pred, average='macro'))


    print("随机森林分类器预测结果")
    print('准确率：', sum(res_accuracy_score2) / len(res_accuracy_score2))
    print('精确率：', sum(res_precision_score2) / len(res_accuracy_score2))
    print('召回率：', sum(res_recall_score2) / len(res_recall_score2))
    print('混淆矩阵:\n', confusion_matrix(testY, y_pred))

SVM(trainX=x_train_winered,trainY=y_train_winered,testX=x_test_winered,testY=y_test_winered)
RF(trainX=x_train_winered,trainY=y_train_winered,testX=x_test_winered,testY=y_test_winered)
plt.plot([i for i in range(10)],res_accuracy_score,label='SVM accuracy')
plt.plot([i for i in range(10)], res_accuracy_score2, label='Random Forest accuracy')
plt.legend()
plt.show()

plt.plot([i for i in range(10)],res_precision_score,label='SVM precision')
plt.plot([i for i in range(10)], res_precision_score2, label='Random Forest precision')
plt.legend()
plt.show()


plt.plot([i for i in range(10)],res_recall_score,label='SVM recall')
plt.plot([i for i in range(10)], res_recall_score2, label='Random Forest recall')
plt.legend()
plt.show()


