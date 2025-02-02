# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:09:57 2024

@author: Vaishnavi
"""
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder

#step1:simulating healthcare transactions(symptoms/diseases/treatment)
healthcare_data=[['fever','cough','covid-19'],
                 ['cough','sore throat','flu'],
                 ['fever','cough','shortness of breath','covid-19'],
                 ['cough','sore throat','flu','headache'],
                 ['fever','body ache','flu'],
                 ['fever','cough','covid-19','shortness of breath'],
                 ['sore throat','headache','cough'],
                 ['body ache','fatigue','flu'],
                 ]

#step1:convert the dataset into a format suitable for Apriori
te=TransactionEncoder()
te_ary=te.fit(healthcare_data).transform(healthcare_data)
df=pd.DataFrame(te_ary,columns=te.columns_)

#step2:Apply the apriori algorithm to find frequent itemsets
frequent_itemsets=apriori(df,min_support=0.3,use_colnames=True)
#min_support =0.6/0.7 try for it
#step3:Generate association rules from the frequent itemsets
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=0.7)
#try for threshold=2
#step4:Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])
