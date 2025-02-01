# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 08:20:08 2024

@author: Vaishnavi
"""

#####################
#append ()-adds the elements from last 
lst=[]
for num in range(0,20):
    lst.append(num)

print(lst)
#######list comprehension-it converts the long code into one line code
#reduce the space complexity.... so, response time will be good
#we can write same method using list comprehension
lst=[num for num in range(0,20)]
print(lst)
##############################
names=['dada','mama','kaka']
lst=[name.capitalize() for name in names]
print(lst) 
#all the operations are written on  the left side and for loop or whatever it would be on right side
names=['dada','mama','kaka']
lst=[name.upper() for name in names]
print(lst)
   
"""list comprehension very very imp for interview"""
#list comprehension with if statement
#while writing the if statement after for loop the business logic or the condition should be there
def even_num(num):
    return num%2==0
#even_num(10)
lst=[num for num in range (10) if even_num(num)]
print(lst)

#########################################
#for loop inside the for loop using the list comprehension
lst=[f"{x}{y}"for x in range(3)for y in range(3)]
print(lst)
####################################
#dictionary comprehension
#business logic on left side of the for loop 
#if statement should be on the right side
dict={x:x*x for x in range(1,3)}
print(dict)
#################################
#create a tuple
#generator
#it is another way of creating iterators
#it uses the keyword "yeild"
#instead of returning it in a defined function
#generators are implemented using function
#to access one element many of the times we use tis generator
gen=(x for x in range(3))
print(gen)
for num in gen:#here gen object will be creted
    print(num)
####################
gen=(x
     for x in range(3)
     
     )
print(gen)
next(gen)
###########to access the one value only will use the next()
next(gen)

#############################
#function which returns multiple values
def range_even(end):
    for num in range(0,end,2):
        yield num
        print(num)
#here the for loop below in going to give the value of end
for num in range_even(6):
    print(num)
#############################3
#now instead of using for loop we can write our own
#we can access this values one by one as well
gen=range_even(6)
next(gen)
next(gen)
next(gen)
#after all elements are being accessed then if still we are tring to call
#it will message stop iteration

next(gen)

########################3
#chaining generators
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*"*"
################################
""" 'ele*' appears to be placeholder for
an element from an iterable.the asterisk(*)
is likely just as a character used to represent
a placeholder or a wildcard
for instance,if you're iterating over a list 
of elements,"ele*"
could symbolize any element in that list
Its a generic representation that doesnt correspond
to any specific syntax in python itertools"""
passwords=["not-good","give'm-pass","00100-100","classydolly"]
for password in hide(lengths(passwords)):
    print(password)
    ##############################given to solve
import random
noun=input("enter your name:")
objective=input("enter adjective:")
number=random.randrange(0,100)
password=noun+objective+str(number)
print("the entered password is:",password)
def lengths(itr):
    for ele in itr:
        yield len(ele)
def hide(itr):
    for ele in itr:
        yield ele*"*"
for i in hide(lengths(password)):
    print(i,end=" ")
###################################
#enumerate
#printing the list with index
lst=["milk","paneer","bread"]
for index in range(len(lst)):
    print(f'{index+1} {lst[index]}')
#############with enumerate
lst=["milk","paneer","bread"]
for index,item in enumerate(lst,start=1):
    print(f"{index} {item}")
#start will decide from what number the index is going to be printed ie suppose 1
#######################################
#use of zip function
#here it is useful for doing like kaka's phn no is:94567,etc
name=["dada","mama","kaka"]
info=[9870,6032,34098]
for nm,inf in zip(name,info):
    print(nm,inf)
#############################
#use of zip function with mismatch list
name=["dada","mama","kaka","baba"]
info=[9870,6032,34098]
for nm,inf in zip(name,info):
    print(nm,inf) 
#########################
#it will not display excess mismatch item in name
#ie baba
#####################
#zip_longest
from itertools import zip_longest
name=["dada","mama","kaka","baba"]
info=[9870,6032,34098]
for nm,inf in zip_longest(name,info):
    print(nm,inf) 
################################
#use of fill value instead of none
name=["dada","mama","kaka","baba"]
info=[9870,6032,34098]
for nm,inf in zip_longest(name,info,fillvalue=0):
    print(nm,inf) 
############################
#use of all(),if all the values are
#true then it will produce output
#values must be non-zero ,+ve or -ve values are allowed
lst=[1,23,-8,27,89]
if all(lst):
    print("all values are true")
else:
    print("there are null values")
############
lst=[1,23,0,-8,27,89]
if all(lst):
    print("all values are true")
else:
    print("there are null values")
############################
#use of any if any one non zero values
lst=[0,0,0,8,9,-1]
if any(lst):
    #here if conition will run
    print('it has some non zero values')
else:
    print('useless')
#######################
lst=[0,0,0,0,0,0]
if any(lst):
    print('it has some non zero values')
else:
    #here else condition will run
    print('all values are null in the list')
###################################
#count()
#for image processing it is used
from itertools import count
counter=count()
print(next(counter))
print(next(counter))
print(next(counter))
#############################
#now lets start the count from 1
from itertools import count
counter=count(start=1)
print(next(counter))
print(next(counter))
print(next(counter))
#########################
#cycle
#suppose you have repeated task to be done
#then you will use this
#eg monitoring the room temperature after 1 hr everytime
#this function is also call periodic function
#for real time application in machine learning we use this cycle()
import itertools
instructions=("eat","code","sleep")
for instructions in itertools.cycle(instructions):
    print(instructions)
#to stop this stop the kernel
#so data sophistication takes the delay for going from device1 to device2 and gain come back to device1
#eg if using the remote for changing the ac so from remote to ac then ac will accept it and then it will again return back to remote
#this is delaying and we shuld always consider it 
#otherwise it will give zero ....means we need to calculate that 
#there is the use of cycle
########################33
#repeat
from itertools import repeat
for msg in repeat("keep paitence",times=3):
    print(msg)
#############################
#combinations()
#on dream11 the ads come and players we select is the use of combinations
from itertools import combinations
players=['jani','jay','janardhan']
for i in combinations(players,2):
    print(i)
###################################
from itertools import permutations
players=['jani','jay','janardhan']
for seat in permutations(players,2):
    print(seat)
    
###################################
#products
from itertools import product
team_a=['rohit','pandya','bumrah']
team_b=['virat','manish','sami']
for pair in product(team_a,team_b):
    print(pair)
#filter method is used when you want to apply on particular elements like print even odd in thst case
#map()-used when we want to apply on all the eleemnts 
##############################

"""VERY IMPORTANT...

