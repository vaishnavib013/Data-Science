# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 08:32:43 2024

@author: Vaishnavi
"""

#31/07/2024
import pandas as pd
#let us import dataset
df=pd.read_csv("C:/5-Data_prep/ethnic_diversity.csv")
#lets check the data types of the column
df.dtypes
#salaries datatype is float,let us convert into int
#df1=df.Salaries.astype(int)
df.Salaries=df.Salaries.astype(int)
df.dtypes
#now the data type of salaries is int
#similarly age data type must be float
#presently it is int
df.age=df.age.astype(float)
df.dtypes
#####################33333333
#identify two duplicates
df_new=pd.read_csv("C:/5-Data_prep/education.csv")
duplicate=df_new.duplicated()
#output of this function is single column
#if there are duplicate records output-True
#if no duplicate records output -False
#series will be created
duplicate
sum(duplicate)
#output=0
#now let us import another dataset
df_new1=pd.read_csv("C:/5-Data_prep/mtcars_dup.csv")
duplicate1=df_new1.duplicated()
duplicate1
sum(duplicate1)
#there are 3 duplicate records
#row 17 is duplicate of row 2 like wise you can 3 duplicate
#records
#there is function called drop_duplicates()
#which will drop all the duplicate records
df_new2=df_new1.drop_duplicates()
duplicate2=df_new2.duplicated()
duplicate2
sum(duplicate2)
#Out[25]: 0
##############################
#outlier treatment
import pandas as pd
import seaborn as sns
df=pd.read_csv("C:/5-Data_prep/ethnic_diversity.csv")
#now lets find the outliers in salaries
sns.boxplot(df.Salaries)
#there are outliers
#let us check outliers in age column
sns.boxplot(df.age)
#there are no outliers
#let us calculate IQR(Q3-Q1)
IQR=df.Salaries.quantile(0.75)-df.Salaries.quantile(0.25)
#have observed IQR in variable explorer
#no,because IQR is in capital letters
#treated as constant
IQR

#but if we will try as I..,IQR then it is showing
lower_limit=df.Salaries.quantile(0.25)-1.5*IQR
upper_limit=df.Salaries.quantile(0.25)-1.5*IQR
#now if you will check the lower limit of salary,it is -19446.9675
#there is a negative salary
#so make it as 0
#how to make it
#go to variable explorer and make it 0
############################3333
#trimming
import numpy as np
import seaborn as sns
outliers_df=np.where(df.Salaries>upper_limit,True,
                     np.where(df.Salaries<lower_limit,True,False))
#you cancheck outlief_df column in variable explorer
df_trimmed=df.loc[~outliers_df]

df.shape
#o/p: (310, 13)
df_trimmed.shape
#Out[19]: (0, 13)
sns.boxplot(df_trimmed.Salaries)

#################################
#replacement technique
#drawback of trimming technique is we are losing the data
df=pd.read_csv("C:/5-Data_prep/ethnic_diversity.csv")
df.describe()
#record no.23 has got outliers
#map all the outlier values to upper limit
df_replaced=pd.DataFrame(np.where(df.Salaries>upper_limit,
                                  upper_limit,np.where(df.Salaries<lower_limit,lower_limit,df.Salaries)))
#if the values are greater than upper_limit
#map it to the upper limit,and less than lower limit
#map it to lower_limit,if it is within the range
#then keep as it is
sns.boxplot(df_replaced[0])
###########################
#Winsorizer
from feature_engine.outliers import Winsorizer
winsor=Winsorizer(capping_method='iqr',
                  tail='both',
                  fold=1.5,
                  varables=['Salaries']
                  )
#copy winsorizer and paste in help tab of  top right window ,study the method
df_t=winsor.fit_transform(df[['Salaries']])
sns.boxplot(df['Salaries'])
sns.boxplot(df_t['Salaries'])
###############################
#zero variance and near zero variance
#features
import pandas as pd
df=pd.read_csv("C:/5-Data_prep/ethnic_diversity.csv")
df.var()#error
df.var()==0
#check the number of columns
df.shape
df.info()

df.Salaries.var()==0#Out[38]: False
df.EmpID.var()==0#Out[38]: False
df.Zip.var()==0#Out[38]: False
df.age.var()==0#Out[38]: False

df.var(axis=0)==0
###########################
import pandas as pd
import numpy as np
df=pd.read_csv("c:/5-Data_prep/modified_ethnic.csv")
#check for null values
df.isna().sum()
####################
#create an imputer that creates NaN values
#mean and median is used for numeric data
#mode is used for discrete data(position,sex,MaritalDes)
from sklearn.impute import SimpleImputer
mean_imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
#check the dataframe
df['Salaries']=pd.DataFrame(mean_imputer.fit_transform(df[['Salaries']]))
#check the dataframe
df['Salaries'].isna().sum()
#Out[48]: 0

#median imputer
median_imputer=SimpleImputer(missing_values=np.nan,strategy='median')
#check the dataframe
df['age']=pd.DataFrame(mean_imputer.fit_transform(df[['age']]))
df['age'].isna().sum()
#Out[53]: 0

################
#mode imputwr
mode_imputer=SimpleImputer(missing_values=np.nan,strategy='most_frequent')
#check the dataframe
df['Sex']=pd.DataFrame(mode_imputer.fit_transform(df[['Sex']]))
df['Sex'].isna().sum()
#Out[54]: 0
df['MaritalDesc']=pd.DataFrame(mode_imputer.fit_transform(df[['MaritalDesc']]))
df['MaritalDesc'].isna().sum()
#Out[54]: 0)

######################
#pip install imbalanced-learn scikit-learn
import numpy as np
from sklearn.datasets import make_classification
from imblearn.over_sampling import SMOTE

#step1:generate an imbalanced dataset

X,y=make_classification(n_samples=1000,n_features=20,
                        n_informative=2,n_redundant=10,
                        n_clusters_per_class=1,weights=[0.99],
                        flip_y=0,random_state=1)
"""
n_samples=1000:
    the total number of samples (datapoints) to generate.
    here,1000 samples will be created
    
