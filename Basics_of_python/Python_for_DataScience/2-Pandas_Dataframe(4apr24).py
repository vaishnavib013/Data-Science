# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 08:22:30 2024
#computer vision and nlp 
@author: Vaishnavi
"""
"""#lambda,shallow,deep,decorators,iloc,loc"""
#what is pandas dataframes?
#conda install pandas/pip install pandas
#pandas is a two dimensional 
#current version of pandas 2.2.1
#to check the version of pandas

#to upgrade the latest version of pandas
#pip uninstall pandas
#upgrade to specific version
#conda install pandas==2.1
import pandas as pd
pd.__version__
"""pd.__version__
Out[2]: '2.1.4'"""
########################################
#create using constructor
#create pandas DataFrame from list
#one dataframe consist of one table like sql
import pandas as pd
technologies=[['Spark',20000,'30days'],
              ['pandas',20000,'40days']]
df=pd.DataFrame(technologies)
print(df)
'''       
    0      1       2
0   Spark  20000  30days
1  pandas  20000  40days'''
#technologies consist of lists
#df will contain the table having the 0 and 1 indexes bydefault as it was not mentioned
#storing in it spark and pandas values
#################################
#add coolumn name and rows labels
#indexes,dataframe by default assigns
#incremental 
column_names=["courses","fee","duration"]
row_label=["a","b"]
df=pd.DataFrame(technologies,columns=column_names,index=row_label)
print(df)
#############################
df.dtypes
'''courses     object
fee          int64
duration    object
dtype: object'''
###################################
#you can also assign custom 
"""important dataframes"""
#datatypes to columns
#set custom types to DataFrames
import pandas as pd
technologies={'courses':
              ["spark","pyspark","hadoop","python","pandas","oracle","java"],
              "fee":[20000,24000,14000,15000,25000,26000,30000],
              "discounts":[11.9,12.8,10.0,9.1,21.9,5.7,11.7],
              "duration":['30days','15days','3days','5days','7days','10days','11days']} 
df=pd.DataFrame(technologies)
print(df.dtypes)
print(df)
"""courses       object
fee            int64
discounts    float64
duration      object
dtype: object """
#convert all types to best possible types
"""readyreference :
    #convert all types to best possible types
    """
d2f=df.convert_dtypes()
print(d2f.dtypes)
#change aLL COLUMNS to same type'
df=df.astype(str)
print(df.dtypes)
#change type for one or multiple variables
df=df.astype({"fee":int,"discounts":float})
print(df.dtypes)

############################
"""readyreference :"""

#convert datatypes for all columns in a list
df=pd.DataFrame(technologies)
df.dtypes
cols=["fee","discounts"]
df[cols]=df[cols].astype('float')
df.dtypes

df=df.astype({"courses":int})
df.dtypes
#here it gives errors

#ignore errors
df=df.astype({"courses":int},errors='ignore')
df.dtypes
###########################
#generates errors
df=df.astype({"courses":int},errors='raise')

#######################
#convert feed column into numeric type
df=df.astype(str)
#it will convert it into the object type
print(df.dtypes)
############################
#convert feed column into numeric type
df=df.astype(str)
print(df.dtypes)
df['discounts']=pd.to_numeric(df['discounts'])
df.dtypes
"""courses       object
fee           object
discounts    float64
duration      object
dtype: object"""
###########################
import pandas as pd
#create dataframes from dictionary
technologies={"courses":['spark','pyspark','hadoop'],
              "fee":[2000,3000,40000],
              "duration":["30days","4days","5days"],
              "discounts":[1000,2300,1500]}
df=pd.DataFrame(technologies)
df
####convert dataframe to csv
df.to_csv('data_file.csv')

