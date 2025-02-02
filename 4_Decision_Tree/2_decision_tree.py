# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 09:27:41 2024

@author: Vaishnavi
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
data=pd.read_csv("C:/11-KNN/4_Decision_tree/salaries.csv")
##data prpartition
#check for null values
data.isnull().sum()
data.dropna()
data.columns
"""
Out[63]: Index(['company', 'job', 'degree', 'salary_more_than_100k'], dtype='object')
"""
lb=LabelEncoder()
data["company"]=lb.fit_transform(data["company"])
data["job"]=lb.fit_transform(data["job"])
data["degree"]=lb.fit_transform(data["degree"])
data["salary_more_than_100k"]=lb.fit_transform(data["salary_more_than_100k"])

#check for non-numeric columns
non_numeric_cols=data.select_dtypes(include=['object']).columns
print(non_numeric_cols)
data["company"]=lb.fit_transform(data["company"])
data["salary_more_than_100k"]=lb.fit_transform(data["salary_more_than_100k"])








