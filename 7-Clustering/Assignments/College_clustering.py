# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 21:05:14 2024

@author: Vaishnavi
"""
#for engineering college cluster the colleges
#on the basis which will help the students 
#to get the admission into the colleges
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
df=pd.read_csv("C:/7-clustering/Eng_colleges.csv")
df
df.head()
df.describe()
plt.scatter(df.fess,df['rating'])
plt.xlabel('fees')
plt.ylabel('Ratings')

km=KMeans(n_clusters=3)
km
y_predicted=km.fit_predict(df[['fess','rating']])
y_predicted