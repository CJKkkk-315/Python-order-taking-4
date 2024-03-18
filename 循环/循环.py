import pandas as pd
import statsmodels.api as sm
import os
import warnings
warnings.filterwarnings('ignore')
files = os.listdir('短期基金')
for file in files:
    print(file)
    try:
        # Step 1: 导入rp, rf和rm的收益率序列（已做数据清洗）
        path = '短期基金/' + file  # 输入你的数据存储地址
        data = pd.read_excel(path,nrows=152)  # 读取数据
        pd.set_option('mode.chained_assignment', None)
        # Step 2：构造所需要的模型
        data['Ex_Rm'] = data['Rm'] - data['Rf']
        data['Ex_Rp'] = data['Rp'] - data['Rf']
        data['sqr_Ex_Rm'] = data['Ex_Rm'] ** 2
        data['Ex_Rm+'], data['Ex_Rm-'] = data['Ex_Rm'].copy(), data['Ex_Rm'].copy()
        for i in data.index:
            if data['Ex_Rm'][i] >= 0:
                data['Ex_Rm+'][i] = data['Ex_Rm'][i]
                data['Ex_Rm-'][i] = 0
            else:
                data['Ex_Rm-'][i] = data['Ex_Rm'][i]
                data['Ex_Rm+'][i] = 0
        # print(data.head())
        # Step 3: 模型输入-输出变量准备
        y = data[['Ex_Rp']]  # 模型输出变量矩阵
        X_TM = sm.add_constant(data[['Ex_Rm', 'sqr_Ex_Rm']])  # T-M模型输入变量矩阵
        X_HM = sm.add_constant(data[['Ex_Rm', 'Ex_Rm+']])  # H-M模型输入变量矩阵
        # Step 4: 模型训练
        TM = sm.OLS(y, X_TM).fit()  # T-M拟合模型
        HM = sm.OLS(y, X_HM).fit()  # H-M拟合模型
        # Step 5: 输出结果

        print(TM.summary())
        print(HM.summary())
    except:
        print('该基金数据有误！')
    print('#######################################################################################################################')
    print()
    print()
    print()