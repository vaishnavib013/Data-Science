# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 22:02:01 2024

@author: Vaishnavi
"""
"""
Problem Statement: - 
A film distribution company wants to target audience
 based on their likes and dislikes, you as a Chief 
 Data Scientist Analyze the data and come up with 
 different rules of movie list so that the business 
 objective is achieved.
3.) my_movies.csv
"""
#pip install mlxtend
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
from mlxtend.preprocessing import TransactionEncoder
#Sample dataset
#load the CSV file
df=pd.read_csv("C:/10-reccomendation_engine/assignments/my_movies.csv")
df.head()
""" Sixth Sense  Gladiator  LOTR1  ...  LOTR  Braveheart  Green Mile
0            1          0      1  ...     0           0           1
1            0          1      0  ...     0           1           0
2            0          0      1  ...     0           0           0
3            1          1      0  ...     0           0           0
4            1          1      0  ...     0           0           0

[5 rows x 10 columns]"""

df.shape#Out[110]: (10, 10)

#step1:convert the dataset into a format suitable for Apriori
te=TransactionEncoder()
te_ary=te.fit(df).transform(df)
df=pd.DataFrame(te_ary,columns=te.columns_)

#step2:Apply the apriori algorithm to find frequent itemsets
frequent_itemsets=apriori(df,min_support=0.05,use_colnames=True)
print(frequent_itemsets)
""" support                        itemsets
0         0.4                             ( )
1         0.2                             (1)
2         0.2                             (2)
3         0.1                             (B)
4         0.2                             (G)
      ...                             ...
2664      0.1     (s, h, e, t, x, i,  , n, S)
2665      0.1     (1, r, e, t, H, y, o, P, a)
2666      0.1     (r, e, t, H, y, 2, o, P, a)
2667      0.1  (1, r, e, t, H, y,  , o, P, a)
2668      0.1  (r, e, t, H, y,  , 2, o, P, a)

[2669 rows x 2 columns]"""

rules=association_rules(frequent_itemsets,metric="lift",min_threshold=1)
#try for threshold=2
#step4:Output the results
print("Frequent Itemsets:")
print(frequent_itemsets)

print("\nAssociation Rules:")
print(rules[['antecedents','consequents','support','confidence','lift']])
""" antecedents                  consequents  support  confidence      lift
0              ( )                          (1)      0.1    0.250000  1.250000
1              (1)                          ( )      0.1    0.500000  1.250000
2              ( )                          (2)      0.1    0.250000  1.250000
3              (2)                          ( )      0.1    0.500000  1.250000
4              ( )                          (G)      0.1    0.250000  1.250000
           ...                          ...      ...         ...       ...
128259         ( )  (r, e, t, H, y, 2, o, P, a)      0.1    0.250000  2.500000
128260         (2)  (r, e, t, H, y,  , o, P, a)      0.1    0.500000  2.500000
128261         (o)  (r, e, t, H, y,  , 2, P, a)      0.1    0.250000  2.500000
128262         (P)  (r, e, t, H, y,  , 2, o, a)      0.1    0.333333  3.333333
128263         (a)  (r, e, t, H, y,  , 2, o, P)      0.1    0.200000  2.000000

[128264 rows x 5 columns]"""











