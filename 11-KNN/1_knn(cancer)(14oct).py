# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 08:31:24 2024

@author: Vaishnavi
"""
import pandas as pd
import numpy as np

wbcd=pd.read_csv("C:/11-KNN/1_wbcd.csv")
#there are 569 rows and 12 columns
wbcd.describe()
#in output column there is only 8 for BAnien and M for Malignant
#let us first convert it asBenign and Malignant
#Benign =A noncancerous ,Malignant=A cancerous
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='B','Beniegn',wbcd['diagnosis'])
#in wbcd there is column named 'diagnosis' where ever there is 'B' replace by Benign'
#similarly where ever there m in the same column   replace it by Malignant
wbcd['diagnosis']=np.where(wbcd['diagnosis']=='M','MAlignant',wbcd['diagnosis'])
##################################
#0 the column is patient ID let us drop it
wbcd=wbcd.iloc[:,1:32]
#######################3333333
#normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now let us apply this function to the dataframe
wbcd_n=norm_func(wbcd.iloc[:,1:32])
#because now 0 th column is output or label it is not considered hence 1:all
######################
#let us now apply X as input and y as output
X=np.array(wbcd_n.iloc[:,:])
##since in wbcd_n,we are already excluding output column,hence all rows and
y=np.array(wbcd['diagnosis'])
#############################
#now let us split the data into training and testing
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

#here you are passing X,y instead dataframe handle
#there could chances of unbalancing on data
#let us assume you have 100 datapoints ,out of which 80 NC and 20 cancer
#these datapoints must be equally distributed
#there is statified sampling concept is used
from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=21)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
pred
#now let us evaluate the model
from sklearn.metrics import accuracy_score
print(accuracy_score(pred,y_test))
pd.crosstab(pred,y_test)
#let us check the aplicablity of the model
#ie.miss classification ,Acutal patient is malignant
#ie cancer patient but predicted is Benien is 1
#actual patient is benien and predicted as cancer patient is 5
#hence this model is not acceptable
###########################33
##let us try to select correct value of k
acc=[]
#running KNN algorithm for k=3 to 50 in the step of 2
#k value selected is odd value
for i in range(3,50,2):
    #declare the model
    neigh=KNeighborsClassifier(n_neighbors=i)
    neigh.fit(X_train,y_train)
    train_acc=np.mean(neigh.predict(X_train)==y_train)
    test_acc=np.mean(neigh.predict(X_test)==y_test)
    acc.append([train_acc,test_acc])
#if you will see the acc ,it has got two accuracy,i[0]-train_acc
#i[1]=test_acc
#to plot the graph of train_acc and test_acc
import matplotlib.pyplot as plt
plt.plot(np.arange(3,50,2),[i[0] for i in acc],"ro-")
plt.plot(np.arange(3,50,2),[i[1] for i in acc],"bo-")
#there are 3,5,7 and 9 are possible values where accuracy is good
#let us check for k=3
knn=KNeighborsClassifier(n_neighbors=9)
knn.fit(X_train,y_train)
pred=knn.predict(X_test)
accuracy_score(pred,y_test)
pd.crosstab(pred,y_test)
#ie miss classification ,acutal patient is malignant