df=pd.read_csv('data_file.csv')
#none=np.nan=" "
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas",None,"oracle","java"],
              "fee":[20000,24000,14000,15000,np.nan,25000,26000,30000],
              "discounts":[11.9,12.8,10.0,9.1,21.9,5.7,11.7,9.7],
              "duration":['30days','15days',' ','7days','5days','7days','10days','11days']} 
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df=pd.DataFrame(technologies ,index=row_labels)
print(df)
###################################
#5april-2024
#dataframes properties
df.shape#imp
#it returns the no of rows and columns
"""(8, 4)"""
df.size#imp
#
#32
df.columns#imp
df.columns.values
df.index
df.dtypes#imp
df.info
"""
#1.understanding business(objective)80%
#2.EDA(exploratory data analysis -include here the imp points noted above)
#3.data dictionary(no of columns,etc )
#4.data processing(col x_y format not including space)
#5.model developing/building(10%)
#6.performance evaluation 
#7.deployment
#8.monitoring and maintainance
"""
#accessing one column contents
df['fee']
#accessing two columns contents
cols=['fee','duration']
df[cols]
"""fee duration
r0  20000.0   30days
r1  24000.0   15days
r2  14000.0         
r3  15000.0    7days
r4      NaN    5days
r5  25000.0    7days
r6  26000.0   10days
r7  30000.0   11days
"""#another way for multiple columns accessing
df[['fee','duration']]
"""fee duration
r0  20000.0   30days
r1  24000.0   15days
r2  14000.0         
r3  15000.0    7days
r4      NaN    5days
r5  25000.0    7days
r6  26000.0   10days
r7  30000.0   11days
"""
#select certain rows and assign it to another dataframes
#df[rows,columns]
#df[:,:]-for all rows and all columns
#df[:7]#for columns from start to 7-1 rows
#it it same as of indexing or range
#df[:,:2]for rows indexing ,for column indexing
#indexing start from 0
df2=df[6:]
df2
"""courses      fee  discounts duration
r6  oracle  26000.0       11.7   10days
r7    java  30000.0        9.7   11days"""

#######
df2=df[:6]
df2
"""courses      fee  discounts duration
r0    spark  20000.0       11.9   30days
r1  pyspark  24000.0       12.8   15days
r2   hadoop  14000.0       10.0         
r3   python  15000.0        9.1    7days
r4   pandas      NaN       21.9    5days
r5     None  25000.0        5.7    7days
"""
#######################################
#accessing certain cell from column duration
df['duration'][3]
#substracting specific value from a column
df['fee']=df['fee']-500
df['fee']
"""
r0    19500.0
r1    23500.0
r2    13500.0
r3    14500.0
r4        NaN
r5    24500.0
r6    25500.0
r7    29500.0
Name: fee, dtype: float64
"""
#pandas to manipulate dataframe
#describe dataframe
#describe the dataframe for all numeric columns
df.describe()
"""                fee  discounts
count      7.000000   8.000000
mean   21500.000000  11.600000
std     5916.079783   4.703494
min    13500.000000   5.700000
25%    17000.000000   9.550000
50%    23500.000000  10.850000
75%    25000.000000  12.125000
max    29500.000000  21.900000
"""
#it wil show 5 number summary
#it describes about mean, median, standard deviation
#it describes dataframes for all numeric columns
#you will get some infrence over here
###############################
#rename()-rename pandas dataframes columns
df=pd.DataFrame(technologies,index=row_labels)
#assign new header by setting new column names
df.columns=['A','B','C','D']
df
#all the columns are having the the new labels as a,b,c,d
############################
##for rowsw axis=0 and for columns axis =1
#rename columns names using rename() method
df=pd.DataFrame(technologies,index=row_labels)
df.columns=['A','B','C','D']
df2
df2=df.rename({'A':'C1','B':'C2'},axis=1)
df2
df2=df.rename({'A':'C1','B':'C2'},axis='columns')
df2
df2=df.rename(columns={'A':'C3','B':'C4'})
df2
################################
"""quick reference"""
#drop Dataframe rows and columns
df=pd.DataFrame(technologies,index=row_labels)
#drop rows by labels
df1=df.drop(['r1','r2'])
df1
#delete rows by position /index
df1=df.drop(df.index[1])
df1
df1=df.drop(df.index[[1,3]])
df1
#delete rows by index range
df1=df.drop(df.index[2:])
df1
##########################333
#when you have default indexes for rows
df=pd.DataFrame(technologies)
df1=df.drop(0)
df1
df=pd.DataFrame(technologies)
df1=df.drop([0,3],axis=0)#it will delete rows0 and row3
df1
df1=df.drop(range(0,2))#it will delete 0 and 1
df1
#######################33
#09-04-2024
"""readyreference pg"""
#dropping of colummns
import pandas as pd
technologies={"courses":['spark','pyspark','hadoop'],
              "fee":[2000,3000,40000],
              "duration":["30days","4days","5days"],
              "discounts":[1000,2300,1500]}
