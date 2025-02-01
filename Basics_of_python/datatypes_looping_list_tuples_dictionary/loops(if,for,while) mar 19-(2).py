# -*- coding: utf-8 -*-
"""
Created on Tue 19 march 22:32:53 2024

@author: Vaishnavi

#if-elif-else
#while loop
#for loop
#for loop with the conditions
"""
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
num=10
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

##############################


#python program to print the even and odd numbers
start,end=4,19
#iterating each number in list 
for num in range(start,end+1):
    #checking the condition
    if num%2!=0:
        print(num,end=" ")
        
        
#for even numbers
start,end=4,19
for num in range(start,end+1):
    if num%2==0:
        print(num,end=" ")
        
#even numbers from 1 to 20
start,end=0,21
for i in range (start,end):
    if i%2==0:
        print(i,end=" ")
        