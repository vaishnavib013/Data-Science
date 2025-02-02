# -*- coding: utf-8 -*-
"""
Created on Thu Jan 16 09:09:58 2025

@author: Vaishnavi
"""
# Hypothesis Testing:

import pandas as pd
import numpy as np
import scipy
from scipy import stats
#provides statistical functions;
#stats contains a variety of statistical tests.
from statsmodels.stats import descriptivestats as sd
#Provides descriptive statistics tools,including the sign_test.
from statsmodels.stats.weightstats import ztest
#Used fro conducting Z-tests on dataset.

#1 sample sign test
#Whenever there is a single sample and dataset is normal
marks=pd.read_csv("C:/13 - Hypothesis Testing/Signtest.csv")

#Normal QQ plot
import pylab
stats.probplot(marks.Scores,dist='norm',plot=pylab)
#creates a QQ plot to visually check if the data follows a normal distribution
#Test for normality
shapiro_test = stats.shapiro(marks.Scores)
#perform the Sharpiro-Wilk Test for normality
#H0(null hypothesis):The data is normally distributed.
#H1(alternate hypothesis):The data is not normally distributed.
#Outputs a test statistic and p-value
print("Shapiro Test:",shapiro_test)
#p_value is 0.024< 0.05,data is not normal

#Descriptive statistics
print(marks.Scores.describe())
#mean=84.20 and meadian=89.00
#1-sample sign test
sign_test_result = sd.sign_test(marks.Scores,mu0=marks.Scores.mean())
print("Sign Test Result:",sign_test_result)
#Result:p-value=0.82
#Interpretation:
#H0:The median of Scores is equal to the mean of Scores.
#H1:The median of Score is not equal to the mean ofScores.
#Since the p-value(0.82) is greater than 0.05, we fail to reject the null hypothesis
#Conclusion:The median and mean of Scores are statistically not similar.

#1-sample Z-test
fabric =pd.read_csv("C:/13 - Hypothesis Testing/Fabric_data.csv")

#Normality test
fabric_normality=stats.shapiro(fabric)
print("Fabric Normality Test:",fabric_normality)
#p value=0.1460>0.05

fabric_mean = np.mean(fabric)
print("Mean Fabric Length:",fabric_mean)

#Z-test
z_test_result,p_val = ztest(fabric['Fabric_length'],value=150)
print("Z-Test Result:",z_test_result,"p-value",p_val)
#Result:p-value=7.15* 10^-6
#Interpretation:
#HO:The mean fabric length is 150.
#H1:Themean fabric length is not 150.
#Since the p-value is extremely small(less tha 0.05), we reject the null hypothesis.
#Conclusion:The mean fabric length significantly differs from 150.

#Mann-Witney Test
fuel=pd.read_csv("C:/13 - Hypothesis Testing/mann_whitney_additive.csv")
fuel.columns=["Without_additive","With_additive"]

#Normality tests
print("Without Additive Normality:",stats.shapiro(fuel.Without_additive))
#p=0.50>0.05 :accept H)
print("With Additive Normality:",stats.shapiro(fuel.With_additive))
#0.04<0.05:reject H) data is not normal
#Mann-Whitney U Test
mannwhitney_result=stats.mannwhitneyu(fuel.Without_additive,fuel.With_additive)
print("Mann-Whitney Test Result:",mannwhitney_result)
#Result:p-value=0.445
#Interpretation:
#H0:difference is performance betwwen Without_additive and With_additive.
#H1:A significant difference exists.
#Since the p-value(0.445) isgreater than 0.05,we fail to reject the null hypothesis
#Conclusion:Adding fuel additive does not significantly impact performance.
#Applies the Mann-Whitney U Test to check if there's a sagnificant difference betwwen them
#H0:No difference in performance betwwn the two groups.
#H1:Significant difference in performance.

#Paired T-Test
sup=pd.read_csv("C:/13 - Hypothesis Testing/paired2.csv")

