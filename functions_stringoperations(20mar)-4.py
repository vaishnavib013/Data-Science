# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:06:00 2024

@author: rutuo
"""
"""global variables,local variables,
range datatype,slicing,int & string concatinate
string-upper(),lower(),strip,lstrip(),rstrip,
replace(),split(),find(),

>reverse the string we use the slicing
>to concate the string and number using using f method,
format method,format method using the ids(location)
>escape character /" /"
>operator precedence
>to add space between two words
>python identity operators
>list-
append(),clear(),extend(),count(),copy(),insert(),pop(),
"""
#global variables
x="awesome"
def my_function():
    print("python is "+x)
my_function()

"""note:if there is local and global variable
then the priority is given to the local variable in the function
but out of the function the glocal variable will be accessible"""
x="awesome"

def my_function():
        x="fantastic"
        print("python is "+x)
my_function()
print("python is "+x)

#range
x=5
print(type(x))
x=range(6)
print(range(6))
print(type(x))
x={"name":"ram","age":34}
print(type(x))


#here the integer and string can not be concatinated
#as same type of datatype gets concatinated
#string+string/int+int
str1="hello"
str2=2
str3=str1+str2
print(str3)
#it will show the error as str and int cannot be concatinated
#by typecasting we can concatinate the string
str1="hello"
str2=2
str4=str(str2)
str3=str1+str4
print(str3)
#string
#if you want multiple strings
x="""this is python.it is very powerfull"""
print(x)
#################
#string slicing
x="""this is python.It is very powerful"""
print(x[2:8])
#slicing from the start
#output will be "is is "
print(x[:9])
print(x[:3])
#bydefault it will start from 0 if not mentioned
#the output will b from 0-8 indexes
#ie."this is p"
#slicing at the end
print(x[2:])
print(x[4:])
#reverse the string do it from the negative indexing
print(x[::-1])
#negative indexing
print(x[-5:-2])
#modify string
#upper()-each letter will get capitalized
print(x.upper())
x=x.upper()
print(x.lower())
#remove the white spaces.use the strip function to remove the initial white spaces
#so strip ()only removes the left spaces
#strip()
x="     this is python   "
print(x.strip())
#lstrip() to remove the left spaces
print(x.lstrip())
#rstrip()to remove the right spaces
print(x.rstrip())
 
#replace()
#to change or replace the words we use replace function()
x="hello world"
print(x.replace("hello","gello"))

#use of split which gives space between two words
#it replaces white spaces 
x="hello world"
print(x.split(" "))
#if space is found it will separate there into two words
#if ,found whereever it will split there
x="hello world"
print(x.split(" ,"))

#reverse string by stepping
x="hello world"
print(x[::-2])
print(x[::-1])

x="Hello World"
string1=x[::-2]
print(string1)

#find method,searching the string for a specific value
x="this is a python and it is very powerful"
print(x.find("and"))
#string concateness
x="hello"
y="world"
print(x+y)
#to add the white space between two words
print(x+" "+y)
#string format
x=36
y="my name is anthony"
print(x+y)
#it will give the error
print(f"{y} and my age is {x}")
print(f"my name is anthony and my age is {x}")
#if you want to concate the string and number which generally gives error can be done by f
quantity=3
item_no=54
price=67
print(f"i want {quantity}pieces and item number is {item_no} and, its price is{price}")
#concatinate string using format method
my_order="i want {} pieces and item number{},its price is{}"
print(my_order.format(quantity,item_no,price))


########################################
#by using the format method using the ids ie the locations
quantity=3
item_number=54
price=67
my_order="i want {0} pieces and item number{1},its price is{2}"
print(my_order.format(quantity,item_no,price))
###############################

#escape character allows you to use double quotes when we required to as it print them 
text="this is fun fair and it has got big \"round rigo\""
print(text)
#o/p:this is fun fair and it has got big "round rigo"
###########################33

#boolean output by python operators
9==10
9>10
9<10
#####
#python operator
a=20
b=10
print(a!=b)
#operator precedence
print(3*3+3/3-3)
"""rules for mathematical operations
PEMDAS
p:paranthesis
e:exponential
m:multiplication
d:division
a:addition
s:substraction"""
#identity operators
a=3
b=4
print(a is b)#it gives us false
print(a is not b)#it givrs true

################################










