# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:12:17 2024

@author: Vaishnavi
"""
#pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder
#Sample dataset
#load the CSV file
df=pd.read_csv("C:/10-reccomendation_engine/assignments/myphonedata.csv")

#here the step 1 is not needed...directly we can go for step 2
#step1:convert the dataset into a format suitable for Apriori
#te=TransactionEncoder()
#te_ary=te.fit(df).transform(df)
#df=pd.DataFrame(te_ary,columns=te.columns_)

#step2:Apply the apriori algorithm to find frequent itemsets
frequent_itemsets=apriori(df,min_support=0.05,use_colnames=True)
print(frequent_itemsets)
#min_support =0.6/0.7 try for it
""" support              itemsets
0   0.545455                 (red)
1   0.636364               (white)
2   0.181818               (green)
3   0.090909              (yellow)
4   0.181818              (orange)
5   0.545455                (blue)
6   0.363636          (red, white)
7   0.090909          (red, green)
8   0.090909         (red, orange)
9   0.363636           (red, blue)
10  0.090909        (white, green)
11  0.181818       (orange, white)
12  0.363636         (blue, white)
13  0.090909   (red, white, green)
14  0.090909  (red, orange, white)
15  0.181818    (red, blue, white)"""
df.shape
df.dtypes
"""Out[130]: 
red       int64
white     int64
green     int64
yellow    int64
orange    int64
blue      int64
dtype: object"""

#step3:Generate association rules from the frequent itemsets
rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
#try for threshold=2
#step4:Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)
"""support              itemsets
0   0.545455                 (red)
1   0.636364               (white)
2   0.181818               (green)
3   0.090909              (yellow)
4   0.181818              (orange)
5   0.545455                (blue)
6   0.363636          (red, white)
7   0.090909          (red, green)
8   0.090909         (red, orange)
9   0.363636           (red, blue)
10  0.090909        (white, green)
11  0.181818       (orange, white)
12  0.363636         (blue, white)
13  0.090909   (red, white, green)
14  0.090909  (red, orange, white)
15  0.181818    (red, blue, white)"""
print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])
"""    antecedents     consequents   support  confidence      lift
0            (red)         (white)  0.363636    0.666667  1.047619
1          (white)           (red)  0.363636    0.571429  1.047619
2            (red)          (blue)  0.363636    0.666667  1.222222
3           (blue)           (red)  0.363636    0.666667  1.222222
4         (orange)         (white)  0.181818    1.000000  1.571429
5          (white)        (orange)  0.181818    0.285714  1.571429
6           (blue)         (white)  0.363636    0.666667  1.047619
7          (white)          (blue)  0.363636    0.571429  1.047619
8     (red, white)         (green)  0.090909    0.250000  1.375000
9     (red, green)         (white)  0.090909    1.000000  1.571429
10  (white, green)           (red)  0.090909    1.000000  1.833333
11           (red)  (white, green)  0.090909    0.166667  1.833333
12         (white)    (red, green)  0.090909    0.142857  1.571429
13         (green)    (red, white)  0.090909    0.500000  1.375000
14   (red, orange)         (white)  0.090909    1.000000  1.571429
15    (red, white)        (orange)  0.090909    0.250000  1.375000
16        (orange)    (red, white)  0.090909    0.500000  1.375000
17         (white)   (red, orange)  0.090909    0.142857  1.571429"""
