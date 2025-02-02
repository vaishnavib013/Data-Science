# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 08:38:14 2024

@author: Vaishnavi
"""
"""
Problem Statement:
This dataset contains information of users in a social network.
This social network has several business clients which can post ads on it.
One of theclients has a car company which has just launched a luxury SUV for a ridiculous price.
Build a BErnoulli Naive Bayes Model using this dataset and 
classify which of the users of the social network are going to purchase
this luxury SUV.1 implies that there was a purchase and 0 implies there wasnt a purchase.

1.Business Problem
1.1.What is the business objective?
    1.1.1 this will help you bring those audiences to your websites who are interested in cars.
    And,there will be many of those who are planning to buy a car in the near future.
    
    1.1.2 Communicating with your target audience over social media 
    is always a great way to build a good market reputation.
    Try responding to people's automobile related queries on Twitter and Facebook
    pages quickly to be their first choice when it comes to buying car.
    
1.2. Are there any constraints?
    Not having a clear marketing or social media strategy may result in reduced benefits for your business
    
    Additional resources may be needed to manage your online presence
    
    Social media is immediate and needs daily monitoring
    
    If you don't actively manage your social media presence,
    you may not see any real benefits
    
    There is a risk of unwanted or inappropriate behaviour on your site
    including bullying and harassment
    
    Greater exposure online has the potential to attract risks.
    Risks can include negative feedback information,leaks ,or hacking.
"""
#2.work on each feature of the dataset to create a data dictionary
#data dictionary
#user ID:integer type which is  not contributory
#Gender:Object Type need to be label encoding
#Age:integer
#EstimateSalary:Integer
#purchased:Integer type
##########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#let us first import the dataset
car=pd.read_csv("C:/11-KNN/NB_Car_Ad.csv") 

#Exploratory data analysis
car.columns
car.dtypes
car.describe()
#min age of employee is 18 years
#max age of employee is 60 years
#average salary is 69742
car.isna().sum()#this counts the number of null values presents in each column
car.isnull().sum()#this counts the number of null values presents in each column
car.drop(['User ID'],axis=1,inplace=True)
car.dtypes
plt.hist(car.Age)
#age is normally distributed
plt.hist(car.EstimatedSalary)
#Data is normally distributed but right skewed

########################
#Data Pre-processing
#3.1 Data cleaning,Feature Engineering ,etc.
car.dtypes

#the column gender is of object type
#let us apply label encoder to input features

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
#this is model of label_encoder which is applied to all the object type
car['Gender']=label_encoder.fit_transform(car['Gender'])

#now let us apply normalization function
def norm_funct(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
car_norm=norm_funct(car)
car_norm.describe()
########################################
#now let us designate train data and Test data

from sklearn.model_selection import train_test_split
car_train,car_test=train_test_split(car_norm,test_size=0.2)

col_names1=list(car_train.columns)
train_X=car_train[col_names1[0:2]]
train_y=car_train[col_names1[3]]
col_names2=list(car_train.columns)
test_X=car_test[col_names2[0:2]]
test_y=car_test[col_names2[3]]

##############################
##Model Building
#build the model on the scaled data (try multiple options)
#build a Naive Bayes model.
#Like MultinomialNB,this classifier is suitable for discrete data.
#BernoulliNB is designed for binary/boolean features.
from sklearn.naive_bayes import BernoulliNB as BB
classifier_bb=BB()

classifier_bb.fit(train_X,train_y)
#let us now evaluate on test data
test_pred_b=classifier_bb.predict(test_X)
##accuracy of the prediction
accuracy_test_b=np.mean(test_pred_b==test_y)
accuracy_test_b




