# -*- coding: utf-8 -*-
"""Created on Thu Jan 30 08:30:02 2025
@author: Vaishnavi
"""
import pandas as pd
import numpy as np
import statsmodels.graphics.tsaplots as tsa_plots
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error
from math import sqrt
from matplotlib import pyplot

'''
pandas as pd:Import the pandas library for handling and analysizng the structure
statsmodels.graphics.tsaplots as tsa_plots: imports time-series plotting functions 
such a ACF(Autocorrection Functions) and PACF(Partial AutoCorrelation functions)
from statsmodels.tsa.arima.model import ARIMA:
Import the Arima Model for the time-series forecasting
mean_squared_error.
from sklearn.metrics import mean_squared_error:Imports the mean squatred error function,used for evaluating forecast
from math import sqrt:Imports the sqrt function to calculate the root mean square error
from matplotlib import pyplot:import pyplots from matplotlib for visualization
'''
Walmart=pd.read_csv("D:/16-TimeSeries/Walmart _Footfalls_Raw.csv")
#Data Partition
Train=Walmart.head(147)
Test=Walmart.tail(12)

tsa_plots.plot_acf(Walmart.Footfalls,lags=12)
tsa_plots.plot_pacf(Walmart.Footfalls,lags=12)
'''
When al=nalyzing ACF and PACF plots,we follow these rules:

AR Order(p) from PACF:
    
    
Look at the partial AutoCorrelation Function(PACF) plot:
The number of significant lags before the PACF drops to near zero
suggests the AR order.
IF PACF shows a sharp cuttoff after lag 4 ,we take AR(4).
MA Order (q) from ACF:
    
Look at the AutoCorrelation Function(ACF) plot.
THe number of significant lags before the ACF drops to near zero suggests the AR Order/MA order
IF ACF shows a sharp cuttoff after 6 lags ,we can take MA (6)

First you try p=4 and q=4
the you can try for p=4 and q=6

'''
#ARIMA with AR=4,MA=6
model1=ARIMA(Train.Footfalls,order=(4,1,6))
res1=model1.fit()
print(res1.summary())
'''
Creates an ARIMA model with:
    AR(Auto-Regressive term)=4
I(Integrated) term=1(indicates the first order differecing to make the data stationary)
MA(moving Average) term =6

When to USe the Differencing (d in ARIMA)
Before selecting p and q,ensure the time series is stationary:
    
If the mean and variance change over the time ,apply differencing.
USe the Augumented Dickey-Fuller(ADF) test to check for stationary.
If the series is not stationary,apply first-order differencing(d=1).

from statsmodels.tsa.statstools import adfuller
result=adfuller(Walmart.Footfalls)
print('ADF Statistic:',result[0])
print('p-value:',result[1])

If p-value>0.05,the series is not stationary ,so apply differencing (d=1)
      '''
#forecast the for the next 12 months
# Forecast for next 12 months
start_index = len(Train)
end_index = start_index+11
forecast_test = res1.predict(start=start_index,end=end_index)
print(forecast_test)
'''

start_index=len(Train):Begins prediction after the trainging the dataset.
end_index=start_index+11: Predicts the next 12 periods.
res1.predict(start=start_index,end=end_index):Generates the forecasts.

'''
#Evaluate forecasts
rmse_test=sqrt(mean_squared_error(Test.Footfalls,forecast_test))
print('Test RMSE:%.3f'%rmse_test)
#Test RMSE :172.915

#plot the forecast against the actual outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_test,color='red')
pyplot.show()

#Auto-Arima-Automatically discover the optimal order for an Arima model
#pip install pmdarima --user

'''
pmdarima is an AutoArima package that automatically selects the best(p,d,q)
start(p=0,start q=0: Initials values for AR and MA terms
      max_p=12,max_q=12:Maximum values for AR and MA
      m=1:Indicates the non-seasonal model.
      d=none:Automatically determines differencing order.
      seasonal=FAlse:Disables seasonal components
      traces=True:Displays the selection process
      stepwise=True:Uses a stepwise approach for efficiency
'''
import pmdarima as pm

#AutoML has autoTS is the package which executes automatically

ar_model=pm.auto_arima(Train.Footfalls,start_p=0,start_q=0,
                       max_p,max_q=12,#maximum p and q 
                       m=1,#frequency of series
                       d=None, #let model determine 'd'
                       seasonal=False, #No seasonal 
                       start_P=0,trace=True,
                       error_action='warn',stepwise=True)

ar_model=pm.auto_arima(Train.Footfalls,start_p=0,start_q=0,
                       max_p=12,max_q=12,
                       m=1,
                       d=None,
                       seasonal=False,
                       start_P=0,trace=True,
                       error_action='warn',stepwise=True)

#Best Parameters Arima
#Arima with AR=3,I=1,MA=5
model=ARIMA(Train.Footfalls,order=(3,1,5))
res=model.fit()
print(res.summary())

#Forecast for next 12 months
start_index=len(Train)
end_index=start_index +11
forecast_best=res.predict(start=start_index,end=end_index)
print(forecast_best)

#Evaluate forecasts
rmse_best=sqrt(mean_squared_error(Test.Footfalls,forecast_best))
print('Test RMSE :%.3f' %rmse_best)
#Test RMSE :176.276

#plot the forecasts against actual  outcomes
pyplot.plot(Test.Footfalls)
pyplot.plot(forecast_best,color='red')
pyplot.show()














