# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 09:15:50 2024

@author: Vaishnavi
"""
import pandas as pd
df=pd.read_csv("C:/11-KNN/4_Decision_Tree/3_movies_classification.csv")
df.info()
#movies_classification dataset contains two columns  which are objecta
#hence convert into dummies
df=pd.get_dummies(df,columns=["3D_available","Genre"],drop_first=True)
#let us assign input and output variables
predictors=df.loc[:,df.columns!="Start_Tech_Oscar"]
#Except start_tech_oscar,rest all columns are assigned as predictors
#as that column is output or target columns
#predictor has got 20 columns
target=df["Start_Tech_Oscar"]
#########################################
#let us partition the dataset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(predictors,target,test_size=0.3)
################################
##model selection
from sklearn.ensemble import RandomForestClassifier
rand_for=RandomForestClassifier(n_estimators=500,n_jobs=1,random_state=42)
#n_estimators:It is number of trees in the forest ,always in range 500
#n_jobs=1 means number of jobs running parallel=1,if is -1 then multiple
#random_state=controls randomness in bootstrapping
#Bootstrapping is getting samples replaced
rand_for.fit(X_train,y_train)
pred_X_train=rand_for.predict(X_train)
pred_X_test=rand_for.predict(X_test)
#############3
#let us check the performance of themodel
from sklearn.metrics import accuracy_score,confusion_matrix
accuracy_score(pred_X_test,y_test)
confusion_matrix(pred_X_test,y_test)


####################
#for trainng dataset
accuracy_score(pred_X_train,y_train)
confusion_matrix(pred_X_train,y_train)
