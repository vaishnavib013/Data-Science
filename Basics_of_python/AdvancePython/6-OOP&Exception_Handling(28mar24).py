# -*- coding: utf-8 -*-
"""
Created on 28 March 2024
Exception Handling,OOP
@author: Vaishnavi
"""

#####################3
#28/03/2024
#exceptions are run time errors
#eg.division by zero,array index out of bound,array negative number indexing
#exception handling
#two types of exception
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print(quotient)
    print("divsion performed successfully")
except ZeroDivisionError:
    print("ohh! this is divide by zero")
print("outside the try block")
  

try:
    numerator=50
    denom=int(input("enter the denominator"))
    print(numerator/denom)
    print("divsion performed successfully")
except ZeroDivisionError:
    print("denominator zero is not allowed")
except ValueError:
    print("ONLY INTEGERS should be entered")
#########################33333333333333
#handling exceptions without naming them
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("divsion performed successfully")
except ValueError:
    print("ONLY INTEGERS should be entered")
except:
    print("OOPS!...some exceptions raised")

#so last statement will run when divsion by zero or any other is there else than float 
#################################
#handling the exception using try..except...else
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("divsion performed successfully")
except ZeroDivisionError:
    print("denominator zero is not allowed")
except ValueError:
    print("ONLY INTEGERS should be entered") 
else:
    print("the result of division operation is ",quotient)
    
#if any exception is occured then it will go except statement else no any error is found then it will go on else part if executed successfully   
##############################
#finally-if you want to print the block of statement compulsory whether your exception occurs or not then you can use the finally block of statement to excute that part
##handling the exception using try..except...else...finally
try:
    numerator=50
    denom=int(input("enter the denominator"))
    quotient=(numerator/denom)
    print("divsion performed successfully")
except ZeroDivisionError:
    print("denominator zero is not allowed")
except ValueError:
    print("ONLY INTEGERS should be entered") 
else:
    print("the result of division operation is ",quotient)
finally:
    print("OVER and OUT")
#############################################
#"A CLASS "IS A COLLECTION OF PROPERTIES(data fields) AND METHODS(procedure or functions) that operates on that data
#a class is essentially  serves as a template for an object and behaves like a basic datatype "int".

#bare bone class-havin no data fields and methods
#object-instance of a class
#object=classname();"creating the object"
#to create the reference or handle of the class:
    #"classname referencename/handler";

"""
class circle:
    x,y;
    r;
    //methods to return circumference and area
    circumference():
        return 2*3.14*r;
    
    area():
        return 3.14*r*r;
"""

"""data abstraction-
declare a class circle,have created a new datatype

can define variables(objects)of that type:
    
    circle aCircle; "reference"
    circle bCircle;
    """
"""human class-
properties:
    1.name
    2.gender
    3.occupation
methods:
    1.sleeps
    2.do_work
    3.speaks"""
#29/03/2024
#constructor dont return values like functions
#__init__ is a constructor
class Human:#class is a blueprint 
#no memory will be assign to class until an object is created
    def __init__(self,n,o):#constructor
        self.name=n
        self.occupation=o
    def do_work(self):
        if self.occupation =='tennis player':
            print(self.name,'plays tennis')
        elif self.occupation =="actor":
            print(self.name,'shoots film')
    def speaks(self):
        print(self.name,'says how are you?')
tom=Human("tom_cruise","actor")
tom.do_work()
tom.speaks()
#here tom was given the handle or reference 
maria=Human("maria_sharapova","tennis player")
maria.do_work()
maria.speaks()
#####################################
#inheritance
#single inheritance
class vehicle:
    def general_usage(self):
        print("general use:transpotation")
        
class Car(vehicle):
    def __init__(self):
        print("I'm car")
        self.wheels=4
        self.has_roof=True

    def specific_usage(self):
        self.general_usage()
        print('specific use:commute to work,vacation with family')
class Motorcycle(vehicle):
    def __init__(self):#self is the reference 
        print("I'm motor cycle")
        self.wheels=2
        self.has_roof=False
        
    def specific_usage(self):
        self.general_usage()
        print('specific usage:local commutation,racing')
a=Car()
b=Motorcycle()
a.specific_usage()
b.specific_usage() 
##########################3333
#multiple inheritance
class Father():
    def skills(self):#not a constructor
        print("I like gardening,programming")

class Mother():
    def skills(self):
        print("I like cooking and art")

class child(Father,Mother):
    def skills(self):
        Father.skills(self)#here using the class we have called the skills
        #father and mother are the classes ie base classes
        
        Mother.skills(self)
        print("I like sports")
        
c=child()#creating the object and calling the derived class using that object so memory will be created
c.skills()
######################## advance python complete##################

