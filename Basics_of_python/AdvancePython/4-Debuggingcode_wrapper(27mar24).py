# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 15:28:19 2024

@author: Vaishnavi
"""
"""debugging process is very important for interview """
#Note:Need to save this file as "wrapper.py" only

#debugging code
#you need to write it on separate file
#it starts to debug from starting 
import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        total_time=(end-start)*1000
        print(func.__name__+f"took {total_time}mil sec")
        return result
    return wrapper

@time_it
def calc_square(numbers):
    result=[]
    for number in numbers:
        result.append(number*number)
    return result
@time_it 
def calc_cube(numbers):
    result=[]
    for number in numbers:
        result.append(number*number*number)
    return result
array=range(1,100000)
out_square=calc_square(array)
out_cube=calc_cube(array)
#debug tells that control goes from where to where
"""for debug->click on debug option->from where 
you want to start click there in your code
->click on debug->click on set/clear breakpoint 
->then red mark will appear there ->again go on debug
->click on "step into"option->then see the console
->again go on debug option ->click on step ->step and 
see the console ->for exit ->go on debug->click on stop"""
#####################################













