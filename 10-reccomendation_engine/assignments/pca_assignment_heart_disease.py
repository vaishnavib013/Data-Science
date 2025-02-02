# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:57:53 2024

@author: Vaishnavi
"""
import pandas as pd
import seaborn as sns
df=pd.read_csv('C:/10-reccomendation_engine/assignments/heart_disease.csv')
df.head()
"""Out[159]: 
   age  sex  cp  trestbps  chol  fbs  ...  exang  oldpeak  slope  ca  thal  target
0   63    1   3       145   233    1  ...      0      2.3      0   0     1       1
1   37    1   2       130   250    0  ...      0      3.5      0   0     2       1
2   41    0   1       130   204    0  ...      0      1.4      2   0     2       1
3   56    1   1       120   236    0  ...      0      0.8      2   0     2       1
4   57    0   0       120   354    0  ...      1      0.6      2   0     2       1

[5 rows x 14 columns]"""
df.shape
df.dtypes
df.columns
df.isnull().sum()
#plot the boxbox to check the outliers
sns.boxplot(df[['age','sex','cp','trestbps','chol']])
sns.boxplot(df[['restecg', 'thalach', 'exang','oldpeak', 'slope', 'ca','thal','target']])
#so in some of them outliers are there

def remove_out(df, columns):
    for col in columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        #Remove outliers
        df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]

    return df

outliers_columns=['trestbps','chol','fbs','thalach','oldpeak','ca','thal']
df= remove_out(df,outliers_columns)
df

#normalize the data
from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
df_scaled=scaler.fit_transform(df)
df_scaled=pd.DataFrame(df_scaled, columns=df.columns)
sns.boxplot(df_scaled)





