# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:09:44 2024

@author: Vaishnavi
"""
import numpy as np

#lets define a true value that we want to measure
#we first define the f=true value of 50 .This is the reference point
true_value=50

#simulate some measurements
#accurate but not precise(close to true vaue but spread out)
'''simulating measurements
We simulate two sets of measurements:

Accurate but not Precise:These values are centered around the true
value(50),but there is some spread(random variation).
this simulates measurements that are accurate
(close to the true value)but not precise (spread out).
'''
accurate_measurements=np.random.normal(loc=true_value,scale=5,size=10)
#precise but not accurate (far from true value but tightly grouped)
'''
Precise but not Accurate:
    These values are tightly clustered around 60,
    not near the true value of 50.
    This simulates measurements that are precise (closely grouped)
    but not accurate (far from the true value).
    
'''
precise_measurements=np.random.normal(loc=60,scale=1,size=10)

#function to calculate accuracy
'''
to calcuate the mean(average) of the measurements.
Thus,we calculate how close this average is to the true value.
The closer the average is to the true value,the higher the accuracy.
The accuracy formula is 1-(difference/true_value).
This gives a number between 0 (low accuracy) and 1(high accuracy)

'''
def calculate_accuracy(measurements,true_value):
    #accuracy :how close the average measurement is to the true value
    average_measurement=np.mean(measurements)
    accuracy=1-abs(average_measurement-true_value)/true_value
    return accuracy

#function to calcuate precision
'''
Precision is determined by the standard deviation of the measurements.
Standard deviation measures how spread out the measurements are.
If the standard deviation is small(measurements are close together),
precision will be high.We use 1/std_deviation to represent precision,
so a small spread gives a higher value for precision'''

def calculate_precision(measurements):
    #precision:how close the measurements are to each other:
    #(low standard deviation means high precision)
    precision=1/np.std(measurements)#higher std deviation
    #means lower precision,so we invert it
    return precision

#calcuate accuracy and precision for both sets
'''
accuracy measurements:we calculate the accuracy and precision of the measurements
that are closer to the true value but spread out.
Precision Measurements:We calculate the accuracy and precision of the 
measurements that are closely grouped but far from the true value .
'''
accuracy_of_accurate=calculate_accuracy(accurate_measurements,true_value)
precision_of_accurate=calculate_precision(precise_measurements)

#print the results
print("Accurate but not precise measurements:")
print(f"Measurements:{accurate_measurements}")
print(f"Accuracy:{accuracy_of_accurate:.2f}")
print(f"Precision:{precision_of_accurate:.2f}")

print("\nPrecise but Not accurate measurements:")
print(f"Measurements:{precise_measurements}")
print()