# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 08:30:46 2025
MAPE value:8.30
2nd MAPEvalue:9.80
3rd:1.50
4th=2.44
@author: Vaishnavi
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
#this we have imported becoz we are going to see the seasonality ,trend ,level,residual
from statsmodels.tsa.holtwinters import Holt
from statsmodels.tsa.holtwinters import ExponentialSmoothing

#Now to load the datasets
#cocacola=pd.read_excel("C:/Users/Vaishnavi/Downloads/CocaCola_Sales_Rawdata.csv")
cocacola=pd.read_csv("C:/Users/Vaishnavi/Downloads/CocaCola_Sales_Rawdata.csv")

#let us plot the dataset and its nature
cocacola.Sales.plot()
#splitting the data into train and test set data
#since we are working on quarterly datasets and in year there are 4  quarters
#Test data=4
#train data=38
#42-4=38
Train=cocacola.head(38)
Test=cocacola.tail(4)
#here we are considering performance parameters as mean absolute
#percentage error
#rather than mean square error
#custom function is written to calculate MPSE
def MAPE(pred,org):
    temp=np.abs((pred-org)/org)*100
    return np.mean(temp)

#EDA which comprises identification of level,trends and seasonality
#In order to separate Trend and Seasonality moving average can be done
mv_pred=cocacola["Sales"].rolling(4).mean()
mv_pred.tail(4)
#this calculates a 4-period Moving Average for the Sales column
#It smooths the data by taking the mean of the last 4 quarters at each point,hence
#now let us calculate mean absolute percentage of these
#values
MAPE(mv_pred.tail(4),Test.Sales)
#Out[19]: 8.525442688640576
#Moving Average helps to extract trend & seasonality
#MAPE evaluates prediction accuracy
#If MAPE is low,the model is performing well
#moving average is predicting complete values,out of which last 4;
#are considered as predicted values and last four values of Test.values
#basic purpose of moving average is deseasonalizing
cocacola.Sales.plot(label='org')
#This is original plot
#NOw let us separate out Trend and Seasonality 
for i in range(2,9,2):
    #it will take window size 2,4,6,8
    cocacola["Sales"].rolling(i).mean().plot(label=str(i))
    plt.legend(loc=3)
#you can see i=4 and 8 are deseasonable plots

#time series decomposition is the another technique of separating data interns 
#seasonality
decompose_ts_add=seasonal_decompose(cocacola.Sales,model="additive",period=4)
print(decompose_ts_add.trend)
print(decompose_ts_add.seasonal)
print(decompose_ts_add.resid)
print(decompose_ts_add.observed)
decompose_ts_add.plot()
'''
Trend Component

THere is a visible upward trend in sales over time,
indicating overall growth.
Seasonal Component

A clear repeating pattern is visible every four quarters(one year),
confirming strong seasonality in sales.
Residual Component

The residuals (random fluctuations) should ideally be white noise.
If they show the patterns,it suggests that other factors might be influencing sales.
'''
#similar plot can be decomposed using multiplicative 
decompose_ts_mul=seasonal_decompose(cocacola.Sales,model="mltiplicative",period=4)
print(decompose_ts_mul.trend)
print(decompose_ts_mul.seasonal)
print(decompose_ts_mul.resid)
print(decompose_ts_mul.observed)
decompose_ts_mul.plot()
#you can observe the difference between these plots
#now let us plot the ACF plot to check the auto correlation
import statsmodels.graphics.tsaplots as tsa_plots
tsa_plots.plot_acf(cocacola.Sales,lags=4)
#we can observe the output in which r1,r2,r3 and r4 has higher correlation
###This is all about EDA
#Let us apply data to data driven models
#simple exponential method
from statsmodels.tsa.holtwinters import SimpleExpSmoothing
ses_model=SimpleExpSmoothing(Train['Sales']).fit()
pred_ses=ses_model.predict(start=Test.index[0],end=Test.index[-1])
#now calculate the MAPE
MAPE(pred_ses,Test.Sales)
#we are getting 8.369866547291215
#holts winter exponential smoothing
hw_model=Holt(Train["Sales"]).fit()
pred_hw=hw_model.predict(start=Test.index[0],end=Test.index[-1])
MAPE(pred_hw,Test.Sales)
#Out[99]: 9.80978335866318

#Holts winter exponential smoothing with additive seasonality
hwe_model_add_add=ExponentialSmoothing(Train["Sales"],seasonal="add",trend="add",seasonal_periods=4).fit()
pred_hwe_model_add_add=hwe_model_add_add.predict(start=Test.index[0],end=Test.index[0])
MAPE(pred_hwe_model_add_add,Test.Sales)
#Out[100]: 2.2394072745051528

#Holts winter exponential smoothing with multiplicative seasonality
hwe_model_mul_add=ExponentialSmoothing(Train["Sales"],seasonal="mul",trend="add",seasonal_periods=4).fit()
pred_hwe_model_mul_add=hwe_model_mul_add.predict(start=Test.index[0],end=Test.index[0])
MAPE(pred_hwe_model_mul_add,Test.Sales)
#Out[101]: 0.021830412310468634

#hre sir values is less of additive but in my case the mul value is less so consider that 
#let us apply to complete data of cocacola
#we have seen that hwe_model_add_add has got the lowest MAPE,hence it is selected 
hwe_model_add_add=ExponentialSmoothing(cocacola["Sales"],seasonal="add",trend="add",seasonal_periods=4).fit()
#import the new datasets for which predictions has to be done
new_data=pd.read_csv("C:/Users/Vaishnavi/Downloads/CocaCola_Sales_New_Pred.csv") 
newdata_pred=hwe_model_add_add.predict(start=new_data.index[0],end=new_data.index[0])

#we have seen that hwe_model_add_add has got the lowest MAPE,hence it is selected 
hwe_model_add_add=ExponentialSmoothing(cocacola["Sales"],seasonal="mul",trend="add",seasonal_periods=4).fit()
#import the new datasets for which predictions has to be done
new_data=pd.read_csv("C:/Users/Vaishnavi/Downloads/CocaCola_Sales_New_Pred.csv") 
newdata_pred=hwe_model_add_add.predict(start=new_data.index[0],end=new_data.index[0])
MAPE(newdata_pred,Test.Sales)
newdata_pred
"""Out[115]: 
0    1788.32762
dtype: float64
"""

