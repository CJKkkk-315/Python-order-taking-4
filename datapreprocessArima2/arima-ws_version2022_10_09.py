#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ARIMA script for wind speed and direction
Modified from https://github.com/shashanksharma1995/Wind-Speed-Prediction-using-Statistical-Model/blob/master/ARIMA_10_daily.ipynb

"""



from pandas import read_csv
import matplotlib.pyplot as plt
import pandas as pd
import pmdarima
from pmdarima import auto_arima
import numpy as np
import sklearn
from pandas.plotting import autocorrelation_plot
from statsmodels.graphics.tsaplots import plot_acf
from statsmodels.graphics.tsaplots import plot_pacf

import statsmodels.api as sm


from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

#from statsmodels.tsa.arima_model import ARIMA

series = read_csv('./Processed_data20221009-160018.csv', header=0, sep=",", squeeze=True, parse_dates=True)
#series
#series = series[301:600]
#series
#series = series.drop('Wind Direction daily mean', 1)
#series = series.drop('Minute', 1)
#series = series.drop('Year', 1)
#series = series.drop('Month', 1)
#series = series.drop('Day', 1)
#series = series.drop('Hour', 1)
#series
series = series.drop('count', 1)
# Wind Speed Plot
series.plot()
plt.xlabel('Days')
plt.ylabel('Wind Speed (Km/hr) at 10m')
plt.show()

# ACF Plot

plot_acf(series, lags = 50)
#autocorrelation_plot(series)
plt.show()

# PACF Plot

plot_pacf(series, lags = 50)
plt.show()




# fit model
ARIMA = sm.tsa.arima.ARIMA
model = ARIMA(series, order=(2,1,2))
#model_fit = model.fit(disp=0)
model_fit = model.fit()
print(model_fit.summary())

# plot residual erros
residuals = pd.DataFrame(model_fit.resid)
residuals.plot()
residuals.plot(kind='kde')
plt.show()
print(residuals.describe())
# Model-1 (LOOP-TRAINING)



X = series.values
size = int(len(X) * 0.80)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = []
for t in range(len(test)):
    #model = ARIMA(history, order=(4,1,1))
    model = ARIMA(history, order=(4,1,1))
    #model_fit = model.fit(disp=0)
    model_fit = model.fit()
    output = model_fit.forecast()
    yhat = output[0]
    predictions.append(yhat)
    obs = test[t]
    history.append(obs)
    print('Example=%f, predicted=%f, expected=%f' % (t, yhat, obs))

error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)

error = mean_absolute_error(test, predictions)
print('Test MAE: %.3f' % error)

# plot
plt.plot(train)
plt.xlabel('Days')
plt.ylabel('Wind Speed (Km/hr) at 10m')
plt.show()
plt.plot(test, 'y')
plt.plot(predictions, 'g-.')
plt.xlabel('Days')
plt.ylabel('Wind Speed (Km/hr) at 10m')
plt.show()
# Model-2 (Auto ARIMA)

X = series.values

#divide into train and test set
train1 = series[:int(0.80*(len(X)))]
test1 = series[int(0.80*(len(X))):]

#plotting the data

train1['Wind Speed daily mean'].plot()
test1['Wind Speed daily mean'].plot()

# arima

# Auto ARIMA Model

model = auto_arima(train1, trace=True, error_action='ignore', suppress_warnings=True)
model.fit(train1)

forecast = model.predict(n_periods=len(test1))
forecast = pd.DataFrame(forecast,index = test1.index,columns=['Prediction'])






# plot the predictions for Test set
plt.plot(forecast, label='Prediction', color = 'red')
plt.xlabel('Days')
plt.ylabel('Wind Speed (Km/hr) at 10m')
plt.show()




error = mean_squared_error(test1, forecast)
print('Test MSE: %.3f' % error)

error = mean_absolute_error(test1, forecast)
print('Test MAE: %.3f' % error)


X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
model = ARIMA(train, order=(5, 2, 2))
model_fit = model.fit()

output = model_fit.forecast(steps=len(test))
yhat = output#[0]
# predictions.append(yhat)

for t in range(len(test)):
    # history.append(obs)
    obs = test[t]
    #print("T is ::::::", t,type(t))
    #print(yhat,type(yhat))
    print('Example=%f, predicted=%f, expected=%f' % (t, yhat[t], obs))
error = mean_squared_error(test, yhat)
print('Test MSE: %.3f' % error)
# plot
plt.plot(test)
plt.plot(yhat, color='yellow')
plt.show()
