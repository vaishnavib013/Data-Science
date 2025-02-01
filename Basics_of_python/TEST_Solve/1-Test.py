# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 08:23:52 2024

@author: Vaishnavi
"""

def foo(a,b=4,c=6):
    print(a,b,c)
foo(20,c=12)
"""output:20 4 12"""

#2.Given the following list:
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
        #Write   code  which will give you "Apples"?

#o/p->
print(fruits[2])

#3.Given the code below:	
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
fruits.append("Lemons")
print(fruits)
"""What do you think will be printed?
 o/p-> ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries","Melons","Lemons"]
"""
#4.Write a line of code will change the starting_dictionary to the final_dictionary?
starting_dictionary = {
	    "a": 9,
	    "b": 8,
	}
final_dictionary = {
    "a": 9,
	    "b": 8,
	    "c": 7,
	}

#o/p->starting_dictionary=final_dictionary.copy()

print(final_dictionary)


#5.Which line of code will print "Steak"?
order = {
	    "starter": {1: "Salad", 2: "Soup"},
	    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
	    "dessert": {1: ["Ice Cream"], 2: []},
	}
#o/p->

print(order["main"][2])


#6.Without running the code below, what do you think will be printed in the console? 
def add(n1, n2):
	  return n1 + n2
def subtract(n1, n2):
	  return n1 - n2
def multiply(n1, n2):
	  return n1 * n2
	 
def divide(n1, n2):
	  return n1 / n2
print(add(2, multiply(5, divide(8, 4))))

#o/p->12.0

#7. What would you predict to be the result of running the following code?
def outer_function(a, b):
	    def inner_function(c, d):
	        return c + d
	    return inner_function(a, b)
result = outer_function(5, 10)
print(result)

#o/p->15


#8. Select the correct ways to get the value of marks key.
student = {
  "name": "Emma",
 
 "class": 9,
  "marks": 75
}

#o/p->
print(student["marks"])
#this will print all the values
print(student.values())

9. write correct way to remove the key marks from a dictionary
student = { 
  "name": "Emma", 
  "class": 9, 
  "marks": 75 
}

o/p->
student.remove("marks")
or
student.pop("marks")
print(student)

10.Suppoes you have dict1 and dict2,write  way to copy a dictionary in Python
dict1={"a":1,"b":2}
dict1.copy(dict2)
print(dict2)


11.Find the output of the code given below?
 lst = [int(x*x) for x in range(3,12,4)]
 print(lst[-2])
o/p->
49

12.Find the output of the code given below?
lst= [ int(x/3) for x in range(5,35) if x % 2 == 0 and x%5 == 0]
print(lst[-1]+5)
o/p->
15.0

.What would be the output of the following code snippet?
Func1=lambda x: ((x + 3) * 5 / 2)

Func1(3)
o/p->
15.0







