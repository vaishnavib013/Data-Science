# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 08:36:40 2025

@author: Vaishnavi
"""
import pandas as pd
import numpy as np
letters=pd.read_csv("D:/15-Logistic_Regression/letterdata.csv")
'''
dataset is typically used for handwritten character recognition or related machine learning and numerical recognition

letter:represents the target class:These are numeric attributes
describing various geometrical or statistical properties of the characters.
xbox and ybox:X and Y are bounding box dimensions.
width and height :of character's bounding box
This is having numerical information about the '''

#let us carry out EDA
a=letters.describe()
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
train,test=train_test_split(letters,test_size=0.2)
#Let us split the data in terms of X and Y for both train and test data
train_X=train.iloc[:,1:]
train_y=train.iloc[:,0]
test_X=test.iloc[:,1:]
test_y=test.iloc[:,0]
#Kernel linear 
model_linear=SVC(kernel="linear")
model_linear.fit(train_X,train_y)
pred_test_linear=model_linear.predict(test_X)
pred_test_linear
#now let us check the accuracy=0.85675
#now let us check the acuracy
np.mean(pred_test_linear==test_y)
#Out[36]: 0.852
#Kernel rbf
#Kernel linear 
model_rbf=SVC(kernel="rbf")
model_rbf.fit(train_X,train_y)
pred_test_rbf=model_rbf.predict(test_X)
#now letus check the accuracy =0.92275
#now let us check the acuracy
np.mean(pred_test_rbf==test_y)
#Out[37]: 0.924