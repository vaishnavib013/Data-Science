
"""to print the the world as it is hello world"""
print("hello world")
"""to declare the variable storing integer 
data and printing it and checking for the type 
using type() """ 
############################

#type() function
a=12
print(a)
#checking the type of variable a is storing
print(type(a))

'''in a variable b storing a floating number
and checking it datatype''' 
b=12.45
print(b)
print(type(a))
#take the input from the user what there age is
#check the the datatype of the age if only the input is 
#taken from the user and then print the age.so the age wil be 
#in the form of string if ony input is taken from the user
"""note:if the input is taken from the user without defining 
the datatype of the variable in which is it stored then
it will get stored in the form of string format"""
age=input("enter your age:")
print(type(age))
print(age)
#in age1 variable take the age from the user and check its datatype
age1=input("enter your age:")
print(type(age1))
print(age1)
#in age2 var take the age from the user  without defining the datatype
age2=(input('enter your age'))
print(type(age2))
print(age2)
#concat the age1 and age2 in age variable
#as both are without defining the datatype so it gives string
#when stored in the variable for eg:1+2=12
age=age1+age2
print(age)
#if defining the datatype as integer and then taking
#the input from the user it will give the type() as int
age1=int(input('enter your age'))
print(type(age1))
print(age1)

age2=int(input('enter your age'))
print(type(age2))
print(age2)
"""when concating the age1 and age2 varibles in the 
age variable it will added as the datatype of both the
variable is integer and the datatype of the age variable 
will be integer as for eg:1+2=3""" 
age=age1+age2
print(age)

########################################

#declare the float variable
#check the datatype of that variable using type()
exchange_rate=1.23
print(exchange_rate)
print(type(exchange_rate))

####################################

#float and integer declaration
int_value=100#int datatype
string_value='1.5'#float datatype
#display the value of int_value which in the intger number
print('the value of int_value is:',int_value)
"""typecasting the int_value var which stores the int
data converting into the float datatype and storing
it into the float_value""" 

#typecasting 
float_value=float(int_value)
print('int value as a float:',float_value)
print(type(float_value))#checking the datatype of typecasting var

"""typecasting:changing one form of data into another 
datatype 
so string_value stores the string value 
converting into the float value and storing into the var
float_value by doing the typecasting there itself"""

float_value=float(string_value)
print('string value as a float:',float_value)
print(type(float_value))

#######################################

#complex numbers
"""storing the real and imagnary value in the c1 and c2
and printing its values and checking the datatype it stores
we will print the real part of c1 and imag part of c2
so imag part will get in the form of floating number"""
c1=1 
c2=2j
print('c1:',c1,',c2:',c2)
print(type(c1),type(c2))
print(type(c2))
print(c1.real)
print(c1.imag)
print(c2.imag)
print(c2.real)
###################################

#boolean values
#python supports another type called boolean;
#a boolean type can only be one of true or false
all_okay=True
print(all_okay)
print(type(all_okay))
all_oka=False
print(all_oka)
print(type(all_oka))
#in boolean the true has 1 and false has 0 values
#so adding it it will give as 1+0=1
all_ok=False
print(all_okay+all_ok)
#you can convert strings into booleans by taking the 
#input and defining it as the bool datatype
#true or false (and nothing else)
#if you enter anything it will give as true and
#if you dont enter anything and simply enter then it gives false
status=bool(input ('ok it is confirmed?:'))
print(status)
print(type(status))

#after performing operations the datatype of the variable
##########################

home=10#integer
away=15
#addition of integer gives integer
print(home+away)
print(type(home+away))
#mutiplication of integer gives integer
print(10*4)
print(type(10*4))
print(4*"string")
print(type((4*"string")))

############################################################

#substraction of two integer gives integer
goals_for=10
goals_against=7.5
print(goals_for - goals_against)
print(type(goals_for - goals_against))
####################################

#division of any two numbers is always the output in float
print(100/20)
print(type(100/20))
#whenever we required the float division in integer
#there is an alternative version of the divide operator
#this operator is referred to as the integer division operator
print(100//20)
print(type(100//20))

 ###################################
 
#power operator
"""a final integer operator we will look at is the power operator that can
be used to raise an integer by a given power ,
for eg: 5^3.
the power is **"""
a=5
b=3
print(a**b) 
##############################

#assignment operator
'''these are the assignment operator are actually 
referred to as an compound operators as they combine together
'''
#is operator gives the output in the form of boolean values
#flow of cntrol statements
winner=None
print(winner is None)
print(winner is not None)
print(winner is None)
############################

#indentation is important in python otherwise it will give indentation error
#comparison operator(==,=<,=>,<,>)
#value is smaller than 0
num=int(input('enter a number:'))
if num<0:
    print(num)
    #value is greater than 0
num=int(input('enter a number:'))
if num>0:
    print(num)
###########################
#if else statements
num=int(input("enter the number"))
if num<0:
    print("number is negative")
else:
    print("positive number")
##############################
  
#elif statements
num=int(input('enter the number'))
if num<0:
    print('negative')
elif num>0:
    print('positive')
else:
    print('equal')

###################################3
    
#the use of elif
#if you want to give many conditions then we use if-elif-else
savings=float(input('enter your savings'))
if savings==0:
    print("sorry no savings")
elif savings<500:
    print('well done')
elif savings<1000:
    print('thats a tidy sum' )
elif savings<10000:
    print('welcome  sir!')
else:
    print('thankyou')

####################################

#while loop
#iteration/ looping
"""the while loop exists in almost all programming languages
and used for iterative one or more code statements
as long as the  test condition (expression is true)"""
count=1
print('starting')
while count<=10:
    print(count)
    count+=1

#####################################

#for loop
#in for loop the condition or range given is (starting,end-1)
print('print the range values')
for i in range(2,10):
    print(i)
    print('done')
###############################

#for loop gets executed upto the range n-1
print('print the range values')
for i in range(2,10):
    print(i)
print('done')
#if you print the done in the for loop it will print done in every step
#if you print something out of for loop it will execute only once
#########################################

#as above the num was asign to 12
print('print the range values')
for i in range(0,16):
    if i==num:
        break
    print(i)
print('done')
#"anonmymous" loop variable
"""no memory is allocated for anonmymous variable.
so it avoid the space complexity"""
#it will give one line space and then it will give dot
for _ in range(1,11):
    print(".")
    print()
    #end=" " is used for space 
for _ in range(1,10):
    print(".",end=' ')
    print()

for _ in range(1,11):
    print(".",end=" ")
print()

for _ in range(1,11):
    print(".")
print()

