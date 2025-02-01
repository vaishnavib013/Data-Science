# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 09:11:33 2024

@author: Vaishnavi
"""
"""1. Write a Pandas program to convert Series of lists to one Series.
Sample Output: 
Original Series of list
0 [Red, Green, White]
1 [Red, Black]
2 [Yellow]
dtype: object
One Series
0 Red
1 Green
2 White
3 Red
4 Black
5 Yellow
dtype: object
"""
#31/07/2024
import pandas as pd
from itertools import chain
df=pd.Series([['Red','Green','White'],['red','black'],['yellow']],index=[0,1,2])
df
one_series=pd.Series(list(chain.from_iterable(df)))
one_series
"""
2. Write a python NLTK program to split the text sentence/paragraph into 
a list of words.
text = '''
Joe waited for the train. The train was late. 
Mary and Samantha took the bus. 
I looked for Mary and Samantha at the bus station.
'''
"""
spli
import nltk 
"""
3. Create a result array by adding the following two NumPy arrays. Next, 
modify the result array by calculating the square of each element
arrayOne = numpy.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = numpy.array([[15 ,33, 24], [4 ,7, 1]])
"""

"""
4. Write a python program to extract word mention someone in tweets 
using @ from the specified column of a given DataFrame.
DataFrame: ({
 'tweets': ['@Obama says goodbye','Retweets for @cash','A political endorsement in 
@Indonesia', '1 dog = many #retweets', 'Just a simple #egg']
 """


"""
5. Write a NumPy program to compute the mean, standard deviation, and 
variance of a given array along the second axis.
array:
[0 1 2 3 8 5]
"""

df.describe()
