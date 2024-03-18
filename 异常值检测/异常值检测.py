# 引入需要的库
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score,mean_squared_error
from sklearn.model_selection import train_test_split
from scipy import stats
import warnings
# 忽略警告
warnings.filterwarnings('ignore')
# 读取数据
df = pd.read_excel('数据300(2).xlsx')
# 序号列无用，丢弃
df.drop(['序号'],axis=1,inplace=True)
# 将时间转为年月日，小时4个新列
df['检测时间'] = pd.to_datetime(df['检测时间'])
df['year'] = df['检测时间'].dt.year
df['month'] = df['检测时间'].dt.month
df['day'] = df['检测时间'].dt.day
df['hour'] = df['检测时间'].dt.hour
# 转换后丢弃原来的列
df.drop(['检测时间'],axis=1,inplace=True)
# print(df)
# 定义一个名为three_sigma_check的函数，输入一个数据框，输出剔除三西格玛法异常值后的数据框
def three_sigma_chek(df):
    df_copy = df.copy()  # 复制一个数据框
    for column in df_copy.columns[:-4]:  # 遍历数据框的每一列

        mean = df_copy[column].mean()  # 计算该列的均值
        std_deviation = df_copy[column].std()  # 计算该列的标准差
        lower_bound = mean - 3 * std_deviation  # 计算该列的下界
        upper_bound = mean + 3 * std_deviation  # 计算该列的上界
        # 将该列中低于下界和高于上界的值替换为缺失值

        df_copy[column] = np.where((df_copy[column] < lower_bound) | (df_copy[column] > upper_bound), np.nan, df_copy[column])
    print('three_sigma:')
    for column in df_copy.columns[:-4]:
        res = []
        for idx, value in enumerate(df_copy[column]):
            if str(value) == 'nan':
                res.append((idx,df[column][idx]))
        print(column,res)

    return df_copy  # 返回处理后的数据框

# 定义一个名为pca_check的函数，输入一个数据框，输出剔除PCA重构误差异常值后的数据框
def pca_check(df):
    df_copy = df.copy()  # 复制一个数据框
    scaler = StandardScaler()  # 初始化一个标准化对象
    scaled_df = scaler.fit_transform(df_copy)  # 对数据框进行标准化
    pca = PCA(n_components=2)  # 初始化一个PCA对象，设置主成分个数为2
    pca_data = pca.fit_transform(scaled_df)  # 对标准化后的数据进行PCA降维
    reconstructed_data = pca.inverse_transform(pca_data)  # 对降维后的数据进行重构
    distances = np.sum((scaled_df - reconstructed_data) ** 2, axis=1)  # 计算重构误差
    threshold = np.percentile(distances, 95)  # 计算重构误差的95分位数
    outliers = distances > threshold  # 判断哪些数据点的重构误差大于阈值
    for column in df_copy.columns[:-4]:  # 遍历数据框的每一列
        # 将异常值替换为缺失值
        df_copy[column] = np.where(outliers, np.nan, df_copy[column])
    print('pca:')
    for column in df_copy.columns[:-4]:
        res = []
        for idx, value in enumerate(df_copy[column]):
            if str(value) == 'nan':
                res.append((idx,df[column][idx]))
        print(column,res)
    return df_copy  # 返回处理后的数据框

# 定义一个名为iForest_check的函数，输入一个数据框，输出剔除孤立森林检测异常值后的数据框
def iForest_check(df):
    df_copy = df.copy()  # 复制一个数据框
    iforest = IsolationForest(contamination='auto')  # 初始化一个孤立森林对象，异常值比例设置为自动
    for col in df_copy.columns[:-4]:  # 遍历数据框的每一列
        iforest.fit(df_copy[[col]])  # 对该列进行孤立森林拟合
        anomaly_predictions = iforest.predict(df_copy[[col]])  # 对该列数据进行异常值预测
        # 将预测为异常值的数据替换为缺失值
        df_copy[col] = df_copy[col].where(anomaly_predictions == 1, np.nan)
    print('iForest:')
    for column in df_copy.columns[:-4]:
        res = []
        for idx, value in enumerate(df_copy[column]):
            if str(value) == 'nan':
                res.append((idx,df[column][idx]))
        print(column,res)
    return df_copy  # 返回处理后的数据框