df=pd.DataFrame(technologies)
df
################
df2=df.drop(["fee"],axis=1)
print(df2)
#explicitly usi g thw parameters name "label"
df2=df.drop(labels=["fee"],axis=1)
df2

#alternatively you can also use the columns instead of labels
df2=df.drop(columns=["fee"],axis=1)
df2
#drop column by index
print(df.drop(df.columns[1],axis=1))
df=pd.DataFrame(technologies)

####################
#if you want to make changes in the same df then use inplace
#so that another instance is not created
#inplace=True
df.drop(df.columns[2],axis=1,inplace=True)
print(df)
#################################
df=pd.DataFrame(technologies)
#drop 2 or more columns by label name
df2=df.drop(["courses","fee"],axis=1)
print(df2)
#######################################
#drop two or more columns by index
df=pd.DataFrame(technologies)
df2=df.drop(df.columns[[0,1]],axis=1)
print(df2)
############################################
"""readyreference pg"""
#drop columns from list of columns
df=pd.DataFrame(technologies)
df.columns
lisCol=["courses","fee"]
df2=df.drop(lisCol,axis=1)
print(df2)
##################################
#using inplace=True
#remove columns from dataframe inplace
#it will delete the col from the original dataframe 
#not from the instance created 
df=pd.DataFrame(technologies)
df.drop(df.columns[1],axis=1,inplace=True)
df
####################################
#pandas select rows by index(position/label)
#iloc is used when we want to access by index
#loc is used when we want to access by names
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas",None,"oracle","java"],
              "fee":[20000,24000,14000,15000,np.nan,25000,26000,30000],
              "discounts":[11.9,12.8,10.0,9.1,21.9,5.7,11.7,9.7],
              "duration":['30days','15days',' ','7days','5days','7days','10days','11days']} 
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df=pd.DataFrame(technologies ,index=row_labels)
print(df)
#accessing rows and columns using index we use iloc
#############################
#iloc:
    #df.iloc[startrow:endrow,startcolumn:endcolumn]

