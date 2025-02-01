# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 08:26:51 2024

@author: Vaishnavi
"""
"""write python code using logical operator 
and if elif.so """
print("welcome to the roller coster")
height=int(input("enter your height in cm:"))
if(height>=120):
    print("you are eligible for the roller coster")
    age=int(input("enter your age"))
    bill=0
    if(age<10 and age>8):
        bill+=20
        print("you have to pay charges Rs",bill)
    elif(age>=10 and age<=15):
        bill+=10
        print("you have to pay Rs",bill)
    elif(age>15):
        bill+=5
        print("you have to pay the amount Rs",bill)
    else:
        print("you are not eligible as per your age")
else:
    print("you are not eligible as per your height ")
  #include the photo cost  
photo=input("do you want photos'y' or'n'?")
popcorn=input("do you want popcorn'y' or'n'?")
if (photo=='y'):
    p=5
    bill+=p
    print("the total cost including photo is:",bill)
else:
    print("the total cost will be excluding the phto:",bill)
if(popcorn=='y'):
    cost_pop=10
    bill+=cost_pop
    print("the grand total including popcorn will be:",bill)
else:
    print("the grand total not including popcorn is:",bill)
   
#include the popcorn facility
"""popcorn=input("do you want popcorn'y' or'n'?")
if(popcorn=='y'):
    cost_pop=10
    bill+=cost_pop
    print("the grand total will be:",bill)
else:
    print("the grand total is:",bill)"""
############################################# 
height=float(input("enter the height in m:"))
weight=float(input("enter your weight in kg:"))
BMI=round((weight/(height*height)),2)
if BMI<18.5:
    print("you are under weight and your BMI is:",BMI)
elif BMI>18.5 and BMI<25:
    print("you are normal and your BMI is:",BMI)
elif BMI>25 and BMI<30:
    print("you are overweight and your BMI is:",BMI)
elif BMI>30 and BMI<35:
     print("you are obese and your BMI is:",BMI)  
elif BMI>35:
    print("you are clinically obese and your BMI is:",BMI)
################################################
lst1=[1,2,3,3,5,6,7]
print(len(lst1))
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
#########
lst1=[1,2,3,5,6,7]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
####################unsorted list then also applicable 
lst1=[6,7,1,2,3,3,5]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
#################################
#it will check the neighbour numbers 
#if they are equal else ifever the 
#repeated values are there but not in 
#neighbour then would result into false
lst1=[6,7,3,1,2,3,5]
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
#so to show the correct result we need to sort it by sort()
lst1=[6,7,3,1,2,3,5]
lst1.sort()
lst1
def is_duplicate(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(is_duplicate(lst1))
##########################
#leap year

def is_leap_year(year):
    if ((year>0) and (year%4==0) and (year%100!=0)or(year%400==0) ):
        return True
    return False
is_leap_year(2022)
is_leap_year(2024)
###############################
#mario pyramid
for i in range(4):
    for j in range(4):
        print("#",end=" ")
    print()
    
for i in range(4):
    for j in range (i+1):
        print("#",end=" ")
    print()
    
for i in range(4):
    for j in range(4-i):
        print("#",end=" ")
    print()
    #
   # #
  # # #
 # # # # homework
  # # #
   # #
    #
    
    #homework
rows=4
for i in range(1,rows+1):
    print(" "*(rows-i) + "# "*i)
for i in range(1,rows+1-1):
    print(" "*i+"# "*(rows -i))    
#####tried in tp 
rows=4   
for i in range(1, rows + 1):
    print(" " * (rows - i) )
    print("# " * i)
#####from google
rows = 4
# Upper part of diamond
for i in range(1, rows + 1):
    print(" " * (rows - i) + "# " * i)
#Lower part of diamond
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "# " * i)
    
######################
for i in range(7):
    for j in range(4):
        print(end=" "*(j-1))
        print("#")
    print( )
 #to find the minimum value there is already a minimum function   
lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("the minimum value ",min)
min_max(lst)
############################
lst=[23,45,2,1,5,7,8,12]
#to find the maximum value
def min_max(lst):
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("the maximum value ",max)
min_max(lst)
###############
#palindrome
a=input("enter the string :")
b=a[::-1]
if(a==b):
    print("it is palindrome")
else:
    print("not a palindrome")
    
#str[::1]==str[::-1]logic can also be used
users=["members","staff","admin","employee"]
for user in users:
    if user=="staff":
        print("hello staffs")
    elif user=="members":
        print("hello members")
    elif user=="admin":
        print("hello admin")
    elif user=="employee":
        print("hello employee")
    else:
        print("hello")
#######################################  
user=input("enter your post:")
if user=="staff":
     print("hello staffs")
elif user=="members":
     print("hello members")
elif user=="admin":
     print("hello admin")
elif user=="employee":
     print("hello employee")
else:
     print("hello")
     
import string  
#design a password
adjectives=['sleepy','moody','classy','slow','smelly','red','fat',
            'orange','yellow','green','dragon','panda','duck','hammer']
nouns=['apple','dinosour','ball','toaster','dolly','goat']
import random
#pick the words
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
password=adjective + noun + str(number) + special_char
print("the password generated is:%s"%password)
##################################################
adjectives=['sleepy','moody','classy','slow','smelly','red','fat',
            'orange','yellow','green','dragon','panda','duck','hammer']
nouns=['apple','dinosour','ball','toaster','dolly','goat']

import random
#pick the words
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select a number
number=random.randrange(0,100)
#select a special character
special_char=random.choice(string.punctuation)
password=adjective + noun + str(number) + special_char
x=input("would you like to generate another password'y' or 'n'?")
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    noun=noun.upper()
    n=random.choice(nouns)
    number=random.randrange(0,100)
    special_char=random.choice(string.punctuation)
    password=adjective + noun + str(number) + special_char+ n
    print("your new password is:",password)
    x=input("would you like to generate another password'y' or 'n'?")
    if x=="n":
        break
    break


#####################################