# 定义一个名为boxplot的函数，输入一个数据框，输出剔除箱线图异常值后的数据框
def boxplot(df):
    df_copy = df.copy()  # 复制一个数据框
    for column in df_copy.columns[:-4]:  # 遍历数据框的每一列
        Q1 = df_copy[column].quantile(0.25)  # 计算该列的第一四分位数
        Q3 = df_copy[column].quantile(0.75)  # 计算该列的第三四分位数
        IQR = Q3 - Q1  # 计算该列的四分位距
        lower_bound = Q1 - 1.5 * IQR  # 计算该列的下界
        upper_bound = Q3 + 1.5 * IQR  # 计算该列的上界
        # 将该列中低于下界和高于上界的值替换为缺失值
        df_copy[column] = np.where((df_copy[column] < lower_bound) | (df_copy[column] > upper_bound), np.nan,
                                   df_copy[column])
    print('boxplot:')
    for column in df_copy.columns[:-4]:
        res = []
        for idx, value in enumerate(df_copy[column]):
            if str(value) == 'nan':
                res.append((idx,df[column][idx]))
        print(column,res)
    return df_copy  # 返回处理后的数据框
# 定义一个名为Zscore的函数，输入一个数据框，输出剔除Z分数异常值后的数据框
def Zscore(df):
    df_copy = df.copy() # 复制一个数据框
    # 计算数据框中数值类型列的Z分数
    z_scores = pd.DataFrame(stats.zscore(df_copy.select_dtypes(include=[np.number])),index=df_copy.index, columns=df_copy.select_dtypes(include=[np.number]).columns)
    threshold = 2 # 设置阈值为2
    # 将Z分数绝对值大于阈值的数据替换为缺失值
    df_copy.loc[:, z_scores.columns] = df_copy.loc[:, z_scores.columns].where(np.abs(z_scores) <= threshold)
    print('Zscore:')
    for column in df_copy.columns[:-4]:
        res = []
        for idx, value in enumerate(df_copy[column]):
            if str(value) == 'nan':
                res.append((idx,df[column][idx]))
        print(column,res)
    return df_copy  # 返回处理后的数据框
# 定义一个名为final_predict的函数，输入一个数据框和目标变量的索引，输出SVR和神经网络模型的预测结果及评分
def final_predict(df, target_idx):
    X = df.drop([target_idx], axis=1)  # 将目标变量列从数据框中移除，得到特征矩阵X
    y = df[target_idx]  # 获取目标变量列，得到标签向量y
    # 将数据集拆分为训练集和测试集，测试集大小为20%
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=False)
    model = SVR()  # 初始化一个支持向量回归(SVR)模型
    model.fit(X_train, y_train)  # 对训练集进行拟合
    y_pred = model.predict(X_test)  # 对测试集进行预测
    xcopy = X_test.copy()
    xcopy[target_idx] = y_pred
    print(f'SVR预测{target_idx}结果：')
    print(xcopy)

    # 打印SVR模型对目标变量的R2得分
    print(f'SVR对{target_idx}预测的R2得分：', r2_score(y_test, y_pred))
    # 打印SVR模型对目标变量的均方误差得分
    print(f'SVR对{target_idx}预测的MSE得分：', mean_squared_error(y_test, y_pred))

    model = MLPRegressor(max_iter=2000)  # 初始化一个多层感知机(神经网络)回归模型，最大迭代次数设置为2000
    model.fit(X_train, y_train)  # 对训练集进行拟合
    y_pred = model.predict(X_test)  # 对测试集进行预测
    xcopy = X_test.copy()
    xcopy[target_idx] = y_pred
    print(f'神经网络预测{target_idx}结果：')
    print(xcopy)
    # 打印神经网络模型对目标变量的R2得分
    print(f'神经网络对{target_idx}预测的R2得分：', r2_score(y_test, y_pred))
    # 打印神经网络模型对目标变量的均方误差得分
    print(f'神经网络对{target_idx}预测的MSE得分：', mean_squared_error(y_test, y_pred))


# 输出不同方法检测以后得到的异常值数量
print("3sigma检测后，DataFrame中的异常值数量:", three_sigma_chek(df).isna().sum().sum())
print("pca检测后，DataFrame中的异常值数量:", pca_check(df).isna().sum().sum())
print("iForest检测后，DataFrame中的异常值数量:", iForest_check(df).isna().sum().sum())
print("boxplot检测后，DataFrame中的异常值数量:", boxplot(df).isna().sum().sum())
print("Zscore检测后，DataFrame中的异常值数量", Zscore(df).isna().sum().sum())

pd.set_option('display.max_rows', None)  # 显示所有行
pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.width', None)  # 不折叠单元格
pd.set_option('display.max_colwidth', None)  # 显示完整的单元格内容


# 选择3sigma作为最终方法
df_copy = three_sigma_chek(df)
print('异常值检测后:')
print(df_copy)
# 将最终方法处理完的DF进行众数填充
df_copy = df_copy.apply(lambda x: x.fillna(x.mode().iloc[0]))
print('填充异常值后:')
print(df_copy)
# 依次对四个不同变量进行预测
target_idxs = ['氢气','甲烷','乙烷','乙烯']
for target_idx in target_idxs:
    final_predict(df_copy,target_idx)