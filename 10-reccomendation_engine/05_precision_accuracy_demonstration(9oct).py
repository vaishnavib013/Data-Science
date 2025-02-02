# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 08:56:37 2024

@author: Vaishnavi
"""
import numpy as np
import matplotlib.pyplot as plt

#target value(true value)
true_value=50

#simulate data
#1.Accurate amd precise (close to true value and tightly grouped)
'''
Loc=true_value(True Value=50):The values will be centered around the true value(50)
scale=1:The standard deviation (spread) IS small,
meaning the values will be tightly grouped around the true value.
This implies high precision.
The measurements will vary only a little from the true value,
so they'll be both accurate (close to 50) and precise(close to each other).
'''
accurate_precise=np.random.normal(loc=true_value,scale=1,size=10)

#2.Accurate but not precise (close to true value but spread out)
accurate_not_precise=np.random.normal(loc=true_value,scale=10,size=10)

'''
The two lines of code you've hightlighted may look similar,but they differ in one important aspect:the value of scale,
which controls the spread of the generated values around the true values(loc)'''
#3.Precise but not accurate (far from true value but tightly grouped)
precise_not_accurate=np.random.normal(loc=70,scale=1,size=10)
#4.neither the accurate nor precise
not_accurate_not_precise=np.random.normal(loc=70,scale=10,size=10)

#plotting the results
plt.figure(figsize=(10,6))

#plot 1:accurate and precise
plt.scatter(accurate_precise,[1]*10,color='green',label='Accurate and Precise')

#plot 2:accurate but not precise
plt.scatter(accurate_not_precise,[2]*10,color='blue',label='Accurate but not Precise')

#plot 3:precise but not accurate
plt.scatter(precise_not_accurate ,[3]*10,color='orange',label='Precise but not accurate')

#plot 4:neither precise nor accurate
plt.scatter(not_accurate_not_precise,[4]*10,color='red',label='Neither Accurate nor Precise')

#adding target line 
plt.axvline(true_value,color='black',linestyle='--',label='True Value')

#label and legend
plt.yticks([1,2,3,4],['Accurate and Precise','Accurate but Not Precise','Precise but not Accurate','Neither Accurate nor Precise'])
plt.xlabel('Measurement Value')
plt.legend()
plt.title('Accuracy and Precision Demonstration')






