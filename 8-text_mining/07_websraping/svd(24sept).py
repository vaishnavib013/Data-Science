# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:31:58 2024

@author: Vaishnavi
"""
import pandas as pd
import numpy as np
#Univ1=pd.read_excel("D:/University_Clustering.xlsx")
Univ1=pd.read_csv("C:/9-PCA_SVD/University_CLustering.csv")
Univ1.describe()
Univ1.info()
Univ=Univ1.drop(["State"],axis=1)
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
Univ.data=Univ.iloc[:,1:]
#normalizing numerical data
uni_normal=scale(Univ.data)
uni_normal
pca=PCA(n_components=6)
pca_values=pca.fit_transform(uni_normal)
var=pca.explained_variance_ratio_
var
#PCA Weights
pca.components_
pca.components_[0]
#to check the cumulative variance
var1=np.cumsum(np.round(var,decimals=4)*100)
var1

"""Association rule in data mining -next topic going

It is about the arranging the racks related eg;milk buying person will buy tea 
and coffee so keep in same rack in mall by studying the history.
in kirana shopee or also in malls to increase the sells and also helps to apply offers there.

here datascience will be used 
Also on flipcart,if we buy something it suggest us relTED items using BAsket market analysis


"""