#Normality tests
print("Supplier A Normality Test:",stats.shapiro(sup.SupplierA))
#p-value=0.896199285>0.05:fails to reject the H),data is normal
print("Supplier B Normality Test:",stats.shapiro(sup.SupplierB))
#pvalue=0.896199285>0.05:fails to reject the H),data is normal
#Paired T-Test
t_test_result,p_val=stats.ttest_rel(sup['SupplierA'],sup['SupplierB'])
print("Paired T-Test Result:",t_test_result,"P-Value:",p_val)
#Result:p-value=0.00
#Interpretation:
#H0:No significant difference in transaction times betwwn Supplier A and Supplier B
#Since the p-value(0.00) is less than 0.05,we reject the null hypothesis
#Conclusion: There is a sangificant difference in transaction times between them

# 2-SAMPLE TEST:
offers = pd.read_excel("C:/13 - Hypothesis Testing/Promotion.xlsx")
offers.columns = ["InterestRateWaiver","StandardPromotion"]

# Normality tests
print("InterestRateWaiver Normality: ", stats.shapiro(offers.InterestRateWaiver))
print("StandardPromotion Normality:", stats.shapiro(offers.StandardPromotion))

# Variance test
levene_test = scipy.stats.levene(offers.InterestRateWaiver, offers.StandardPromotion)
print("Levene Test (Variance): ", levene_test)

# pvalue=0.2875
# H0 = variance equal
# H1 = variance unequal
# pvalue = 0.2875>0.05 fail to reject null hypothesis (HO is accepted)

# 2-sample T-Test
ttest_result = scipy.stats.ttest_ind(offers.InterestRateWaiver, offers.Standard)
print("Two-sample T-Test:",ttest_result)
# Result: p-value=0.0242

# Interpretation:
# H0: Both offers have the same mean impact.
# H1: The mean impacts of the two offers are different.
# Since the p-value (0.0242) is less than 0.05, we reject the null hypothesis.
# Conclusion: There is significant difference between the two promotional offers

# Mood's Median Test
# Objective: Is the medians of Pooh, Piglet and Tigger are statistically equal.
# it has equal median or not.
import pandas as pd
animals = pd.read_csv("C:/13 - Hypothesis Testing/animals.csv")
animals.head()
animals

# Normality tests
print("Pooh Normality:", stats.shapiro(animals.Pooh))
# p-value : 0.0122

print("Piglet Normality:", stats.shapiro(animals.Piglet))
# p-value = 0.044

print("Tigger Normality:", stats.shapiro(animals.Tigger))
# p-value : 0.0219

# H0: data is normal
# H1: data is not normal
# Since all p values are less than 0.05 hence reject the null hypothesis
# data is not normal, hence Mood's Test

# MEDIAN TEST
median_test_result = stats.median_test(animals.Pooh, animals.Piglet, animals.Tigger)
print("Mood's Median Test: ", median_test_result)
# Result: 
# p-value = 0.186
# Interpretation:
# H0: All groups have equal medians.
# H1: At least one group has different median.
# Since the p-value (0.186) is greater than 0.05 , we fail to reject
# the null hypothesis
# Conclusion: The medians of Pooh, Piglet and Tigger are statistically equal.

######################################################################

# One-Way ANOVA test
# Objective: is the transaction times for the three suppliers are not significantly different

contract = pd.read_excel("C:/13 - Hypothesis Testing/ContractRenewal_Data(unstacked).xlsx")
contract.columns = ["Supp_A","Supp_B", "Supp_C"]

# Normality tests
print("Supp_A Normality: ", stats.shapiro(contract.Supp_A))
print("Supp_B Normality: ", stats.shapiro(contract.Supp_B))
print("Supp_C Normality: ", stats.shapiro(contract.Supp_C))

# All p-values are greater than 0.05
# We fail to reject the null hypothesis
# i.e H0 is accepted means data is normal

# Variance test
levene_test = scipy.stats.levene(contract.Supp_A,contract.Supp_B,contract.Supp_C)
print("Levene Test (Variance): ", levene_test)

# H0: data is having equal variance
# H1: data is having difference in variance
# p-value: 0.777>0.05 , H0 is accpeted

# ANOVA Test
anova_result = stats.f_oneway(contract.Supp_A,contract.Supp_B, contract.Supp_C)
print("One-Way ANOVA:", anova_result)

# Result: p-value = 0.104
# Interpretation:
# H0: All suppliers have the same mean transaction time.
# H1: At least one supplier has a different mean.
# Since the p-value(0.104) is greater than 0.05, we fail to reject the
# null hypothesis.
# Conclusion: The transaction times for the three suppliers are not


