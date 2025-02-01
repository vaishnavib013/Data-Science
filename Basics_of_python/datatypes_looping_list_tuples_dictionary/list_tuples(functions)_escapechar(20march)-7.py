# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 20:06:00 2024

@author: Vaishnavi
"""
"""global variables,local variables,
range datatype,slicing,
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

#
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

#python list
list=["cherry","banana","apple"]
print(list)
#list items are indexed,the first item has index[0],and remaining the same way
print(list[0])
print(list[1])
print(list[2])
print(list[2][2])
#append(): adds an element at the end of the list
list=["cherry","banana","apple"]
list.append("mango")
print(list)
#clear(): removes all the elements from the list
list.clear()
print(list)
#copy method
list=["cherry","banana","apple"]

list2=list.copy()
print(list2)
#count():return the number of times the value of "cherry" occured
list=["cherry","cherry","apple"]
list.count("cherry")
#extend():add the elements of cars to the fruits list
list3=[1,2,3]
list1=[4,5,6]
list3.extend(list1)
print(list3)
#list[]:mixed datatype,mutable,repeated data
#insert():insert the values "orange"
list=["cherry","cherry","apple"]
list.insert(1,"mango")
print(list)
#pop:removes the element at the specified position
list=["cherry","cherry","apple"]
list.pop(2)
print(list)
#remove():removes the item with the specified value
list=["cherry","cherry","apple"]
list.remove("cherry")
print(list)
#reverse():it reverses the list
list=["cherry","cherry","apple"]
list.reverse()
print(list)
#sort():sort the list by alhabethical order
list=["cherry","orange","apple","cine"]
list.sort()
print(list)
#tuple:()-declared in round braces
tup=("cherry","cherry","banana")
print(tup)
print(tup[2])
#tuple is immutable so data cannot be changed,mixed datatypes,to change the tuple need to convert it into the list

#to change the data of the tuple we need to convert the tuple into list
#in adharcard the data is not allowed to change so it can be used there
x=("cherry","cherry","apple")
x[1]="kiwi"
#it will give the error as tuple is immutable
#convert the tuple into the list
y=list(x)
y[1]="kiwi"
#convert list to tuple
x=tuple(y)
print(x)
x=("apple","banana","cherry")
print(x[1])
#to join the two tuples use the + operator
tuple1=("a","b","c")
tuple2=(1,2,3)
tup1=tuple1+tuple2
print(tup1)
#dictionary:it is in the form of key:value pair
dict1={"brand":"maruti","model":"2345","year":2011}
print(dict1)
dict1.get("model")
dict1.keys()
#the number of key:value pair are
print(len(dict1))
print(type(dict1))
#if you are applying the dictionary for large data suppose student data so many rollno,name,class will be required for this we can use this as colname as name and value as "abc"
dict2={"brand":["maruti","toyoto","mahendra"],"model":["a","b","c"],"year":["2011","2013","2022"]}
print(dict2)
print(len(dict2))
dict2.get("model")
dict2.keys()

#######################################################
#21/03/24
car={"brand":"ford",
     "model":"mustang",
     "year":1964
    }
x=car.keys()
print(x)
#to insert/add the new key:value air in the existing dictionary we use dictname["key"]="value"
car["color"]="white"
car
x=car.keys()
print(x)
#to remove the key:value pair from the dictionary
#remove-pop method in dictionary uses the "key/value" pair
#in list remove()-uses the location or the index to delete or remove the element
car.pop("model")#here the model key will be eliminated with its value also ie mustang
print(car)
#accessing keys in the dictionary using for loop
for x in car:
    print(x)
    
#accessing the values in the dictonary using for oop
for x in car:
    print(car[x])
#accessing the key values pair 
'''very important'''
for key,value in car.items():
    print("%s=%s" %(key,value))

#copying the dictionary
#dictname.copy()
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car2=car.copy()
car2
#another way to make a copy is to use the
thisdict={
    "brand":"ford",
    "model":"mustang",
    "year":1964}
dict1=dict(thisdict)
dict1
###########################################

#dictionary inside the dictionary
our_family={
    "child1":{
        "name":"ram",
        "dob":"21-05-2008"},
        "child2":{"name":"sham",
                  "dob":"01-01-2008"
                  }
        }
our_family
######################################
#dictionary methods
#clear():removes all the elements from the car
#dict dont get deleted only the elements gets deleted
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.clear()
car
#empty dictionary will be there
#create the dictionary with 3 keys
x={'key1','key2','key3'} 
y=0
thisdict=dict.fromkeys(x,y)
thisdict
#get():to get the value of dictionary
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.get("model")
#items():return the dictionary key-value
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.items()
car.keys()
#values():it will give all the values in the given dict
car.values()
#update():insert an item to the dictionary
car={
     "brand":"ford",
     "model":"mustang",
     "year":1964
     }
car.update({"color":"white"})
car
car.update({"brand":"maruti"})
car
#everytime new elements will be added at the end
##################################################










