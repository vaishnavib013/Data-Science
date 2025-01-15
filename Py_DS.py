# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 08:45:26 2024

@author: Vaishnavi

--------------------------------------------------------
-----------------'''02/04/2024'''-----------------------
--------------------------------------------------------
"""
#A series is used to model one dimensional data,
#similar to a list in python
#a series object also has a few more bits
#of data,including index and name

import pandas as pd
songs2=pd.Series([145,142,18,13],name='counts')
#it is easy to inspect index of a series
songs2.index
#the indexing can be string based
#indexing can be any type
import pandas as pd
songs3=pd.Series([145,142,18,13],name='counts',index=['paul','john','George','Ringo'])
songs3.index
songs3

#Null Values
#This value stands for not a value
#and is usually ignored in arithmatic operation
#Empty space in columns of values is Nan value


import pandas as pd
f1=pd.read_csv('age.csv')
f1

#A series object behaves similarly to numpy arrays
import numpy as np
numpy_ser=np.array([145,142,18,13])
songs3[1]
#142
numpy_ser[1]
#They both have methods in common
songs3.mean()
numpy_ser.mean()

#The pandas Series data structure provides support for
#basic Crud = create , read ,update ,delete

george=pd.Series([10,7,1,22],
index=['1968','1969','1970',1970],name='George_Songs')
george
george[1970]
george['1970']

#we can iterate over data in a series as well ,
#when iterting over series
for item in george:
    print(item)
    
george['1969']=68
george['1969']
george

-------------------------------------------------------
--------------------"03/04/2024"----------------------
-------------------------------------------------------
#deletion
#the del statement appears to have problems with 
#duplicate index
import pandas as pd
s=pd.Series([2,3,4],index=[1,2,3])
del s[1]
s

songs_66=pd.Series([3.0,None,11.0,0.0],
                   index=['George','Ringo','John','Paul'],name='Counts')
songs_66.dtypes

pd.to_numeric(songs_66.apply(str))#error

#if we pass errors='coerce'
#we can see that it support many formats
pd.to_numeric(songs_66.astype(str),errors='coerce')
songs_66.dtypes

#Dealing with none
#the fillna method will replace them with given value
songs_66=songs_66.fillna(-1)
songs_66=songs_66.astype(int)
songs_66.dtypes

#Nan values can be dropped from the series using .dropna
songs_66=songs_66.dropna()
songs_66
####################################################

#Append ,combining and joinning two series
songs_69=pd.Series([7,16,21,39],
index=["Ram","Sham","Ghansham","Krishna"],name="Counts")
pd.concat([songs_66,songs_69])
songs=songs_66.append(songs_66)

###################################################
#Plotting of Series
import matplotlib.pyplot as plt
fig=plt.figure()
songs_66.plot()
plt.legend()

#Bar plot
fig=plt.figure()
songs_69.plot(kind='bar')
songs_66.plot(kind='bar',color='r')
plt.legend()

#######################################################
#Histogram
import numpy as np
data=pd.Series(np.random.randn(500),name='500_random')
fig=plt.figure()
ax=fig.add_subplot(111)
data.hist()
------------------------------------------------------
-------------------"04/04/2024"-----------------------
------------------------------------------------------
import pandas as pd
pd.__version__

import pandas as pd
tech=[["Spark",2000,"30days"],
      ["pandas",20000,"30days"]]
df=pd.DataFrame(tech)
print(df)

column_names=["Courses","Fee","Duration"]
row_label=["a","b"]
df=pd.DataFrame(tech,columns=column_names,index=row_label)
print(df)

df.dtypes

#we can give custom datatypes


import pandas as pd
tech={
      "Course":["Spark","Pyspark","Hadoop","Python","Pandas","Oracle","Java"],
      "Fee":[20000,30000,20000,25000,33000,35000,19000],
      "Duration":['30days','40days','35days','40days','60days','50days','55days'],
      "Discount":[11.8,23.7,21.4,45.3,55.0,12.0,13.4]}
df=pd.DataFrame(tech)
df
df.dtypes
#Convert all types to best possible type
df2=df.convert_dtypes()
print(df2.dtypes)
#change all colums to same type
df=df.astype(str)
print(df.dtypes)
#change type for one or multiple column
df=df.astype[{'Fee':int,'Discount':float}]
print(df.dtypes)
#convert data type for all columns in a list
df=pd.DataFrame(tech)
df.dtypes
cols=['Fee','Discount']
df[cols]=df[cols].astype('float')
df.dtypes
#Ignores error
df.astype({"Course":int},errors='ignore')
df.dtypes
#Generates Error
df.astype({"Course":int},errors='raise')
df.dtypes  
#converts feed column to numeric type
df=df.astype(str)
print(df.dtypes)
df["Discount"]=pd.to_numeric(df["Discount"])
df.dtypes
#################################################
#convert dataframe to csv
df.to_csv("Technology.csv")

df=pd.read_csv('Technology.csv')
df

####################################################
#pandas dataframe - basic operation
#create dataframe with null/emptytowork with example
import pandas as pd
import numpy as np
tech={
      "Course":["Spark","Pyspark",None,"Python","Pandas","Oracle","Java"],
      "Fee":[20000,30000,20000,np.nan,33000,35000,19000],
      "Duration":['30days','40days','35days','40days','60days','50days','55days'],
      "Discount":[11.8,23.7,21.4,45.3,55.0,12.0,13.4]}
row_name=['a','b','c','d','e','f','g']
df=pd.DataFrame(tech,index=row_name)
print(df)
df.dtypes

------------------------------------------------------
-------------------"05/04/2024"-----------------------
------------------------------------------------------


#DataFrame properties
df.shape   #(7, 4)
df.size     #28
df.columns
df.columns.values
df.index
df.dtypes
df.info

#Accessing one column contents
df['Fee']
#Accessing two column contents
df[['Fee','Duration']]
cols=['Fee','Duration']
df[cols]

#Select certain rows and assign it to another DataFrame
df2=df[3:]
df2
df2=df[:3]
df2

#Accessing certain cell from a clumn

df['Duration'][3]   #40days

#Substracting specific value from column

df['Fee']=df['Fee'] - 500
df['Fee']

#Pandas to manipulate datframe
#Describe Dtaframe
#describe dataframe for all numeric columns
df.describe()
#It will give 5 number summary
###########################################

#rename()-renames Pandad Dtaframe columns
df=pd.DataFrame(tech,index=row_name)
#Assign new header by setting new column names
df.columns=['A','B','C','D']
df
####################################################
#Rename column name using rename() method
df=pd.DataFrame(tech,index=row_name)
df.columns=['A','B','C','D']
df2=df.rename({'A':'c1','B':'c2'},axis=1)
df2=df.rename({'C':'c3','D':'c4'},axis='columns')
df2=df.rename(columns={'A':'c1','B':'c2'})
df2

#Drop rows by labels
df1=df.drop(['r1','r2'])
df1

#Delete Rows by position index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#Delete Rows by Index range
df1=df.drop(df.index[2:])
df1

#When you have default indexes for rows
df=pd.DataFrame(tech)
df1=df.drop(0)
df1
df=pd.DataFrame(tech)
df1=df.drop([0,3],axis=0) #it will delete row 0 & 3
df1
df1=df.drop(range(0,2)) #it will delte 1 & 0
df1

------------------------------------------------------
---------------------"10-04-2-24"--------------------
---------------------------------------------------
#explicitely using wrong name 'labels'
df2=df.drop(labels=["Fee"],axis=1)
print(df2)

#Alternarively you can also use columns instead of
#labels
df2=df.drop(columns=["Fee"],axis=1)
df2
#Drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(tech)

#using inplace True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)

#Drop two or more columns by label name
df2=df.drop(["Course","Fee"],axis=1)
print(df2)

#Drop two or more columns by index
df=pd.DataFrame(tech)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)

#Drop Columns from list of Columns
df=pd.DataFrame(tech)
df.columns
liscol=["Course","Fee"] 
df2=df.drop(liscol,axis=1)
print(df2)

#Remove columns from DataFrame inplace
df.drop(df.columns[1],axis=1,inplace=True)
df
#using inplace =True


####################################################
#Pandas Select Rows by index (Position/Label)use of
#iloc
import pandas as pd
import numpy as np
tech={
      "Course":["Spark","Pyspark",None,"Python","Pandas","Oracle","Java"],
      "Fee":[20000,30000,20000,np.nan,33000,35000,19000],
      "Duration":['30days','40days','35days','40days','60days','50days','55days'],
      "Discount":[11.8,23.7,21.4,45.3,55.0,12.0,13.4]}
row_name=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(tech,index=row_name)
print(df)

#df.iloc[startrow:endrow,startcolumn:endcolumn]

df=pd.DataFrame(tech,index=row_name)

#For all rows and two columns
df2=df.iloc[:,0:2]
df2
#For two columns and all rows
df2=df.iloc[0:2,:]
df2

#this line uses slicing operator to get Dtaframe items
#by index
#The first slice indicates to return all rows,the second
#slice specifies only columns


#Slicing specific rows and columns using iloc attributes

df2=df.iloc[1:2,0:2]
df2

#Select rows by integer index
df2=df.iloc[2] #Select row by index
df2


df2=df.iloc[[2,3,6]]
df2=df.iloc[1:5]      #Select rows by integer index range
df2=df.iloc[:1]       #select first row
df2=df.iloc[:3]       #Select first three rows 
df2=df.iloc[-1:]      #Select last row 
df2=df.iloc[-3:]      #Select last three rows
df2=df.iloc[::2]      #Selects alternate rows
------------------------------------------------------------------
--------------------------"12/04/2024"-------------------------
------------------------------------------------------------------


#Select rows by index label
df2=df.loc['r1']                #Select row by label
df2=df.loc[['r2','r3','r6']]
df2
df2=df.loc['r1':'r5']
df2
df2=df.loc['r1':'r5':2]
df2

###################################################################
#Accessing columns by column name or index
#By using df[] notation
df2=df['Fee']
df2
#Select muktiple columns
df2=df[['Fee','Course','Discount']]
df2

#using loc to take columns slices
#loc[] syntax to slice columns
#df.loc[:,start:stop:step]
#select multiple columns
df2=df.loc[:["Course","Fee","Duration"]]
df2
#Select random columns
df2=df.loc[:["Course","Fee","Duration"]]
#Select columns between two columns
df2=df.loc[:,"Fee":"Discount"]
df2
#Select column by range
df2=df.loc[:,'Duration']
df2
df2=df.loc[:,'Duration':]
df2
df2=df.loc[:,::2] #select alternate columns
df2
##################################################################
#Pandas .DataFrame.query() by example
#Query all rows with courses equal 'Spark'

df2=df.query("Course=='Spark'")
print(df2)
df2=df.query("Course!='Spark'")
print(df2)

##########################################################
#Pandas add new column to dataframe

tutors=['Ram','Sham','Ghansham','Ganesh','Ramesh','Suresh','Kumar']
df2=df.assign(TutorAssigned=tutors)
print(df2)

########################################
#Add multiple columns to Dataframe
Companies=['Hcl','Infosys','Accenture','Tcs','Capgemini','AppliedAi','Benchmark']
df2=df.assign(Mnc=Companies,Tutor=tutors)
print(df2)

#######################################
#Derive new column from  existing column
df=pd.DataFrame(tech)
df2=df.assign(Discount_percent=lambda x:x.Fee * x.Discount /100)
print(df2)

#######################################
#Append column to existing pandas DataFrame

df["MNC Companies"]=Companies
print(df)

#########################################
#Add new column add specific Loaction
df.insert(0,'Tutors',tutors)
df

##########################################
#Rename multilple column df.rename

df.rename(columns={'Fee':'Fees','Course':'Courses','Duration':'Time'},inplace=True)
df.columns

------------------------------------------------------------------
--------------------"15/04/2024"------------------------------
--------------------------------------------------------------------

#Quick examples of get the number of rows in DataFrame

row_count=len(df.index)
row_count
row_count=len(df.axes[0])
row_count
columns_count=len(df.axes[1])
columns_count

#########################################################
row_count=df.shape[0]
row_count
column_count=df.shape[1]
column_count

#############################################################
#Pandas apply function to a column
#using DataFrame.apply()to apply function add colunmn
import pandas as pd
import numpy as np
data={
      "A":[1,2,3],
      "B":[4,5,6],
      "C":[6,7,8]}
df=pd.DataFrame(data)
df
print(data)

def add_3(x):
    return x+3
df2=df.apply(add_3)
df2

###########################
#using apply function onsingle column
def add_3(x):
    return x+3
df["B"]=df["B"].apply(add_3)
df["B"]
df[['B','C']]=df[['B','C']].apply(add_3)
df

#apply lambda function to each column
df2=df.apply(lambda x:x+10)
df2

df=df.transform(add_3)
df
#######################################################
#using pandas Dataframe.map( ) to single column
df['A']=df['A'].map( lambda A:A/2)
print(df)

#######################################################
#using numpy function on single column
#using datframe.apply() & '[]operator
df['A']=df['A'].apply(np.square)
print(df)

df['A']=np.square(df['A'])
print(df)

###################################################
#use group by to compute the sum
import pandas as pd
import numpy as np
tech={
      "Course":["Pandas","Pyspark",None,"Pyspark","Pandas","Oracle","Java"],
      "Fee":[20000,30000,20000,np.nan,33000,35000,19000],
      "Duration":['30days','40days','35days','40days','60days','50days','55days'],
      "Discount":[11.8,23.7,21.4,45.3,55.0,12.0,13.4]}
row_name=['r0','r1','r2','r3','r4','r5','r6']
df=pd.DataFrame(tech,index=row_name)


df2=df.groupby(['Course']).sum()
print(df2)

################################################
#group multiple columns
df2=df.groupby(['Course','Duration']).sum()
print(df2)

#Add indexes to group data
#Add Row index to the group by results

df2=df.groupby(['Course','Duration']).sum().reset_index()
print(df2)

############################################
#Get the list of all column names from haeders
column_headers=list(df.columns.values)
print("The columns Header :",column_headers)

#############################################
#using list (df)to get the columns
column_headers=list(df.columns)
print("The columns Header :",column_headers)


--------------------------------------------------------------
-----------------------"16/04/2024"---------------------------
------------------------------------------------------------

#Pandas shuffle DataFrame rows
#Shuffle th DataFrame rows & return all rows

df1=df.sample(frac=0.5)
print(df1)

#reset index after shuffling
df2=df.sample(frac=0.8).reset_index()
print(df2)

########################################################
#drop shuffle index
df2=df.sample(frac=0.6).reset_index(drop=True)
print(df2)

############################################################
#Pandas Joins
import pandas as pd
tech1={"Course":["Spark ","Pyspark","Python ","PAndas"],
       "Fee":[20000,25000,22000,30000],
       "Duration":["30days","40days","35days","50days"]}
row_name1=['r1','r2','r3','r4']
df=pd.DataFrame(tech1,index=row_name1)



df3=df.join(df2,lsuffix="_left",rsuffix="_right")
df3

#PAndas inner join
df4=df.join(df2,lsuffix="_left",rsuffix="_right",how="inner")
print(df4)

#PAndas right join DataFrame
df4=df.join(df2,lsuffix="_left",rsuffix="_right",how="right")
print(df4)

#Pandas left join DataFrame
df3=df.join(df2,lsuffix="_left",rsuffix="_right",how="left")
print(df3)

###############################################
#Pandas Merge

df3=pd.merge(df,df2)
print(df3)

df3=df.merge(df2)
print(df3)

############################################
#Using pandas.concat to concat two dataframe
df1=pd.DataFrame({"Course":["Spark ","Pyspark","Python ","PAndas"],
       "Fee":[20000,25000,22000,30000]})
df2=pd.DataFrame({"Course":["Unix","Hadoop","Hyperion","Java"],
       "Fee":[20000,25000,22000,30000]})
df=pd.DataFrame({"Duration":["30days","40days","35days","60days","55days"],
                 "Discount":[3000,2300,2500,2000,3000]})

data=[df1,df2]
df3=pd.concat(data)
df3

df4=pd.concat(data,axis=1).reset_index()
df4

#Concating multiple Columns
data=([df1,df2,df])
df5=pd.concat(data)


----------------------------------------------------------
--------------------"18/04/2024"------------------------
----------------------------------------------------------
import pandas as pd
df=pd.read_excel("expenses.xls")
df
       
#################################################
#using series.values.tolist()
col_list=df.Course.values
print(col_list)
col_list=df.Course.values.tolist()
print(col_list)


col_list=df["Course"].values
print(col_list)

col_list=df["Course"].values.tolist()
print(col_list)

#Using list() function
col_list=list[df["Course"]]
print(col_list)

#Convert to numpy array
col_list=df["Course"].to_numpy()
print(col_list)


