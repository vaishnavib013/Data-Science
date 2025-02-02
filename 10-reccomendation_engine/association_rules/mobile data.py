# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 09:42:26 2024

@author: Vaishnavi
"""
#for mobile data
min_support=0.2
metric="confidence"
min_threshold=0.5

import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder


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
-
print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])

