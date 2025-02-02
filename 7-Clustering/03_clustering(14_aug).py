# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 08:25:35 2024

@author: Vaishnavi
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
#let us try to understand first how k means work for 2 dimensional data
#for that,generate random numbers in the raange 0 to 1
#and with uniform probability of 1/50
X=np.random.uniform(0,1,50)
Y=np.random.uniform(0,1,50)
#create a empty dataframe with 0 rows and 2 columns
df_xy=pd.DataFrame(columns=["X","Y"])
#assign the values X andY   to these columns
df_xy.X=X
df_xy.Y=Y
df_xy.plot(x="X",y="Y",kind="scatter")
model1=KMeans(n_clusters=3).fit(df_xy)
"""with X and Y data ,apply KMeans model,
generate scatter plot with scale/font=10
cmap=plt.cm.coolwarm:cool color combination"""
model1.labels_#these are all the data points that we are going to plot just in the below

df_xy.plot(x="X",y="Y",c=model1.labels_,kind="scatter",s=10,
           cmap=plt.cm.coolwarm)
#s=10 is the 
#coolwarm is the ploting type kind of filter having 3 colors
#through which we have any color combination

###############################
#Univ1=pd.read_excel("C:/7-clustering/University_clustering.xlsx")

Univ1=pd.read_csv("C:/7-clustering/University_clustering.csv")
Univ1.describe()
Univ=Univ1.drop(['State'],axis=1)
#we know that there is scale difference among the columns ,whixh we have 
#either by using normalization or standardization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization function to univ dataframe for all the 

df_norm=norm_func(Univ.iloc[:,1:])
"""what will be ideal cluster number,will it be 1,2 or 3"""

TWSS=[]
k=list(range(2,8))
for i in k:
    kmeans=KMeans(n_clusters=i)
    kmeans.fit(df_norm)
    TWSS.append(kmeans.inertia_)
    #total within sun of square
    
"""KMeans inertia ,also known as SUm ofSquare Errors(or SSE),
calculate the sum of the distances
of all the points within a cluster from the centroid of the point.It isthe differnece 
between the observed value and the predicted value"""
TWSS
#as k value increases the TWSS value decreases
plt.plot(k,TWSS,'ro-');
plt.xlabel("No_of_clusters")
plt.ylabel("Total_within_SS")

"""how to select value of k from the elbow curve
when k changes from 2 to 3,then decrease in twss is higher than 
when k changes from 3 to 4
when k values changes from 5 to 6 decrease
"""
model=KMeans(n_clusters=3)
model.fit(df_norm)
model.labels_
mb=pd.Series(model.labels_)
Univ['clust']=mb
Univ.head()
Univ=Univ.iloc[:,[7,0,1,2,3,4,5,6]]
Univ
Univ.iloc[:,2:8].groupby(Univ.clust).mean()

Univ.to_csv("kmeans_University.csv",encoding="utf-8")
import os
os.getcwd()








