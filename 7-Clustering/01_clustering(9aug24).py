# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 08:29:48 2024

@author: Vaishnavi
"""
import pandas as pd
import matplotlib.pylab as plt
#now import file from dataset and create a dataframe
Univ1=pd.read_csv('C:/7-clustering/University_Clustering.csv')
a=Univ1.describe()
#we have one column  "state" which really not useful we will drop it
Univ=Univ1.drop(["State"],axis=1)
#we know that there is scale difference among the columns
#which we have to remove 
#either by using normalization or standardization
#whenever there is mixes data apply normalization
def norm_func(i):
    x=(i-i.min())/(i.max()-i.min())
    return x
#now apply this normalization function to univ dataframe
#for all the rows and columns from 1 until end
#since 0 th column has university namehhence skipped 

df_norm=norm_func(Univ.iloc[:,1:])




b=df_norm.describe()
#before you apply clustering,yo need to plot the dendrogram first 
#now to create dendrogram,we need to meansure distance,
#we have to import linkage
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#linkage function gives us hierarchical or agglomotive clustering
#ref the help for linkage
z=linkage(df_norm,method='complete',metric="euclidean")
plt.figure(figsize=(15,8));
plt.title("hierarchical clustering dendrogram");
plt.xlabel("Index");
plt.ylabel("Distance")
#ref help of dendrogram 
#sch.dendrogram(z)
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=10)
plt.show()
#dendogram
#applying agglomotive clustering choosing 5 as clusters from dendogram
#whatever has been displayed in dendrogram in not clustering
#it is just showing number of possible clusters
from sklearn.cluster import AgglomerativeClustering 
h_complete=AgglomerativeClustering(n_clusters=3,linkage='complete',metric="euclidean").fit(df_norm)
#apply labels to the clusters
h_complete.labels_
cluster_labels=pd.Series(h_complete.labels_)
#assign this series to univ dataframe as column and name the column 
Univ['clust']=cluster_labels
#we want to relocate the column 7 to 0
Univ1=Univ.iloc[:,[7,1,2,3,4,5,6]]
#now check the univ1 dataframe
Univ1.iloc[:,2:].groupby(Univ1.clust).mean()
#from the output cluster 2 has got highest top10

