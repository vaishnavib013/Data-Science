# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 08:36:43 2025

@author: Vaishnavi
"""
import pandas as pd 
import numpy as np 
import scipy 
from scipy import stats

#provides statistical function:
#stats contains a variety of statistical tests.
from statsmodels.stats import descriptivestats as sd
#provides descriptive statistical tools,including the sign_test.
from statsmodels.stats.weightstats import ztest 
#used for conducting Z-tests on datasets.

#1 sample sign test
#whenever there is a single sample and data is not normal 
marks =pd.read_csv("C:/Users/Vaishnavi/Downloads/Signtest.csv")
 #normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)

##Creates a QQ plot to visually check if the data follows 
#Test for normality 
shapiro_test=stats.shapiro(marks.Scores)
#peroforms the SHapiro -Wilk Test for normality
#H0 (null hypothesis):THe data is normally distributed
#H1(alternate hypothesis):THe data is normally ditributed
#outputs as test statistic and p-value
print("Shapiro Test:",shapiro_test)
#p_value is 0.024<0.05 ,data is not normal 

#Descriptive statistics
print(marks.Scores.describe())
#mean=84.20 and median =89.000
#1-sample sign test 
sign_test_result=sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
print("Sign Test Result:",sign_test_result)
#result:p-value=0.82

#Interpretation:
#H0:The median of scores is equal to the mean of Scores
#H1:The median of scores is not equal to the mean of scores
#since the p-value (0.82) is greater than 0.05,we fail to reject the null hypothesis 
#Conclusion:THe median and mean of the Scores are statistically not similar

#Objective:CHeck whether the fabric length is exactly 150 or differ? 
#1-sample z-test:
fabric=pd.read_csv("C:/Users/Vaishnavi/Downloads/fabric_data.csv")

#Normality test
fabric_normality=stats.shapiro(fabric)
print("Fabric Normality Test:",fabric_normality)
#p-value=0.1460>0.05

fabric_mean=np.mean(fabric)
print("Mean Fabric Length:",fabric_mean)

#Z-test
z_test_result,p_value=ztest(fabric['Fabric_length'],value=150)
print("Z-test Result:",z_test_result,"P-value:",p_value)


#Mann-Whitney Test

#objective:check is there any difference in performance if additive is added in the petrol
fuel=pd.read_csv("C:/Users/Vaishnavi/Downloads/mann_whitney_additive.csv")
fuel.columns=["Without_additive","With_additive"]

#Normality tests
print("WIthout Additive Normality:",stats.shapiro(fuel.Without_additive))
#p=0.50>0.05:Accept H0 ie data is normal
print("WIth Additive Normality:",stats.shapiro(fuel.With_additive))
#0.04<0.05: Reject H0 data is not not normal
#Mann -Whitney U test
mannwhitney_result=stats.mannwhitneyu(fuel.Without_additive,fuel.With_additive)
print("Mann-Whitney Test Result:",mannwhitney_result)
#Result:p-value=0.445
#Interpretation:
#H0:No difference in performance between without_additive and with_additive
#H1:A significant difference exists.
#since the p-value (0.445) is greater than 0.05 ,we fail to reject the null hypothesis 
#Conclusion:Adding the fuel addittive does not significantly impact performance.
#Applies the Mann-Whitney U Test to check if here's a significant difference between 2 groups
#H0:No difference in performance between the two groups.
#H1:Significant diffrence in performance.


#Paired T-Test 
#Objective :Check whether there is diffrence in transaction time of SupplierA and SupplierB
sup=pd.read_csv("C:/Users/Vaishnavi/Downloads/paired2.csv")

#Normality Tests
print("Supplier A Normality Test:",stats.shapiro(sup.SupplierA))
#pvalue=0.896199285>0.05 :fails to reject the H0,data is normal
print("SupplierB Normality Test:",stats.shapiro(sup.SupplierB))
#pvalue=0.896199285>0.05:fails to reject the H0,data is normal
#Paired t-Test
t_test_result,p_val=stats.ttest_rel(sup['SupplierA'],sup['SupplierB'])
print("Paired T-Test Result:",t_test_result,"P-value:",p_val)
#Result:p-value=0.00
#Interpretation:
#H0:No significant Differnce in transaction times between Supplier A and Supplier B 
#H1:A significant diffrence exists
#Since the p-value (0.00) is less than 0.05,wereject the null hypothesis
#COnclusion:There is a significant differnce in trancaction times between SupplierA and SupplierB