in python,assignments statements(obj_b=obj_a)
it do not create real objects.
it only creates the new variable with the same reference.
so when you want to make actual copies of mutual objects(lists,dicts)
and want to modify the copy without affecting the original copy,you have to be carefl
for 'real'copies we can use the copy module
however,for compound/nested objects(eg nested lists and discts)
and custom objects there is an important difference between 
shallow and deep copying:


-shallow copies:only one level deep. it creates a new collection and populates it with references to the nested objects
this means modifying a nesrted object in the copy
deeper than
-deeper objects:a full independent clone.
it creates a new collection and then recursively populates it with copies of the nested"""
list_a=[1,2,3,4,5]
list_b=list_a
list_a[0]=-10
print(list_a)
print(list_b)
##################################
"very important interview"
#copy .copy()-or object specific copy functions 
import copy
list_a=[1,2,3,4,5]
list_b=copy.copy(list_a)
#not affects the other list
list_b[0]=-10
print(list_a)
print(list_b)
###########################
#but with nested objects ,modifying on level 2
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.copy(list_a)
#affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)
############################
#deep copies
#full independent cones.use copy.deepcopy(C:/Users/Vaishnavi/Downloads/buzzers.csvC:/Users/Vaishnavi/Downloads/buzzers.csv)
import copy
list_a=[[1,2,3,4,5],[6,7,8,9,10]]
list_b=copy.deepcopy(list_a)
#not affects the other
list_a[0][0]=-10
print(list_a)
print(list_b)