##16-01-2025
#Two Proportions Z-Test

#Use a Two-sided test when you want to detect a difference without 
#assuming beforehand which group will have a higher or lower proportion.
#Example:Testing if there's a difference in soft drinks consumption between adults and children
#Adults and chilren without  assuming which group comsumes more.
#Objective:There is a significant diffrenece in soft drinksconsumption
#between adults and children.
soft_drinks=pd.read_excel("JohnyTalkers.xlsx")
from statsmodels.stats.proportion import proportions_ztest

#Data preparation 
count=np.array([58,152])
nobs=np.array([480,740])
#the two proportion z-test compares the proportions
#of two groups.here:
    
#count=[58,152]:THe number of successes
#(people comsuming soft drinks) in each group(adults and children)

#nobs[480,740]:THe total number of observations
#in each group(total adults and children surveyed).
#the count and nobs values come from summarizing the data
#about the soft drink consumption for adult  and children .
#here's how there values are typically obtained:
    
#count:Represents the number of individuals in each groups
# who consume soft drinks (the "successes").


#For example, if 480 adults were surveyed and 58 of them
#reported consuming soft drinks, the first count is 58.

#similarly,if 740 children were surveyed and 152 of them 
#reported consuming soft drinks,the sencond count is 152
#thus,count=[58,152].

#nobs:Represents the total number of individuals surveyed 
#in each group

#the total number of adults surveyed is 480.
#the total number of children surveyed is 740.
#hence,nobs=[480,740]

#these values are often extracted from the dataset
#if your data is in a file (like "JohnyTalkers.xlsx"),
#you can calculate these values as follows:
    
import pandas as pd

#load the dataset
file_path="C:/Users/Vaishnavi/Downloads/JohnyTalkers.xlsx"
soft_drink_data=pd.read_excel(file_path)

#filter thw data into adults and children categories
adults=soft_drink_data[soft_drink_data['Person']=='Adults']
children=soft_drink_data[soft_drink_data["Person"]=='Children']

#Count of successes (soft drinks consumers) for each group
count_adults=adults[adults['Drinks']=='Purchased'].shape[0]
count_children=children[children['Drinks']=='Purchased'].shape[0]

#total observations for each group
nobs_adults=adults.shape[0]
nobs_children=children.shape[0]

#FInal arrays for Z-test
count=[count_adults,count_children]
nobs=[nobs_adults,nobs_children]

print("COunts(soft Drink COnsumers):",count)
print("TOtal observaltions:",nobs)

#Two sided test
z_stat,p_val=proportions_ztest(count,nobs,alternative='two-sided')
print("Two sided Proportion Test:",z_stat,"P-Value:",p_val)
#REsult:p_val=0.00
#Interpretations:
#H0:Proportions of adults and children consuming the soft drinks are there
#H1:Proportions are diffrent
#Since the p-value(0.000) is less than 0.05,we reject the null hypothesis
#COnclusions:There is a significant diffrence in soft drink consuptions

#Chi-Squared TEst
#objective:is defective proportions are independent of the country?
#The dataset contains two columns:
    
#Defective:Indicates whether an item is defective(likely binary,
#with 1 for defective and 0 is for not defective).
#Country:Specifies the country associated with the item(eg.,"india")
#The dataset has 800 entries ,and there are
#no missing values either column.It appears to be designed to analyze
#defect rates across different countries,
#which aligns with the chi-square test you performed earlier
#to determin if defectiveness is independent of the country

Bahaman=pd.read_excel("C:/Users/Vaishnavi/Downloads/Bahaman_1.xlsx")

#CrossTabulation
count=pd.crosstab(Bahaman["Defective"],Bahaman["Country"])
count

#Chi-Squared Test
chi2_result=scipy.stats.chi2_contingency(count)
print("Chi-Square Test:",chi2_result)
#Result:pvalue=0.6315
#Interpretation:
#H0:Defective proportions are independent of the country
#H1:Defective proportions depend of the country
#Since the p-value (0.6315) is greater than 0.05 ,we accept the null hypothesis
#Conclusion:Defective proportions are independent of the country.