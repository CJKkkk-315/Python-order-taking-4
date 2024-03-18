# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:56:13 2017

@author: wudi
"""

import pandas as pd
data=pd.read_csv('diabetes.csv',index_col=0)#将索引是0的列当作数据表的行标
#数据预处理
Index=data.columns
xtitle=[index for index in Index if 'x.' in index]#找出自变量矩阵x的列名
x2title=[index for index in Index if 'x2.' in index]#找出自变量矩阵x2的列名
xdata=data[xtitle]
x2data=data[x2title]
ydata=data['y']
#自变量矩阵条件数
import numpy as np
def kappa(x):
    x=np.array(x)
    XX=np.dot(x.T,x)
    lam=np.linalg.eigvals(XX)
    return(np.sqrt(lam.max()/lam.min()))
kappa(x2data) #5472.957046414529
#最小二乘回归
import statsmodels.api as sm
import matplotlib.pyplot as plt
import scipy
X=sm.add_constant(x2data,prepend=True)
lm=sm.OLS(ydata,X)
lm_result=lm.fit()
dir(lm_result)#查看类里有什么属性#
lm_result.summary()
#拟合值与餐擦散点图
y_hat=lm_result.fittedvalues
res=lm_result.resid
plt.plot(y_hat,res,'.k')
plt.xlabel('yhat')
plt.ylabel('residuals')
plt.show()

W,p_value=scipy.stats.shapiro(res)#夏皮洛-威尔克检验
#W=0.9937732815742493，p_value=0.06650751084089279与R得到结果相同

#Ridge#
from sklearn import linear_model
n_alphas=200
alphas=np.logspace(-10, -2, n_alphas)
clf=linear_model.Ridge(fit_intercept=False)#去掉截距项#
coefs=[]
for a in alphas:
    clf.set_params(alpha=a)
    clf.fit(X,ydata)
    coefs.append(clf.coef_)
ax=plt.gca()
ax.plot(alphas, coefs)
ax.set_xscale('log')
ax.set_xlim(ax.get_xlim())
plt.xlabel('alpha')
plt.ylabel('weights')
plt.title('Ridge coefficients as a function of the regularization')
plt.axis('tight')
plt.show()
#lasso#
from sklearn.linear_model import lasso_path
eps = 5e-5  # the smaller it is the longer is the path
alphas_lasso,coefs_lasso,_=lasso_path(X,ydata,eps,fit_intercept=False)
ax=plt.gca()
ax.plot(np.log(alphas_lasso),coefs_lasso.T)
ax.set_xlim(ax.get_xlim())
plt.xlabel('Log(alpha)')
plt.ylabel('coefficients')
plt.title('lasso coefficients')
plt.axis('tight')
plt.show()
#利用AIC和BIC准则选择lasso的最优参数alpha#
import time
from sklearn.linear_model import LassoCV, LassoLarsCV, LassoLarsIC
#LassoLarsIC#
model_bic=LassoLarsIC(criterion='bic',fit_intercept=False)
t1=time.time()
model_bic.fit(X,ydata)
t_bic=time.time()-t1
alpha_bic_=model_bic.alpha_ #0.20694147313160893

model_aic=LassoLarsIC(criterion='aic',fit_intercept=False)
model_aic.fit(X,ydata)
alpha_aic_=model_aic.alpha_ #0.11744005093693313
#根据不同准的进行变量选择#
def plot_ic_criterion(model,name,color):
    alpha_=model.alpha_
    alphas_=model.alphas_
    criterion_=model.criterion_
    plt.plot(-np.log10(alphas_),criterion_,'--',color=color,
             linewidth=3,label='%s criterion' % name)
    plt.axvline(-np.log10(alpha_),color=color,linewidth=3,
                label='alpha: %s estimate' % name)
    plt.xlabel('-log(alpha)')
    plt.ylabel('criterion')

plt.figure()
plot_ic_criterion(model_aic,'AIC','b')
plot_ic_criterion(model_bic,'BIC','r')
plt.legend()
plt.title('Information-criterion for model selection (training time %.3fs)' 
            % t_bic)
plt.show()
#20折交叉验证#
t1=time.time()
model=LassoCV(cv=20).fit(X,ydata)
t_lasso_cv=time.time()-t1
# Display results
m_log_alphas=-np.log10(model.alphas_)
plt.figure()
ymin, ymax=2500,3800
plt.plot(m_log_alphas,model.mse_path_,':')
plt.plot(m_log_alphas,model.mse_path_.mean(axis=-1),'k',
         label='Average across the folds',linewidth=2)
plt.axvline(-np.log10(model.alpha_),linestyle='--',color='k',
            label='alpha: CV estimate')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean square error')
plt.title('Mean square error on each fold: coordinate descent '
          '(train time: %.2fs)' % t_lasso_cv)
plt.axis('tight')
plt.ylim(ymin,ymax)
plt.show()
#最小角回归方法
t1=time.time()
model=LassoLarsCV(cv=20).fit(X,ydata)
t_lasso_lars_cv=time.time()-t1
# Display results
m_log_alphas=-np.log10(model.cv_alphas_)
plt.figure()
plt.plot(m_log_alphas,model.cv_mse_path_, ':')
plt.plot(m_log_alphas,model.cv_mse_path_.mean(axis=-1),'k',
         label='Average across the folds',linewidth=2)
plt.axvline(-np.log10(model.alpha_),linestyle='--',color='k',
            label='alpha CV')
plt.legend()
plt.xlabel('-log(alpha)')
plt.ylabel('Mean square error')
plt.title('Mean square error on each fold: Lars (train time: %.2fs)'
          % t_lasso_lars_cv)
plt.axis('tight')
plt.ylim(ymin,ymax)
plt.show()
#恩格尔数据
reg=linear_model.Lasso(alpha=model.alpha_,fit_intercept=False)
reg.fit(X,ydata)
dir(reg)
#读入数据
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
data=sm.datasets.engel.load_pandas().data
#描述统计
fig=plt.figure()
ax=fig.add_subplot(1,1,1)
box=plt.boxplot((data['foodexp'],data['income']),
                notch=True, patch_artist=True,labels=['foodexp','income'])
colors = ['lightblue','pink']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)
    patch.set_alpha(1)
plt.show()
#分位回归与线性回归
quantiles=np.arange(.05,.96,.1)
def fit_model(q):
    mod=smf.quantreg('foodexp~income',data)
    res=mod.fit(q=q)
    return([q,res.params['Intercept'],res.params['income']]+ 
            res.conf_int().ix['income'].tolist())

models=[fit_model(x) for x in quantiles]
models=pd.DataFrame(models,columns=['q','a','b','lb','ub'])

ols=smf.ols('foodexp~income',data).fit()
ols_ci=ols.conf_int().ix['income'].tolist()
ols=dict(a=ols.params['Intercept'],
           b=ols.params['income'],
           lb=ols_ci[0],
           ub=ols_ci[1])

x=np.arange(data.income.min(),data.income.max(),50)
get_y=lambda a,b:a+b*x

fig,ax=plt.subplots(figsize=(8,6))

for i in range(models.shape[0]):
    y=get_y(models.a[i],models.b[i])
    ax.plot(x,y,linestyle='dotted',color='grey')

y=get_y(ols['a'],ols['b'])

ax.plot(x,y,color='red',label='OLS')
ax.scatter(data.income,data.foodexp,alpha=.2)
ax.set_xlim((240,3000))
ax.set_ylim((240,2000))
legend=ax.legend()
ax.set_xlabel('Income',fontsize=16)
ax.set_ylabel('Food expenditure',fontsize=16)
plt.show()

ax=plt.figure()
n=models.shape[0]
p1=plt.plot(models.q,models.b,color='black',label='Quantile Reg.')
p2=plt.plot(models.q,np.array(models.ub),linestyle='dotted',color='black')
p3=plt.plot(models.q,np.array(models.lb),linestyle='dotted',color='black')
p4=plt.plot(models.q,[ols['b']]*n,color='red',label='OLS')
p5=plt.plot(models.q,[ols['lb']]*n,linestyle='dotted',color='red')
p6=plt.plot(models.q,[ols['ub']]*n,linestyle='dotted',color='red')
plt.ylabel('beta')
plt.xlabel('Quantiles of the conditional food expenditure distribution')
plt.legend()
plt.show()