n_features=20:
    the total number of features (columns) in the dataset
    each sample will have 20 features
    
informative=2:
    the number of informtive features
    these features 
    
    are generated 
    """
#sshow the original class distribution
print("original class distribution:",np.bincount(y))
#o/p:
#original class distribution: [990  10]


#step2:apply smote to balance the dataset
smote=SMOTE(random_state=42)
X_res,y_res=smote.fit_resample(X,y)

#show the new class distribution after applying SMOTE
print("REsampled class distribution:",np.bincount(y_res))
#o/p:REsampled class distribution: [990 990]

############################3
#05-08-2024
#show the original class distribtion 
print(f"original class distribution:{np.bincount(y)}")
#o/p:original class distribution:[990  10]


from sklearn.model_selection import train_test_split
#step 2:split the data into training and testing sets
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
#out of 100 yoou are reserving the 30%datapoints for testing and 70%datapoints for training
#random_state you can change at whatever u will get good accuracy choice that point 
#not necessary to take 42 for it you can change but u will get different solution


#step 3:apply smote to balance the training datasets
smote=SMOTE(random_state=42)
X_train_res,y_train_res=smote.fit_resample(X_train,y_train)

#show the new class distribution after applying SMOTE
print(f"RESampled class distribution:{np.bincount(y_train_res)}")
#o/p:RESampled class distribution:[693 693]
#so here the solution is different because we have applied the smote

#step4:train  a classifier on the balanced dataset
from sklearn.ensemble import RandomForestClassifier
clf=RandomForestClassifier(random_state=42)
clf.fit(X_train_res,y_train_res)
#Out[19]: RandomForestClassifier(random_state=42)

#step5:evaluate the classifier on the test set
y_pred=clf.predict(X_test)



######################################
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#generate a sample dataset
np.random.seed(0)
data=np.random.exponential(scale=2.0,size=1000)
df=pd.DataFrame(data,columns=['Value'])

#perform log transformation
df['logValue']=np.log(df['Value'])

#plot the original and log_transformed data
fig,axes=plt.subplots(1,2,figsize=(12,6))

#original data
axes[0].hist(df['Value'],bins=30,color='blue',alpha=0.7)
axes[0].set_title('original Data')#Out[33]: Text(0.5, 1.0, 'original Data')
axes[0].set_xlabel('Value')#Out[34]: Text(0.5, 36.72222222222221, 'Value')
axes[0].set_ylabel('Frequency')#Out[35]: Text(108.09722222222221, 0.5, 'Frequency')

#log tranformed data 
axes[1].hist(df['LogValue'],bins=30,color='green',alpha=0.7)
axes[1].set_title('Log-transformed Data')
axes[1].set_xlabel('Log(Value)')
axes[1].set_ylabel('Frequency')

plt.tight_layout()
plt.show()