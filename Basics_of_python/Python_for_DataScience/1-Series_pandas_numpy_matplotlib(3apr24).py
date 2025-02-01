# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 08:14:53 2024

@author: Vaishnavi
"""
#creation
import pandas as pd
george= pd.Series([10,7,1,22],
index=['1968','1969','1970','1970'],
name='George_songs')

#deletion 
#the del statement apears to have 
#problems with duplicate index
s=pd.Series([2,3,4], index=[1,2,3])
del s[1]
s
#so it will delete the 1st postion value
###############################
#convert types
#string use.astype(str)
#numeric use pd.to_numeric
#integer use.astype(int),
#note that this will fail with NaN
#datetime use pd.to_datetime
songs_66=pd.Series([3.0,None,11.0,9.0],
index=['george','ringo','john','paul'],
name='counts')
songs_66.dtypes
#dtype is a property not a method
#method is ()function
#dtype will tell the type of data that 
#column will have
#####################################
#dtype('float64')
pd.to_numeric(songs_66.apply(str))
#here it come error as null value will be there and it not suppoerted by python 
pd.to_numeric(songs_66.astype(str),errors='coerce')
#here coerce will ignore the errors
#we can see it supports many formats
songs_66.dtypes


#the .fillna mwthod will replace them a given value
songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='counts')
songs_66.dtypes
songs_66
songs_66=songs_66.fillna(-1)
#here we need to give the handle to any of the variable otherwise it would be stored for temporary
songs_66=songs_66.astype(int)
songs_66.dtypes
songs_66

#######################################
#drop the null values
songs_66=pd.Series([3,None,11,9],
index=['george','ringo','john','paul'],
name='counts')
songs_66=songs_66.dropna()
songs_66
####################################
#append,combining,and joining two series
#it will append vertically
songs_69=pd.Series([7,26,21,39],#values in the column
index=['ram','sham','ghanshyam','krishna'],#index names
name='counts')#the name of the column
songs=songs_66.append(songs_69)
#it doesnt support on new version so go on stackoverflow and search the alternative for it
######################################
songs_69=pd.Series([7,16,21,39],#values in the column
index=['ram','sham','ghanshyam','krishna'],#index names
name='counts')#the name of the column
songs=pd.concat([songs_66,songs_69])
#here it is necessary to give the handle
songs
#########################################
#as :it is aliasing (instead of using the whole big name use a small name)
#plotting series
import matplotlib.pyplot as plt
#line graph
#so here in matplotlib module there is a package pyplot
fig=plt.figure()
songs_69.plot()
plt.legend()
#######################
#bargraph
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
#here the latest was songs_66 so bar graph names will be of songs_66
plt.legend()
"""<matplotlib.legend.Legend at 0x2c191f43950>
"""
#this is the object created we will see it in o/p
################################
#histograph
#gaussian distribution
import numpy as np
data=pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()



