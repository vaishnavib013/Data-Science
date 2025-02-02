# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 22:34:40 2024

@author: Vaishnavi

1. Business Problem 
1.1.	What is the business objective?
1.2.	Are there any constraints?

2. Work on each feature of the dataset to create a data dictionary as displayed in the below image:
 

3. Exploratory Data Analysis (EDA):
      4.1. Summary.
      4.2. Univariate analysis.
      4.3. Bivariate analysis.
4. Data Pre-processing 
3.1 Data Cleaning, Feature Engineering, etc.

5. Model Building 
5.1 Build the model on the scaled data (try multiple options).
5.2 Perform K- means clustering and obtain optimum number of clusters using scree plot.
5.3 Validate the clusters (try with different number of clusters) – label the clusters and derive insights (compare the results from multiple approaches).
6. Write about the benefits/impact of the solution - in what way does the business (client) benefit from the solution provided? 

"""
"""
1.	Perform K means clustering on the airlines
 dataset to obtain optimum number of clusters.
 Draw the inferences from the clusters 
 obtained. Refer to EastWestAirlines.xlsx 
 dataset.
"""
import pandas as pd
import numpy as np
import seaborn as sns 
import matplotlib.pyplot as plt

df=pd.read_csv("C:/7-clustering/Assignments/EastWestAirlines.csv")
df.head()#first read the file
#observe the first 5 rows
df.shape
df.columns#check for all the columns 
df['Award?'].value_counts()#checking for what kind of data it has
df['Days_since_enroll'].value_counts()
df.describe()

"""
Index(['ID#', 'Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'Days_since_enroll', 'Award?'],
      dtype='object')
Out[10]:
               ID#       Balance  ...  Days_since_enroll       Award?
count  3999.000000  3.999000e+03  ...         3999.00000  3999.000000
mean   2014.819455  7.360133e+04  ...         4118.55939     0.370343
std    1160.764358  1.007757e+05  ...         2065.13454     0.482957
min       1.000000  0.000000e+00  ...            2.00000     0.000000
25%    1010.500000  1.852750e+04  ...         2330.00000     0.000000
50%    2016.000000  4.309700e+04  ...         4096.00000     0.000000
75%    3020.500000  9.240400e+04  ...         5790.50000     1.000000
max    4021.000000  1.704838e+06  ...         8296.00000     1.000000

[8 rows x 12 columns]"""

df.isna().sum()
#lets check whether the given data has how many null values
"""Out[8]: 
ID#                  0
Balance              0
Qual_miles           0
cc1_miles            0
cc2_miles            0
cc3_miles            0
Bonus_miles          0
Bonus_trans          0
Flight_miles_12mo    0
Flight_trans_12      0
Days_since_enroll    0
Award?               0
dtype: int64"""


from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

km=KMeans(n_clusters=3)
km
y_predicted=km.fit_predict(df[["Balance","Bonus_miles","Bonus_trans","Flight_miles_12mo","Flight_trans_12","Days_since_enroll","Award?"]])
y_predicted
df['clusters']=y_predicted
df.head(10)
km.cluster_centers_



features = ["Balance", "Bonus_miles", "Bonus_trans", "Flight_miles_12mo", "Flight_trans_12"]
#df = df.dropna(subset=features)

# Standardize the features
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df = scaler.fit_transform(df[features])

df1=df[df.clusters==0]
df2=df[df.clusters==1]
df3=df[df.clusters==2]

plt.scatter(df1.Balance,df1["Bonus"],color='green')
plt.scatter(df2.Balance,df2["Bonus"],color="red")
plt.scatter(df3.Balance,df3["Bonus"],color="blue")
plt.scatter(km.cluster_centers_[:,0],km.cluster_centers_[:,1],color='purple',marker='*',label='centroid')
plt.legend()
