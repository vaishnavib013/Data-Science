# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:26:10 2024

@author: ishwa


"""

---------------------------------------------------------
----------------'''9th Session ,25/03/2024'''----------
--------------------------------------------------------
#list Comprehenssion

lst=[num for num in range (0,20)]
print(lst)

#####################

names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst)
 
#list comprehesion with if statement\

def is_even(num):
    return num%2==0
lst=[num for num in range(10) if is_even(num)]
print(lst)        

lst=[f"{x}{y}"for x in range (3)for y in range(3)]
print(lst)

#############################################
#Dictionary Comprehension
dict={x:x*x for x in range(3)}
print(dict)



###############################################
#Generator

gen=(x for x in range(3))
print(gen)
for num in gen:
    print(num)

gen=(x for x in range(3))
next(gen)
next(gen) #it gives step by step value

###############################
#Function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
for num in range_even(6):
    print(num)
    
gen=range_even(6) #instead of using for loop we can write our own generator
next(gen)
next(gen)

#########################################
#Chainning Generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*'*'
    
'''ele appears to be a placeholder for an element from
an iterable .the astrick(*) is likely just a character
used to represent a placeholder or a wildcard.
for instance ,if you are iterating over a list of elements
,"ele*" could symbolize any element i that list .its a
generic representation that doesn't correspond to any
specific syntax in python or itertools
'''
  
password=["not-good","give'm-mass","0010=123"]
for password in hide(lengths(password)):
    print(password)
    
    
import string
adjectives=input("Enter the Adjective :")
nouns=input("Enter the Noun :")
#pick the words
import random
number=random.randrange(0,100)
#select a special character
special=random.choice(string.punctuation)
#create the password
password=adjectives+nouns+str(number)+special
print('Your new password is : %s'%password)
for password in hide(lengths(password)):
    print(password,end=" ")


---------------------------------------------------------
--------------'''10th Session,25/03/2024'''------------
---------------------------------------------------------
gen =(x for x in range(3))
print(gen)
next(gen)
next(gen)
'''for i in range(0,10,2):
    yield i'''
    
###############################################################################

#Enumerate
lst=["apple","banana","cherry"]
for index,item in enumerate(lst,start=1):
    print(f'{index} {item}')
###############################################################################

#zip function

lst1=['abc','xyz','lmn']
lst2=[123,456,789]
for name,number in zip(lst1,lst2):
    print(name,number)


lst1=['abc','xyz','lmn']
lst2=[123,456,789,321]
for name,number in zip(lst1,lst2):
    print(name,number)
#won't display last data in lst2
#solution
import itertools as it
for name,number in it.zip_longest(lst1,lst2): #show 321 with None
    print(name,number)
#  
for name,number in it.zip_longest(lst1,lst2,fillvalue=0): #show 321 with None
    print(name,number)
    
###############################################################################

#all() function
lst=[1,-2,5,-3,4]
if all(lst):
    print('all values are true')
else:
    print('there are zero values')
#
lst=[1,-2,5,-3,0,4]
if all(lst):
    print('all values are true')
else:
    print('there are zero values')
    
###############################################################################

#any() function
lst=[0,0,0,3,0,0]
if any(lst):
    print('it has some non zero value')
else:
    print('useless')
#
lst=[0,0,0,0,0]
if any(lst):
    print('it has some non zero value')
else:
    print('useless')

###############################################################################

#count() function
import itertools as it
counter=it.count(start=1)  #start=1 (0 by defult)
print(next(counter))

###############################################################################

#cycle() function
import itertools as it
instructions=['eat','code','sleep']
for a in it.cycle(instructions):
    print(a)
    
###############################################################################

#reprat() function
import itertools as it
for msg in it.repeat("Jai Hind", times=5):
    print(msg)
    
###############################################################################
#permutations and combinations

import itertools as it
players=['John','Jani','janardhan','Jaikal']
for i in it.permutations(players,2):
    print(i)
#
import itertools as it
players=['John','Jani','janardhan','Jaikal']
for i in it.combinations(players,2):
    print(i)

###############################################################################

#product()

team1=['Bumrah','pandya','Shami']
team2=['Rohit','Kohli','Dhoni'] 
for pair in it.product(team1,team2):
    print(pair)
---------------------------------------------------------------
###shallow and deep copy
'''In python assignment statement (a=b) do not create
real copies
it only creates a new variable with same reference.
so when u want to make actual copies of mutable objects
(list,dicts)
and want to modify the copy without affecting the original
you have to be careful.
for "real"copies we can use the copies module.
however,for compound/nested objects (eg nested lists or dicts) and
custom objects there is an imp difference between shallow
and deep copying.

shallow copy->only one level deep.it creates a new 
copy and populates it with references to the nested objects.
this means modyfying a nested obj in the copy deeper 
than modification in original also
deep copy->a full independent clone.it creates a new 
copy and then recusively populates it with copies of 
nested'''

#assignment operation
#This will create a new variable with the same reference
list_a=[1,2,3,4,2]
list_b=list_a
list_a[0]=-10
print(list_a) 
print(list_b)

import copy as cp
list_a=[1,2,3,4,5]
list_b=cp.copy(list_a)

#not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)


#with nested object modifying level two
import copy as cp
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=cp.deepcopy(list_a)

list_a[0][0]=-10
print(list_a)
print(list_b)

--------------------------------------------------------------------
----------------'''11th session,26th March 2024'''------------------
--------------------------------------------------------------------

#Read CSV File
import pandas as pd
data=pd.read_csv('buzzers.csv') 
data

#check the working directory
import os
with open('C:/1-Python/buzzers.csv')as raw_data:#Absolute path
    print(raw_data.read()) 
   
#Read CSV data as Lists :'
import csv
with open('C:/1-Python/buzzers.csv')as raw_data:
    for line in csv.reader(raw_data):
        print(line)

#Read CSV data as Dictionary :
import csv
with open('C:/1-Python/buzzers.csv')as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)

#######################################################################
with open('C:/1-Python/buzzers.csv')as raw_data:
    #ignore=data.readline()
    flights={}
    for line in raw_data:
        k,v=line.split(',')
        flights[k]=v
flights


def plus_one(number):
    number1=number+1
    return number1
plus_one(5)

def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    result=add_one(number)
    return result
plus_one(4)

#passing function asargument to other function
def plus_one(number):
    result=number+1
    return result

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)

#Function Returning other function
def hello_function():
    def say_hi():
        return "Hi"
    return say_hi()
hello=hello_function()
hello

#Need for decorators
import time
def calc_sq(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"Total time for execution of square is :{total_time}")
    return result

array=range(1,1000)
out_square=calc_sq(array)

---------------------------------------------------------------------
----------------------'''14th ,27th march 2024'''--------------------------
---------------------------------------------------------------------

#A python decorator is a function that takes is a function and
#returns it by adding some functionality

def say_hi():
    return 'hello there'
def upper_decorator(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
decorator=upper_decorator(say_hi)
decorator()

#simple way tpo use decorator
#for us to apply decorator
#we simply use the @ symbol before the function
#we'd like to  decorate

def upper_decorator(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
@upper_decorator
def say_hi():
    return 'hello there'
say_hi()

#Applying Multiple decorator to use a single function
#we can use multiple decorators to a single function
#decorators will be applied in the order that 
#we have called them

def split_str(function):
    def wrapper():
        func=function()
        splitted_str=func.split()
        return splitted_str
    return wrapper
def upper_decorator(function):
    def wrapper():
        func=function()
        make_upper=func.upper()
        return make_upper
    return wrapper
@split_str
@upper_decorator
def say_hi():
    return 'hello there'
say_hi()


import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took {total_time} mil sec")
        return result
    return wrapper 
@time_it 
def calc_sq(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cu(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,1000)
out_sq=calc_sq(array)
out_cu=calc_cu(array)




from wrapper import time_it
@time_it 
def calc_sq(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it
def calc_cu(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,1000)
out_sq=calc_sq(array)
out_cu=calc_cu(array)


------------------------------------------------------
-------------------"28th March , 2024"---------------
------------------------------------------------------

#Exception Handling

try:
    numerator=50
    denominator =int(input("Enter the denominator :"))
    print(numerator/denominator)
    print("Division Performed Succesfully")
except ZeroDivisionError:
    print("Denominator zero is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
#############################################
try:
    numerator=50
    denominator =int(input("Enter the denominator :"))
    print(numerator/denominator)
    print("Division Performed Succesfully")
except ValueError:
    print("Only INTEGERS should be entered")  
except :
    print("Denominator zero is not allowed")

################################################
#Handling Exception using try...except....else

try:
    numerator=50
    denominator =int(input("Enter the denominator :"))
    quotient=numerator/denominator
    print("Division Performed Succesfully")
except ZeroDivisionError:
    print("Denominator zero is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("The result of division operation is",quotient)

#Handling Exception using try...except....finally
try:
    numerator=50
    denominator =int(input("Enter the denominator :"))
    quotient=numerator/denominator
    print("Division Performed Succesfully")
except ZeroDivisionError:
    print("Denominator zero is not allowed")
except ValueError:
    print("Only INTEGERS should be entered")
else:
    print("The result of division operation is",quotient)
finally:
    print("Over And Out")


#####################################################

#OOP in Python