#whenever using ","in iloc is necessary....df=pd.DataFrame(technologies,index=row_labels)
#in slicing ","should not b given
df=pd.DataFrame(technologies,index=row_labels)
#below are quick examples
df2=df.iloc[0:2]
df2
"""
courses      fee  discounts duration
r0    spark  20000.0       11.9   30days
r1  pyspark  24000.0       12.8   15days
"""
###########################
#when we want all rows And 2 columns only
df2=df.iloc[:,0:2]
df2
"""courses      fee
r0    spark  20000.0
r1  pyspark  24000.0
r2   hadoop  14000.0
r3   python  15000.0
r4   pandas      NaN
r5     None  25000.0
r6   oracle  26000.0
r7     java  30000.0
""" 
#this line uses slicing operator tp get datafrsme
#items by index
#the first slice[:]  indicated to return all rows
#the 2nd slice[0:2] indicated to return only 2 columns here it is specified 2
#between 0 and 2 (excluding 2) should be return
###################
#when we want 2 rows and all columns we use this
df2=df.iloc[0:2,:]
df2
"""courses      fee  discounts duration
r0    spark  20000.0       11.9   30days
r1  pyspark  24000.0       12.8   15days"""
#in this case, the 1st slice[0:2] is
#requesting only 2 rows 0 through 1 of the dataframe
#the second slice [:] indicates that all columns are required
###############################
#slicing specific rows and columns using iloc attribute
df3=df.iloc[1:2 , 1:3]
df3
"""fee  discounts
r1  24000.0       12.8"""
####################
#another example
df3=df.iloc[:,1:3]
df3
"""fee  discounts
r0  20000.0       11.9
r1  24000.0       12.8
r2  14000.0       10.0
r3  15000.0        9.1
r4      NaN       21.9
r5  25000.0        5.7
r6  26000.0       11.7
r7  30000.0        9.7"""
#the second operator [1:3] yeilds column 1 and 3 only
#select rows by integer index
df2=df.iloc[2]#seelct row by index
df2
"""courses       hadoop
fee          14000.0
discounts       10.0
duration            
Name: r2, dtype: object
"""
df2=df.iloc[[2,3,6]]#select rows by index list
df2=df.iloc[1:5]#select rows by integer index range
df2=df.iloc[:1]#seelct 1st row
df2=df.iloc[:3]

#########################
#12-04-2024
df2=df.iloc[2]
df2
df2=df.iloc[:3]
df2=df.iloc[1:5]
df2=df.iloc[:1]
df2=df.iloc[-1:]
df2=df.iloc[-3:]
df2=df.iloc[::-2]
df2=df.iloc[::2]
#################################
#select rows by index labels
df2=df.loc['r2']#select rows by label
df2
df2=df.loc[['r2']]
df2
df2=df.loc[['r2','r3','r6']]#select rows by index
df2=df.loc['r1':'r5']#select rows by label index
#select multiple rows by label index
df2=df.loc['r1':'r5':2]
#select alternate rows
"""courses      fee  discounts duration
r1  pyspark  24000.0       12.8   15days
r3   python  15000.0        9.1    7days
r5     None  25000.0        5.7    7days"""
#########################
#pandas selec columns by name or index
#by using df[] notation
df2=df['courses']
#select multiple columns
df2=df[['courses','fee','discounts']]

#using loc[] to take column slices
#loc[] syntax to slice columns
"""#df.loc[:,start:stop:step]"""
#select multiple columns
df2=df.loc[:,['courses','fee','discounts']]
#select random columns
df2=df.loc[:,["courses","fee","discounts"]]
#select columns between two columns
df2=df.loc[:,"courses":"discounts"]#from which column to which column you want the result we will use ":"
#select columns by range
df2=df.loc[:,"duration":]
#select column by range
#all the columns upto 'duration'
df2=df.loc[:,:'duration']
df2=df.loc[:,:'discounts']
#select alternate columns
df2=df.loc[:,::2]
##################################
#pandas.DataFrame.query() for exmaples
#query all rows with courses equals 'spark'
import pandas as pd
import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas","spark","oracle","java"],
              "fee":[20000,24000,14000,15000,np.nan,25000,26000,30000],
              "discounts":[11.9,12.8,10.0,9.1,21.9,5.7,11.7,9.7],
              "duration":['30days','15days',' ','7days','5days','7days','10days','11days']} 
row_labels=['r0','r1','r2','r3','r4','r5','r6','r7']

df=pd.DataFrame(technologies ,index=row_labels)
print(df)
df2=df.query("courses=='spark'")
print(df2)
"""courses      fee  discounts duration
r0   spark  20000.0       11.9   30days
"""
df2=df.query("courses!='spark'")
print(df2)

"""courses      fee  discounts duration
r1  pyspark  24000.0       12.8   15days
r2   hadoop  14000.0       10.0         
r3   python  15000.0        9.1    7days
r4   pandas      NaN       21.9    5days
r6   oracle  26000.0       11.7   10days
r7     java  30000.0        9.7   11days
"""
#pandas add column to dataframe
#add new column to the dataframe
tutors=["ram","sham","aarvi","ganshyam","rohan","ganesh","aaru","maanvi"]
df2=df.assign(TutorsAssigned=tutors)
df2


