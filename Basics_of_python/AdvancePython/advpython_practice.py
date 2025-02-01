# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 21:34:27 2024

@author: Vaishnavi
"""
#advancepython practice
import string
import random
a=["hi","itsme","weird"]
b=["dolly","maggie","cheese"]
ab=random.choice(a)
ba=random.choice(b)
num=random.randrange(20)
num1=str(num)
print(ab+ba+num1)
############################

l=[1,4,6,83,67,44,3,4]
def min(l):
    m=l[0]
    for i in l:
        if i>m:
            m=i
    print(m)
min(l)
 ###################### 
l=[1,4,6,83,67,44,3,4]
def min(l):
    m=l[0]
    for i in l:
        if i>m:
            m=i
    print(m)
min(l)
#######################
l=[1,4,6,83,67,44,3,4]

l1=[i for i in l]
l2=[i**2 for i in l]
print(l1)
print(l2)

###########################
d={"key1":1,"key2":2,"key3":3}
d1={k:v for k,v in d.items() }
print(d1)
##############################
#tuples generator to access the values one by one
gen=(x for x in range(5))
print(gen)
for i in gen:
    print(i)
next(gen)
#############################
#for accessing multiple values from a function
def odd(num):
    for i in range(1,num,2):
        yield i
odd(6)
for i in odd(6):
    print(i)
gen=odd(6)
next(gen)
########################
import random
noun=input("enter your name:")
objective=input("enter adjective:")
number=random.randrange(0,100)
password=noun+objective+str(number)
print("the entered password is:",password)
def lengths(value):
    for ele in value:
        yield len(ele)
def hide(value):
    for ele in value:
        yield ele*"*"
for i in hide(lengths(password)):
    print(i,end=" ")
#########################3
pas=["real","therapy"]
def lengths(itr):
    for i in itr:
        yield len(i)
def hide(itr):
    for p in itr:
        yield p*"*"
for i in hide(lengths(pas)):
    print(i,end=" ")
############################
#with enumerate
pas
for i,j in enumerate(pas,start=4):
    print(f"{i} {j}")
###########################
a=[1,2,3,4,5]
b=["papa","baba","dada","mama"]
c=[596749739,84738738,357835827]
for i,j,k in zip(a,b,c):
    print(i,j,k)
#############################
from itertools import zip_longest
for i,j,k in zip_longest(a,b,c,fillvalue=0):
    print(i,j,k)
##########################
#all(),any()
lst=[1,23,0,-8,27,89]
if all(l):
    print("all values are true")
else:
    print("there are null values")
###############3333
from itertools import count
counter=count(0)
next(counter)
#######################3
import itertools
task=["code","learn","projects"]
for i in itertools.cycle(task):
    print(i)
#####################
from itertools import repeat
task=["code","learn","projects"]
for i in repeat(task,times=3):
    print(i)
 ############################   
from itertools import combinations
task=["code","learn","projects"]
comb=[1,2,3]
for i in combinations(task,2):
    print(i)
#############################
from itertools import permutations
task=["code","learn","projects"]
comb=[1,2,3]
for i in permutations(task,2):
    print(i)
########################
from itertools import product
task=["code","learn","projects"]
comb=[1,2,3]
for i in product(task,comb):
    print(i)
##########################
import copy
l
l2=copy.copy(l)
l[0]=10
l2[1]=12
print(l)
print(l2)

list_a=[[1,2,3,4,2],[2,3,4,5]]#two level
l2=copy.copy(list_a)
list_a[0][0]=10
l2[1]=12
print(list_a)
print(l2)

import copy
l
l2=copy.deepcopy(l)
l[0]=15
l2[1]=12
print(l)
print(l2)

import pandas as pd
f1=pd.read_csv('c:/1-python/buzzers.csv')
print(f1)

import os
with open('c:/1-python/buzzers.csv') as raw_data:
    print(raw_data.read())

import csv
with open('c:/1-python/buzzers.csv') as raw_data:
    for i in csv.reader(raw_data):
        print(i)
        
import csv
with open('c:/1-python/buzzers.csv') as raw_data:
    for i in csv.DictReader(raw_data):
        print(i)