# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 09:10:28 2025

@author: Vaishnavi

#Logistic Regression AUC-ROC curve
"""
#OLS method
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.formula.api as sm
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import classification_report
claimants=pd.read_csv("D:/15-Logistic_Regression/claimants.csv")
#the 0th column is CASENUM which is not useful,hence drop the column
c1=claimants.drop("CASENUM",axis=1)
c1.head()
c1.describe()
#let us check the null values
c1.isna().sum()
#There are several null values around 200
###
#let us use mean imputation for continuous data and mode imputation
#for discrete data
mean_value=c1.CLMAGE.mean()
mean_value
c1.CLMAGE=c1.CLMAGE.fillna(mean_value)
c1.CLMAGE.isna().sum()
###
#for descrete value like CLMSEX we need to use the mode imputation
mode_CLMSEX=c1.CLMSEX.mode()
mode_CLMSEX
#Here if you will observe the output it is 0 1 i.e
#mode_CLMSEX[0]=0,mode_CLMSEX[1]=1,we are passing mode_CLMSEX[0]
c1.CLMSEX=c1.CLMSEX.fillna((mode_CLMSEX)[0])
c1.CLMSEX.isna().sum()
#CLMINSUR
mode_INSUR=c1['CLMINSUR'].mode()
mode_INSUR
c1.CLMINSUR=c1.CLMINSUR.fillna((mode_CLMSEX)[0])
c1.CLMINSUR.isna().sum()
#SEATBELT
mode_SB=c1['SEATBELT'].mode()
mode_SB
c1.SEATBELT=c1.SEATBELT.fillna((mode_SB)[0])
c1.SEATBELT.isna().sum()
######################
#model building
logit_model=sm.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=c1).fit()
logit_model.summary()#here we look for coef only
#here we look coef ,value should be lower
logit_model.summary2()#AIC should be lower for better model
##AIC-(Akaike informance Coefficient)

#let us go for prediction
pred=logit_model.predict(c1.iloc[:,1:])
#############################
#To derive ROC curve

#ROC curve has tpr on y-axis and fpr on x-axis ,ideally ,tpr must be high
#fpr must be low
fpr,tpr,thresholds=roc_curve(c1.ATTORNEY,pred)
#To identify optimum threshold
optimal_idx=np.argmax(tpr-fpr)
optimal_threshold=thresholds[optimal_idx]
optimal_threshold
#0.52944 ,bydefault you can take 0.5 value as a threshold 
#now we want to identify if new value is given to the model ,it will
#fall in which region 0 or 1,for that we need to derive ROC curve
#To draw ROC curve
import pylab as pl
i=np.arange(len(tpr))
roc=pd.DataFrame({
    'fpr':pd.Series(fpr,index=i),
    'tpr':pd.Series(tpr,index=i),
    '1-fpr':pd.Series(1-fpr,index=i),
    'tf':pd.Series(tpr-(1-fpr),index=i),
    'thresholds':pd.Series(thresholds,index=i)
})
#This code creates a DataFrame called roc using Pandas (pd).
#It organises various metrics related to the Receiver Operating Charactwristics
#into columns.Each column represents a specific metric,and the rows are index
#plot ROC curve
plt.plot(fpr,tpr)
plt.xlabel("False positive rate");
plt.ylabel("True Positive rate")
roc_auc=auc(fpr,tpr)
print("Area under the curve %f"%roc_auc)
##################
#Now let us add prediction column in dataframe
c1['pred']=np.zeros(1340)
c1.loc[pred>optimal_threshold,"pred"]=1
#if predicted value is greater then optimal threshold then change pred column and ATTORNEY
#Classification report
classification=classification_report(c1["pred"],c1["ATTORNEY"])
classification
######################
#splitting the data into train and test data
train_data,test_data=train_test_split(c1,test_size=0.3)
#model building using
model=sm.logit('ATTORNEY~CLMAGE+LOSS+CLMINSUR+CLMSEX+SEATBELT',data=train_data).fit()
model.summary()
model.summary2()
#AIC is 1175.5490
#prediction on test data
test_pred=model.predict(test_data)
test_data["test_pred"]=np.zeros(402)
#taking threshold value as optimal thresold value
test_data.loc[test_pred>optimal_threshold,"test_pred"]=1
#confusion matrix
confusion_matrix=pd.crosstab(test_data.test_pred,test_data.ATTORNEY)
confusion_matrix
accuracy_matrix=(140+141)/402
accuracy_matrix
#O/P:0.6990049751243781
#Classification report 
classification_test=classification_report(test_data["test_pred"],test_data["ATTORNEY"])
classification_test
#accuracy we got as 0.70

#ROC curve and AUC
fpr,tpr,threshold=metrics.roc_curve(test_data["ATTORNEY"],test_pred)
#plot of ROC
plt.plot(fpr,tpr);
plt.xlabel("False Positive rate");
plt.ylabel("True Positive Rate")
roc_auc_test=metrics.auc(fpr,tpr)
roc_auc_test
###prediction on train data
train_pred=model.predict(train_data.iloc[:,1:])
#creating new column
train_data["train_pred"]=np.zeros(938)
train_data.loc[train_pred>optimal_threshold,"train_pred"]=1
#confusion matrix
confusion_matrix=pd.crosstab(train_data.train_pred,train_data.ATTORNEY)
confusion_matrix
####
#Accuracy Test
accuracy_test=(324+347)/938
accuracy_test
#Out[72]: 0.7153518123667377
#Classification report 
classification_train=classification_report(train_data.train_pred,train_data.ATTORNEY)
classification_train
#here we are getting the accuracy as 0.72

###############
#ROC AUC curve
roc_auc_train=metrics.auc(fpr,tpr)
plt.plot(fpr,tpr);
plt.xlabel("False Positive Rate");
plt.ylabel("True Positive rate") 

