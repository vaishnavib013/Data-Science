# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 08:24:02 2024

@author: SSK
"""

import seaborn as sns
import pandas as pd
sales = pd.read_excel("C:/Users/SSK/1-python/PythonforDS/sales.xlsx")
sales.head()
sales.columns

cars=pd.read_csv("C:/Users/SSK/1-python/PythonforDS/cars.csv")
cars.columns
sns.relplot(x='HP', y='MPG',data=cars)
sns.relplot(x='HP', y='MPG',data=cars,kind='line')




sns.relplot('Sales','Profit', data=sales)
sns.relplot('Sales','Profit', data=sales,hue='Order')
sns.relplot('Order Date','Sales', data=sales, kind='line')



#########################
#Boxplot
sns.catplot(x='HP', y='MPG',data=cars,kind='box')

#sns.catplot(x='Product Category', y='Sales',data=sales,kind='box')

#################################
#Histogram
sns.distplot(cars.HP)
#################################



#multiple correlation regression analysis
import pandas as pd
import numpy as np
import seaborn as sns
cars=pd.read_csv("C:/Users/SSK/1-Python/PythonforDS/cars.csv")
cars.describe()
'''
               HP        MPG         VOL          SP         WT
count   81.000000  81.000000   81.000000   81.000000  81.000000
mean   117.469136  34.422076   98.765432  121.540272  32.412577
std     57.113502   9.131445   22.301497   14.181432   7.492813
min     49.000000  12.101263   50.000000   99.564907  15.712859
25%     84.000000  27.856252   89.000000  113.829145  29.591768
50%    100.000000  35.152727  101.000000  118.208698  32.734518
75%    140.000000  39.531633  113.000000  126.404312  37.392524
max    322.000000  53.700681  160.000000  169.598513  52.997752
'''


#graphical representation
import matplotlib.pyplot as plt
import numpy as np
plt.bar(height=cars.HP, x = np.arange(1, 82, 1))
sns.distplot(cars.HP)
sns.boxplot(cars.HP)
#check last 3rd page of notebook 
#to plot the box plots
sns.distplot(cars.MPG)
sns.boxplot(cars.MPG)

sns.distplot(cars.VOL) #slight left skewed
sns.boxplot(cars.VOL)

sns.distplot(cars.SP) #right skwewd
sns.boxplot(cars.SP)

sns.distplot(cars.WT) #right skwewd
sns.boxplot(cars.WT)


##############################
#Joint Plot

#histogram+scattered plot

import seaborn as sns
sns.jointplot(x=cars['HP'], y=cars['MPG'])

#################################

#Count Plot
#how many times each value occurred
plt.figure(2, figsize=(16,10))
sns.countplot(cars["MPG"])
