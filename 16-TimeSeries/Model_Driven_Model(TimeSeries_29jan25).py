# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:40:04 2025

@author: Vaishnavi
"""
import pandas as pd
walmart=pd.read_csv("C:/Users/Vaishnavi/Downloads/Walmart _Footfalls_Raw.csv")
month=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
#in Walmart data we have Jan-1991 in 0th Column we need only first three letters
#example:jan from each cell
p=walmart["Month"][0]
p[0:3]
#before we will extract ,let us create the new column called months to store the month initials
walmart['months']=0
#you can check the dataframes with the months name with all values 0
#the total records are 159 in walmart
for i in range(159):
    p=walmart["Month"][i]
    walmart["months"][i]=p[0:3]
    #for all these months create dummy variables
month_dummies=pd.DataFrame(pd.get_dummies(walmart['months']))
#now let us concatenate these dumy values to dataframe'
walmart1=pd.concat([walmart,month_dummies],axis=1)
#you can check the dataframe walmart1
#similarly we need to create the column t
import numpy as np
walmart1['t']=np.arange(1,160)
walmart1['t_squared']=walmart1['t']*walmart1['t']
walmart1['log_footfalls']=np.log(walmart1['Footfalls'])
walmart1.columns
#now let us check the visuals of the footfall
walmart1.Footfalls.plot()
#you will get exponential trend with first decreasing and then increasing 
#we have to forecast the footfalls in next 12 months,hence horizon=12 ,even 
#season=12,so validating data will be 12 and training will 159-12-147
Train=walmart1.head(147)
Test=walmart1.tail(12)
#now let us apply linear regression
import statsmodels.formula.api as smf

##Linear Model
linear_model=smf.ols("Footfalls~t",data=Train).fit()
pred_linear=pd.Series(linear_model.predict(pd.DataFrame(Test['t'])))
rmse_linear=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_linear))**2))
rmse_linear
#Out[158]: 209.92559265462594
#here we got the erros so high ,so we will try with other models and see of the other models has less values
#we are checking for low value as it would be telling us how much error we are getting 
#so,we want less value 

##Exponential Model
Exp_model=smf.ols("log_footfalls~t",data=Train).fit()
pred_Exp=pd.Series(Exp_model.predict(pd.DataFrame(Test['t'])))
rmse_Exp=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.exp(pred_Exp))**2))
rmse_Exp
#Out[162]: 217.05263566813454

#Quadratic Model
Quad=smf.ols("Footfalls~t+t_squared",data=Train).fit()
pred_Quad=pd.Series(Quad.predict(Test[["t","t_squared"]]))
rmse_Quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_Quad))**2))
rmse_Quad
#Out[166]: 137.1546274135642
#here we got the comparing other models this is the less error value till now

#Additive Seasonality
add_sea=smf.ols("Footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov",data=Train).fit()
#here we take upto Nov only,no need to take upto Dec 
#it would be giving us same
#Ingeneral also we take upto Nov not upto Dec
add_sea.summary()
pred_add_sea=pd.Series(add_sea.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov']]))
rmse_add_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(pred_add_sea))**2))
rmse_add_sea
#Out[185]: 264.6643900568777

#Multiplicative Seasonality
mul_sea=smf.ols("Footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov",data=Train).fit()
#here we take upto Nov only,no need to take upto Dec 
#it would be giving us same
#Ingeneral also we take upto Nov not upto Dec
#mul_sea.summary()
mul_sea=smf.ols("log_footfalls~Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov",data=Train).fit()
pred_mul_sea=pd.Series(mul_sea.predict(Test))
rmse_mul_sea=np.sqrt(np.mean((np.array(Test['Footfalls'])-np.array(np.exp(pred_mul_sea)))**2))
rmse_mul_sea
#Out[214]: 268.197032530918

#Additive Seasonality with Quadratic Trend
add_sea_quad=smf.ols('Footfalls~t+t_squared+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=Train).fit()
pred_add_sea_quad=pd.Series(add_sea_quad.predict(Test[['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','t','t_squared']]))
rmse_add_sea_quad=np.sqrt(np.mean((np.array(Test['Footfalls'])-(np.array(pred_add_sea_quad)))**2))
rmse_add_sea_quad
#Out[213]: 50.60724584032393
#from all of the abpove models we found that additive seasonality qudratic trend is giving us mininum error

#create the dataframe and add all these rmse_values
data={"Model":pd.Series(['rmse_linear','rmse_Exp','rmse_Quad','rmse_add_sea','rmse_mul_sea','rmse_add_sea_quad']),
      "RMSE_Values":pd.Series([rmse_linear,rmse_Exp,rmse_Quad,rmse_add_sea,rmse_mul_sea,rmse_add_sea_quad])}
data

##Now let us test the model with full data
#predict_data=pd.read_excel("C:/Users/Vaishnavi/Downloads/Predict_new.xlsx")
#using this it doesnt execute
predict_data=pd.read_csv("C:/Users/Vaishnavi/Downloads/Predict_new.csv")

predict_data
model_full=smf.ols('Footfalls~t+t_squared+Jan+Feb+Mar+Apr+May+Jun+Jul+Aug+Sep+Oct+Nov',data=walmart1).fit()
pred_new=pd.Series(model_full.predict(predict_data))
pred_new

predict_data["forecasted_Footfalls"]=pd.Series(pred_new)
predict_data

###AR models
#let us find out the errors
