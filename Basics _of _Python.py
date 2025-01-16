# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 09:41:50 2024

@author: Vaishnavi 
"""

print("Hello World")
x=1.5
print(x)
print(type(x))
x=1000000000000000000000000
print(x)
print(type(x))

age = input('Enter your age')
print(type(age))
print(age)

age1 = input('Enter your age1')
print(type(age1))
print(age1)
print (age+age1)

age2 = int(input('Enter your age2'))
print(type(age2))
print(age2)
#by default data type of input  is string
age3 = int(input('Enter your age3'))
print(type(age3))
print(age3)
print(age2+age3)

#######################################

#conversion of string and int into thr float 

int_value=100
string_value='1.5'
float_value=float(int_value)
print('int value of float is :',float_value)
print(type(float_value))
float_value=float(string_value)
print('string value as a float :',float_value)
print(type(float_value))

######################################

#complex numbers

c1=1
c2=2j
print('c1 :',c1,'cs :',c2)
print(type(c1))
print(type(c2))
print(c1.real)
print(c2.imag)

######################################

#boolean values

all_ok=True
print(all_ok)
all_ok=False
print(all_ok)
print(type(all_ok))

######################################

status=bool(input('ok it is confirmed'))
print(status)
print(type(status))

######################################

h=10
a=15
print(h+a)
print(type(h+a))
print(10*4)
print(type(10*4))
g=10
b=7
print(g-b)
print(type(g-b))
print(100/20)
print(type(100/20))


######################################

#integer division operator

print(100//20)
print(type(100//20))

######################################


print ('MOdulaus division 100%13',100%13)
print ('MOdulaus division 3%2',3%2)
#modulus operation for calculating the remainder


######################################

#power operator(**)
a=5
b=3
print(a**b)

#####################################
x=0
x+=1
print(x)
#####################################

winner=None
print(winner)
print(winner is None)
print(winner is not None)
print(type(winner))#none type

#######################################

num=int(input('Enter a number :'))
if num>0:
    print(num)
    
num=int(input('Enter a number :'))
if num>0:
    print(num)
else:
    print("It is negative")
    
    
num=int(input('Enter a number :'))
if num<0:
    print("it is negative")
else:
    print("It is not negative")
    
#######################################

#elif ladder

saving=float(input("Enter how much you have in saving"))
if saving==0:
    print("Sorry no savings")
elif saving<500:
    print('well done')
elif saving<100:
    print('thats a tidy sum')
elif saving<10000:
    print("Welcome sir")
elif saving <100000:
    print(saving,"It is very very good")
else:
    print("Bye")
    
#######################################

#while loop

count=1
print('Starting')
while count<=10:
    print(count)
    count +=1
    
#######################################

#for loop
print('Print out values in range')
for i in range(2,10):
    print(i)
print('Done')
    
#######################################

print('only print code if all iterations completed')
num=int(input("enter a number to check for :"))
for i in range(0,16):
    if i==num:
        break
    print(i)
print('Done')
#######################################

#anonymous code

for _ in range(0,10):
    print("$")
    print(" ")
    
for _ in range(0,10):
    print(".",end=" ")
    print()
    
"""-----------------------------------------------------
----------------'''5th Session 20/03'''---------------
------------------------------------------------------
"""

#odd numbers in range
start ,end=4,19
for num in range(start,end+1):
    if num%2!=0:
        print(num,end=" ")
        
#####################################
#even numbers in range
start,end=4,22
for num in range(start,end+1):
    if num%2==0:
        print(num)
        
#####################################
x,y,z=5,6,7
print(x)
print(y)
print(z)
x,y,z=5
print(x)
print(y)
print(z)
###############################
#global variable
x="awesome"
def my_function():
    print("python is "+x)
my_function()

###############################
#local variable and local variable
x="awesome"
def my_function():
    x="funtastic"
    print("python is "+x)
my_function()
print("python is "+x)

#####################################
#getting data types
x=5
print(type(x))
x=range(6)
print(x)
print(type(x))
x={"name":"Ishwar","age":"20"}
print(x)
print(type(x))
####################################
#string concate
str1="Hello"
str2=2
print(str1+str2)
##################
str1="Hello"
str2=str(2)
print(str1+str2)

#####################################
#if you want muptiple strings
x="""This is python .It is very Powerful"""
print(x)
print(x[2:8])
print(x[:3])   #slicing from the start
print(x[4:])   #slicing to the end
print(x[-5:-2]) #negative indexing
print(x.upper())
#x=x.upper()
print(x.lower())
###################################
#remove white spaace ,removes white spaace from intitial part of string
x="  this is python"
print(x.strip())

##################################
#replace the string
x="Hello world"
print(x.replace("Hello","Namaste"))
##################################
#use of split which replaces space
x="Hello world"
print(x.split(" "))
############################
x="Hello world"
string1=x[::-2]
print(string1)

x="NAYN" 
string1=x[::-1]  #string reversing
print(string1)


#find method searches the string for a spaecified value

x="This is python and it is powerful"
print(x.find("and"))

######################################
#string concatness
x="Hello"
y="World"
print(x+y)
print(x+" "+y)    #string with white space

##############################
#string format
x=19
y="My name is Ishwar"
#print(x+y) #it will give error
print(f" {y} and my age is{x}")

quantity=3
item_no=54
price=67
print(f"I want {quantity} and item number is{item_no} its price is{price}")

my_order="I want {} and item number is{} its price is{}"
print(my_order.format(quantity,item_no,price))

quantity=3
item_no=54
price=67
print(f"I want {0} and item number is{1} its price is{2}")
print(my_order.format(quantity,item_no,price))

text="This is fun fair and it has got big\"round rigo\""
print(text)

'''Rule for mathmatical operation 
PEMDAS
P=Parenthesis
E=Exponential
M=Multiplication
D=Division
A=Addition
S=Substraction
'''
print(3*3+3/3-3)

---------------------------------------------------
----------------'''PYTHON LIST'''--------------------
              
lst=["cherry","banana","apple"]
print(lst)
#list items are indexed,the first item has index [0]
print(lst[0])
print(lst[1])

lst=["cherry","banana","apple"]
lst.append("Mango")
print(lst)

lst=["cherry","banana","apple"]
lst.clear()  
print(lst)

#copy method
lst=["cherry","banana","apple"]
lst2=lst.copy()
print(lst2)

#count reppeated items
lst=["cherry","cherry","apple"] 
lst.count("cherry")

lst=[0,1,2,3]
lst1=[4,5,6,]
lst.extend(lst1)
print(lst)


#insert Function
lst=["cherry","cherry","apple"] 
lst.insert(1,"mango")
print(lst)

#Delete from list
lst=["cherry","cherry","apple"] 
lst.pop(1)
print(lst)

lst=["cherry","apple","cherry"] 
lst.remove("cherry")
print(lst)
# reverse the list
lst=["cherry","cherry","apple"] 
lst.reverse()
print(lst)

#sorting of list alphabeticalyy sort()
lst=["cherry","orange","apple"] 
lst.sort()
print(lst)


--------------------------------------------------
-----------------'''PYTHON TUPLE'''---------------


tup=("cherry","cherry","apple")
print(tup)
print(tup[2]) 

#once the tuple is created we cannot change its value
x=("banana","cherry","apple")
#x[1]="kiwi"
#first convert it into list
y=list(x)
y[1]="kiwi"
#convert list to tuple
x=tuple(y)
print(y)
 
#to join to tuple we can use + operator
tuple1=("a","b","c")
tuple2=(1,2,3)
tup=tuple1+tuple2
print(tup)


--------------------------------------------------
---------------'''PYTHON DICTIONARY'''---------------

dict1={"Brand":"Maruti","Model":"2345","Year":2011}
print(dict1)
print(len(dict1))
print(dict1.get("Model"))
print(dict1.keys())

dict1={"Brand":["Hyundai","Maruti","Toyato"],
       "Model":["a","b","c"],
       "Year":[2011,2012,2022]}
print(dict1)

------------------------------------------------------
--------------'''6th session, 21-03-2024'''------------
------------------------------------------------------

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
x=car.keys()
print(x)
car["color"]="White"
#car
x=car.keys()
print(x)

#Removing Dictionary element

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.pop("Brand")
print(car)

#Accessing keys from dictionary 
for x in car:
    print(x)
    
#Accessing values from dictionary
for x in car:
    print(car[x])

#if you want to access both keys and values(VI)
for key,value in car.items():
    print("%s=%s" %(key,value))
    
#copying the dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car2=car.copy()
car2
print(car2)

#Another way to make a copy of dictionary
thisdict={"Brand":"Ford","Model":"Mustang","Year":"1964"}
dict1=dict(thisdict)
print(dict1)

#A dictionary can contain dictionaries this is called'
#as nested dictonary
our_family={"Child":{ "Name":"Ram","Dob":"02-12-2000"},
           "Child2":{"Name":"Sham","Dob":"03-04-2000"}}
print(our_family)

#clear() removes all elements from the car

car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.clear()
print(car)

#create a dictionary from key method
x={'key1','key2','key3'}
y=0
thisdict=dict.fromkeys(x,y)
print(thisdict)
       
#get()=to get values from dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.get("Model")

#items()=returns thr dictinary's key-value
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.items()

#values()=Display all values od dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.values()

#update()=insert item in dictionary
car={"Brand":"Ford","Model":"Mustang","Year":"1964"}
car.update({"color":"white"})
print(car)

#merging of two dictionaries
dict1={"one":1,"two":2}
dict2={"three":3,"four":4}
dict3=dict1|dict2
print(dict3)

--------------------------------------------------
#for loop
fruits=["Apple","Banana","cherry"]
for i in fruits:
    print(i)
    
#use of break statement
fruits=["Apple","Banana","cherry"]
for i in fruits:
    #print(i)
    if (i=="Banana"):
        break
    print(i)
    
fruits=["Apple","Banana","cherry"]
for i in fruits:
    if (i=="Banana"):
        break
    print(i)
    
#use of continue statement
fruits=["Apple","Banana","cherry"]
for i in fruits:
    print(i)
    if (i=="Banana"):
        continue

fruits=["Apple","Banana","cherry"]
for i in fruits:
    if (i=="Banana"):
        continue
    print(i)
    
----------------'''Afternoon Session'''---------------
#range function
for x in range(2,30,3):
    print(x)

#loop inside loop (Nested loop)
colors=["green","yellow","red"]
fruits=["guava","banana","apple"]
for x in colors:
    for y in fruits:
        print(x,y)
       

#Function

def my_function():    #function without arguement
    print("Print hello from a function")
my_function()

def my_function(name): #function with single argument
    print("Hello"+name)
my_function(" Ishwar")

def my_function(name1,name2): #function with two arguments
    print(name1+" "+name2)
my_function("Hello ","World")

#Arbitary Arguments,*args 
#if you dont know how many arguments that will be 
#passedinto your function , add a *before the 
#parameter name 

def my_function(*kids):
    print(kids[0]+ " "+kids[2])
my_function("Hello","World","India")

#kwargs **

def my_fnction(**kwargs):
    for key,value in kwargs.items():
        print("%s==%s"%(key,value))
my_fnction(first ='Popatlal',mid='Mohanlal',last='Goyal')
    
#Function with default argument

def my_function(country="Norway"):
    print("I am from "+country)
my_function()
my_function("India")
my_function("Usa")

#passing list as an argument
#you can pass any data types as an argument

fruits=["Apple","Banana","cherry"]
def my_fnc(fruits):
    for x in fruits:
        print(x)
my_fnc(fruits)

#return values
#to let a function return a value,use the return
# statement
def my_fnc(x):
    return x*5
my_fnc(5)

#Pass Function
def my_fnc():  #empty function
    pass
#an empty function without pass function will give error

#Factorial 
#Recursive Function : function in function
def factorial(x):
    if x==1:
        return 1
    else:
        return(x*factorial(x-1))
factorial(4)
    
#Lambda function
#lambda function is a small anonymous function 
#it can take any numver of arguments but can only have
#but only have one expression

def add(a):
    sum=a+10
    return sum
add(20)

add=lambda a:a+10
print(add(20))

#lambda function can have number of arguments
add=lambda a,b:a+b
print(add(20,20))

#finding odd number from list
lst=[34,12,64,55,75,13,63]
odd_lst=list(filter(lambda x:(x%2!=0),lst))
print(odd_lst)
#the filter() method accepts two arguments in  python
#a function and an iterable such as list
lst=[34,12,64,55,75,13,63]
even_lst=list(filter(lambda x:(x%2==0),lst))
print(even_lst)


lst=[34,12,64,55,75,13,63,42,75,20]
sqr=list(filter(lambda x:(x**2),lst))
print(sqr)

lst=[34,12,64,55,75,13,63,42,75,20]
sqr=list(map(lambda x:(x*x),lst))
print(sqr)

------------------------------------------------------
----------------'''7th Session,22/03/24'''------------
------------------------------------------------------

'''
Write python code using logical operators and if elif.
so as to check height as weel as
so as to allow for roller coater also ask user age 
and charge ticket accordingly'''


print("Welcome to the roller coaster")
height=int(input("Please entyer your height :"))
if height>=120:
    bill=0
    print("You are eligible for roller coaster !")
    
    
    age=int(input("Eneter your age in years :"))
  
    if age<=12:
        print("childs ticket is $5")
        bill+=10
    elif age>=18:
        print("Your ticket is $7")
        bill+=15
    elif age<=60:
        print("Your ticket is $10")
        bill+=20 
    else:
        print("As you are old you are not eligible ! ")
    print("Do you need popcorn ?")
    p=int(input("Enter 1 for popcorn :"))
    if p==1 :
        print("Enjoy your Popcorns ")
        bill+=5
        print(f"You need to pay {bill} ")
    else:
        print(f"You need to pay {bill}")
    print("Do you need photo ")
    Need_photo=(input("Enter Y or N :"))
    if Need_photo=='Y':
        bill+=3
        print(f"You need to pay {bill}")
    else:
        print(f"You you need to pay {bill}")
        
        
----------------'''BMI calculator'''------------------

Height=float(input("Enter your height in m :"))
Weight=float(input("Enter your weight in kg :"))
BMI=round((Weight/(Height*Height)),2)
if BMI <18.5:
    print(f"You are under weight and your BMI is{BMI} !")
elif BMI>18.5 and BMI<25 :
    print(f"you are normal weight and your BMI is {BMI} !")
elif BMI>25 and BMI<30:
    print(f"You are over weight and your BMI is {BMI} !")
elif BMI>30 and BMI<35:
    print(f"You are obese and your BMI is {BMI} !")
elif BMI>35:
    print(f"You are clinically obese and your BMI is {BMI} !")

------------'''Duplicates is list'''------------------

lst1=[1,2,3,4,5,7,5,3]
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))


lst1=[1,2,3,4,5,5]
lst1.sort()
lst1
def dup_lst(lst1):
    for i in range(len(lst1)-1):
        if(lst1[i]==lst1[i+1]):
            return True
    return False
print(dup_lst(lst1))

---------------------'''leap Year'''------------------
def is_leap_year(year):
    if((year>0) and (year%4==0) and (year%100!=0) or (year%400==0)):
        return True
    return False
print(is_leap_year(2024))

---------------'''Mario Pyramid'''--------------------

for i in range(4):
    for j in range(4):
        print("*",end=" ")
    print()
    
for i in range(4):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
for i in range(4):
    for j in range(4-i):
        print("*",end=" ")
    print()

'''Diamond'''


---------'''Finding The Minimum and Maximum '''-------

lst=[23,45,2,1,5,7,8,12]
def min_max(lst):
    min=lst[0]
    for i in lst:
        if i<min:
            min=i
    print("The minimum value ",min)
    
    max=lst[0]
    for i in lst:
        if i>max:
            max=i
    print("The minimum value ",max)
min_max(lst)

----------------'''Palindrome'''---------------------

def palindrome(input):
    if input==" ":
        print("You enetered wrong string")
    else:
        string=input[::-1]
        if string==input:
            return True
    return False
    
palindrome("pets on no steps")

n=input("Enter the string")
def palindrome(n):
    if n==n[::-1]:
        print("It is Palindrome")
    else:
        print("It is not palindrome")
palindrome(n)

--------------------'''Password'''----------------------------
    
users=["Admin"]#\"Manager","Employee","Staff"]
#user=input("Enter your password")
for user in users:
    if user=="Admin":
        print("Welcome Admin")
    elif user=="Manager":
        print("Welcome Manager")
    elif user=="Employee":
        print("Welcome employee")
    elif user=="staff":
        print("Welcome staff")
    else:
        print("Password Incorrect")
        
#user=["Admin","Manager","Employee","Staff"]
user=input("Enter User :")
if user=="Admin":
    print("Welcome Admin")
elif user=="Manager":
    print("Welcome Manager")
elif user=="Employee":
    print("Welcome employee")
elif user=="staff":
    print("Welcome staff")
else:
.
    print("Password Incorrect")
    
----------------'''Password Picker'''-----------------


import string
adjectives=['sleepy','slow','smelly','wet','fat','red',
            'orange','yellow','green','purple','blue',
            'fluffy','proud','brave']
nouns=['apple','dinosour','ball','toatster','goat',
       'dragon','hammer','duck','panda']
#pick the words
import random
adjective=random.choice(adjectives)
noun=random.choice(nouns)
#select number
number=random.randrange(0,100)
#select a special character
special=random.choice(string.punctuation)
#create the password
password=adjective+noun+str(number)+special
print('Your new password is : %s'%password)
    

import string
adjectives=['sleepy','slow','smelly','wet','fat','red',
            'orange','yellow','green','purple','blue',
            'fluffy','proud','brave']
nouns=['apple','dinosour','ball','toatster','goat',
       'dragon','hammer','duck','panda']
#pick the words
import random
print("Welcome to the password picker")
while True:
    adjective=random.choice(adjectives)
    noun=random.choice(nouns)
    #select number
    number=random.randrange(0,100)
    #select a special character
    special=random.choice(string.punctuation)
    #create the password
    password=adjective+noun.upper()+str(number)+special
    print('Your new password is : %s'%password)
    response=input("Would you like to generate another password ?")
    if response=="n":
        print('Your new password is : %s'%password)
        break
    else:
        password=adjective+noun.upper()+str(number)+special
        print('Your new password is : %s'%password)
    

    
    
        
      

      
            
        
    
        
    

