#another example
aarr=["ram","sham","aarvi","ganshyam","rohan","ganesh","aaru","maanvi"]
df2=df.assign(AarrAssigned=aarr)
df2
#
aarr=["sham","aarvi","ganshyam","rohan","ganesh","aaru","maanvi"]
df2=df.assign(AarrAssigned=aarr)
df2
"""Length of values (7) does not match length of index (8)"""
aarr=["a","b","sham","aarvi","ganshyam","rohan","ganesh","aaru","maanvi"]
df2=df.assign(AarrAssigned=aarr)
df2
"""Length of values (9) does not match length of index (8)"""
###################################
#add multiple columns to the dataframes
MNCCCompanies=["tata","HCL","Infoysys","google","amazon","benchmark","a","b"]
df2=df.assign(MNC=MNCCCompanies,tutors=tutors)
df2
"""courses      fee  discounts duration        MNC    tutors
r0    spark  20000.0       11.9   30days       tata       ram
r1  pyspark  24000.0       12.8   15days        HCL      sham
r2   hadoop  14000.0       10.0            Infoysys     aarvi
r3   python  15000.0        9.1    7days     google  ganshyam
r4   pandas      NaN       21.9    5days     amazon     rohan
r5    spark  25000.0        5.7    7days  benchmark    ganesh
r6   oracle  26000.0       11.7   10days          a      aaru
r7     java  30000.0        9.7   11days          b    maanvi
"""
#########################
#derive new column from existing column
df=pd.DataFrame(technologies)
df2=df.assign(Discount_percent=lambda x:x.fee*x.discounts/100)
print(df2)
"""courses      fee  discounts duration  Discount_per
0    spark  20000.0       11.9   30days        2380.0
1  pyspark  24000.0       12.8   15days        3072.0
2   hadoop  14000.0       10.0                 1400.0
3   python  15000.0        9.1    7days        1365.0
4   pandas      NaN       21.9    5days           NaN
5    spark  25000.0        5.7    7days        1425.0
6   oracle  26000.0       11.7   10days        3042.0
7     java  30000.0        9.7   11days        2910.0
"""
#######################
#append column to existing pandas dataframe
#add new column to the existing dataframe
df=pd.DataFrame(technologies)
df['mnccompanies']=MNCCCompanies
print(df)
##########################
#add new column at the specific position'
df=pd.DataFrame(technologies)
df.insert(0,'tutors',tutors)
print(df)
#at 0 position the new column is added ie tutors
#####################3
#rename the column
import pandas as pd
#import numpy as np
technologies={'courses':["spark","pyspark","hadoop","python","pandas","spark","oracle","java"],
              "fee":[20000,24000,14000,15000,np.nan,25000,26000,30000],
              "discounts":[11.9,12.8,10.0,9.1,21.9,5.7,11.7,9.7],
              "duration":['30days','15days',' ','7days','5days','7days','10days','11days']} 
df=pd.DataFrame(technologies)
df.columns
print(df.columns)
"""Index(['courses', 'fee', 'discounts', 'duration'], dtype='object')"""

#######################
#pandas rename column name
#rename a single column
df2=df.rename(columns={'courses':'courses_list'})
print(df2.columns)
"""Index(['courses_list', 'fee', 'discounts', 'duration'], dtype='object')"""

#alternatively, you can also write 
#rename multiple columns
df.rename(columns={"courses":"courses_list","fee":"courses_fee","duration":"courses_duration","discounts":"DISCOUNTS"},inplace=True)
print(df.columns)
df.columns
"""Index(['courses_list', 'courses_fee', 'DISCOUNTS', 'courses_duration'], dtype='object')"""
#HERE SEQUENCE DOESN'T MATTER

