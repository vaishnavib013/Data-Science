# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 08:37:39 2024

@author: Vaishnavi
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/11-KNN/4_Decision_Tree/credit.csv")
##data prpartition
#check for null values
data.isnull().sum()
data.dropna()
data.columns
#There are 9 columns having non numeric values,let us 
#there is one column called phone which is not useful,
data=data.drop(["phone"],axis=1)
#now there are 16 columns
lb=LabelEncoder()
data["Checking_balance"]=lb.fit_transform(data["checking_balance"])
data["credit_history"]=lb.fit_transform(data["credit_history"])
data["purpose"]=lb.fit_transform(data["purpose"])
data["savings_balance"]=lb.fit_transform(data["savings_balance"])
data["employment_duration"]=lb.fit_transform(data["employment_duration"])
data["other_credit"]=lb.fit_transform(data["employment_duration"])
data["housing"]=lb.fit_transform(data["housing"])
data["job"]=lb.fit_transform(data["job"])

#check for non-numeric columns
non_numeric_cols=data.select_dtypes(include=['object']).columns
print(non_numeric_cols)
data["checking_balance"]=lb.fit_transform(data["checking_balance"])
data["default"]=lb.fit_transform(data["default"])


##now let us check how many unique values are there in target column
data["default"].unique()
data["default"].value_counts()
##now we want ro split tree,we need all feature columns
colnames=list(data.columns)
#now let us assign these columns to variable predictor
predictors=colnames[:15]
target=colnames[15]

#splitting data into training ad testing data set
from sklearn.model_selection import train_test_split
train,test=train_test_split(data,test_size=0.3)

from sklearn.tree import DecisionTreeClassifier as DT

help(DT)

model=DT(criterion='entropy')
model.fit(train[predictors],train[target])

#prediction on test data
preds=model.predict(test[predictors])
pd.crosstab(test[target],preds,rownames=['Actual'],colnames=['Predictions'])
"""
Out[46]: 
Predictions    0   1
Actual              
0            157  51
1             55  37
"""
np.mean(preds==test[target])#Test Data Accuracy
#O/p:0.6466666666666666

#prediction on train data 
preds=model.predict(train[predictors])
pd.crosstab(train[target],preds,rownames=['Actual'],colnames=['Predictions'])

np.mean(preds==train[target])#train data accuracy
#Out[53]: 1.0