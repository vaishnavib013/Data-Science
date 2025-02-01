# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 08:44:49 2024

@author: Vaishnavi
"""

"""1.Write a Python function that takes two lists and returns True if they have at least one common
member."""
list1=[1,2,3,4,5]
list2=[6,7,8,2,9]
def common_value(list1,list2):
    return any(item in list1 for item in list2)
common_value(list1,list2)
"""Out[3]: True"""

"""2. Use list comprehension to construct a new list but add 6 to each item."""
original_list = [1, 2, 3, 4, 5]
new_list = [x + 6 for x in original_list]
print(new_list)
#[7, 8, 9, 10, 11]


"""3.Write a Python program to reverse a string."""
x="vaishnavi"
print(x[::-1])
#ivanhsiav


"""4. Write a Python program to iterate over dictionaries using for loops."""
dict={"name":"vaishnavi","rollno":1,"class":"sya"}
for key,value in dict.items():
    print(key,":",value)
"""name : vaishnavi
rollno : 1
class : sya"""

"""5. Using dict comprehension and a conditional argument create a dictionary from the current dictionary
where only the key:value pairs with value above 2000 are taken to the new dictionary."""
dict1={name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh'],
'score': [3000, 9000, 160,2000, 900, 200, 1400, 5000, 800, 190]}
dict2={items>2000}
""""6. Open the file data.txt using file operations."""
file=open("data.txt")


"""7. Define a array ,data = array([11, 22, 33, 44, 55]) find 0 th index 4 th index data"""
array=[11, 22, 33, 44, 55]
print(array[0],array[4])
#11 55

"""8. Write a Python program to filter a list of integers using Lambda.
Original list of integers:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Even numbers from the said list:
[2, 4, 6, 8, 10]
Odd numbers from the said list:
[1, 3, 5, 7, 9]"""

"""9. Write a Pandas program to create the specified columns and rows from a given data frame.
name': ['Anna', 'Dinu', Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', ‘venkat', 'Ajay', 'Dhanesh']
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19]
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1]
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']"""
import pandas as pd
import numpy as np
dict={"name": ['Anna', 'Dinu', 'Ramu', 'Ganu', 'Emily', 'Mahesh', 'Jayesh', 'venkat', 'Ajay', 'Dhanesh'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
d=pd.DataFrame(dict,index=labels)
print(d)
"""name  score  attempts qualify
a     Anna   12.5         1     yes
b     Dinu    9.0         3      no
c     Ramu   16.5         2     yes
d     Ganu    NaN         3      no
e    Emily    9.0         2      no
f   Mahesh   20.0         3     yes
g   Jayesh   14.5         1     yes
h   venkat    NaN         1      no
i     Ajay    8.0         2      no
j  Dhanesh   19.0         1     yes """


"""10. Define a array data = array([11, 22, 33, 44, 55]) and slice it from 1 to 4"""
a=[11, 22, 33, 44, 55]
print(a[1:4])
"""[22, 33, 44]"""