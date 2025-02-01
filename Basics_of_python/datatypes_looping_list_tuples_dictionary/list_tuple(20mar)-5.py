# -*- coding: utf-8 -*-
"""
Created on 20 march 2024 17:37:46 2024

@author: Vaishnavi
"""

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
#extend():add the elements of list1 to the list3 list
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

###############################3
#tuple:()-declared in round braces
tup=("cherry","cherry","banana")
print(tup)
print(type(tup))
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