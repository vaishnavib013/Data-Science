# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 09:22:37 2024

@author: Vaishnavi
"""
#why we use csv file,what is absolute path,relative path
#relative path when you are not in working directory then will give relative path
#absolute path when you are not in the working directory ie 1-python in cdrive
import pandas as pd
f1=pd.read_csv('c:/1-python/buzzers.csv')
#to open this file you need to go on variable explorer 
#double click on the f1 there created
#how to read the file 
import pandas as pd
f1=pd.read_csv('buzzers.csv')
###################################
#check for working directory
import os
with open('c:/1-python/buzzers.csv') as raw_data:
    print(raw_data.read())
###################################
#reading this csv file as lists
import csv
with open('c:/1-python/buzzers.csv') as raw_data:
    for line in csv.reader(raw_data):
        print(line)
#####################################
'''ready reference project'''
#reading csv file in the form of dictionary
import csv
with open ('buzzers.csv') as raw_data:
    for line in csv.DictReader(raw_data):
        print(line)
########################################
#keep habit of read csv files
import csv
with open('buzzers.csv') as data:
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights
#######################
import csv
with open("buzzers.csv") as data:
    ignore=data.readline()
    flights={}
    for line in data:
        k,v=line.split(',')
        flights[k]=v
flights

################################
#pre-requisite to decorators
def plus_one(number):
    number1=number+1
    return number1
plus_one(5)
##########################
#defining function inside the fnction

def plus_one(number):
    def add_one(number):
        number1=number+1
        return number1
    #here function inside the function is there so it will create object instead of giving the values
    result=add_one(number)
    return result
plus_one(4)
#######################
#passing functions as arguments
#to other functions
def plus_one(number):
    result1=number+1
    return result1

def function_call(function):
    result=function(5)
    return result
function_call(plus_one)
###############################
#function returning other function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi#here it is returning the function
hello_function()
hello()
#here it will create the hello_function
#so instead of creating itself as an object let it store it in other object and then call it as a function

##function returning other function
def hello_function():
    def say_hi():
        return "hi"
    return say_hi#here it is returning the function
hello=hello_function()
hello()
############################
"""decorators-most important topic """
#need for decorators
import time
def cal_square(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"total time for execution of square is{total_time}")
    return result

def calc_cube(numbers):
    start=time.time()
    result=[]
    for number in numbers:
        result.append(number*number*number)
    end=time.time()
    total_time=(end-start)*1000
    print(f"the total time execution of square is{total_time}")
    return result
array=range(1,100000)
out_square=cal_square(array)
out_cube=calc_cube(array)

###################################27/03
"""decorator very very important for interview"""
#decorator are als called wrapper ()
#a decorator function is a function that
#takes in  a function and
#returns it by adding some functionality
def say_hi():
    return"hello there"    

def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
decorate=uppercase_decorator(say_hi)
decorate()
#however python provides the easier way for writing and using /apply the decorators
#we simply use the @symbol there 
#the function we'd like to decorate
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper

@uppercase_decorator#here we do not need to store it in another variable
def say_hi():
    return 'hello there'
say_hi()
#############################
#applying multiple decorators
#to a single function
#we can use multiple decorators
#the decorator will be applied in the order we have called them
def split_string(function):
    def wrapper():
        func=function()
        splitted_string=func.split()
        return splitted_string
    return wrapper
def uppercase_decorator(function):
    def wrapper():
        func=function()
        make_uppercase=func.upper()
        return make_uppercase
    return wrapper
@split_string
@uppercase_decorator
def say_hello():
    return "hello there"
say_hello()
#so here we have called 1st splited_string so it would be executed 1st
#then uppercase would be applied there
######################################
#*args=if arguments are known then we use it.it is also call arbitary 
#**kwargs=keyword 
###############################


import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took {total_time}mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it 
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)



###############################
#to debug the code-go on debug option click it
#click on the option set/clear breakpoint






