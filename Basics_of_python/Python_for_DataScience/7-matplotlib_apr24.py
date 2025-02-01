# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 08:42:56 2024

@author: Vaishnavi
"""
#matplotlib 
#seaborn

#write a python program to draw a line with suitable label
import matplotlib.pyplot as plt
#here there is major library or package from which we are using pyplot package
#and using aliasing we are naming the pyplot as plt
x=range(1,50)
y=[value * 3 for value in x]
print("values of x:")
print(*range(1,50))
"""values of x:
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49"""

############################
"""this is equivALENT TO
instead of this we can use """
for i in range(1,50):
    print(i,end=" ")
"""1 2 3 4 5 6 7 8 9 10 11 12
 13 14 15 16 17 18 19 20 21 22 23 24 25 
 26 27 28 29 30 31 32 33 34 35 36 37 38
 39 40 41 42 43 44 45 46 47 48 49 """
 #run the below code togehter
import matplotlib.pyplot as plt
 #here there is major library or package from which we are using pyplot package
 #and using aliasing we are naming the pyplot as plt
x=range(1,50)
y=[value * 3 for value in x]
print("values of x:")
print(*range(1,50))
print("values of Y (thrice of x):")
print(y)
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x-label')
#set the y axis label of teh current axis
plt.ylabel('y-axis')
#set a title
plt.title('draw a line')
#display the figure
plt.show()
#display is not necesary

####################################

#label in the x-axis,y-axis and a title
import matplotlib.pyplot as plt
#x axis values
x=[1,2,3]
#y axis values
y=[2,4,1]
#plot lines and/or markers to the axes
plt.plot(x,y)
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("sample graph!")
#display a figure
plt.show()
################################
#write a python program to plot two or more lines
#on same plot with suitable legends of each line
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting line 1 points
plt.plot(x1,y1,label='line1')
#plotting line 2 points
plt.plot(x2,y2,label='line2')
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("two or more lines on same plot with suitable legends!")
#show a legend on the plot
plt.legend()
#display a figure
plt.show()
#########################333333
#write a python program to plot two or more lines
#lines with legends with different width and colors
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting line 1 points
plt.plot(x1,y1,color='blue',linewidth=3,label='line1 width 3')
#plotting line 2 points
plt.plot(x2,y2,color='red',linewidth=5,label='line2 width 5')
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("two or more lines on same plot with suitable legends!")
#show a legend on the plot
plt.legend()
#display a figure
plt.show()
#####################################
#write a python program to plot two or more lines
#different line patterns...dotted and dashed lines
import matplotlib.pyplot as plt
#line 1 points
x1=[10,20,30]
y1=[20,40,10]
#line 2 points
x2=[10,20,30]
y2=[40,10,30]
#plotting line 1 points
plt.plot(x1,y1,color='blue',linewidth=3,label='line1 width 3',linestyle='dotted')
#plotting line 2 points
plt.plot(x2,y2,color='red',linewidth=5,label='line2 width 5',linestyle='dashed')
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("two or more lines on same plot with suitable legends!")
#show a legend on the plot
plt.legend()
#display a figure
plt.show()
##########################################
#wrie a pthon program to plot 2 or more lines
#AND set the line markers
import matplotlib.pyplot as plt
#introducing marker in your graph
#x axis values
x=[1,4,5,6,7]
#y axis values
y=[2,6,3,6,3]
#plotting the points
plt.plot(x,y,color='red',linestyle='dashdot',linewidth=3,
         marker='o',markerfacecolor='blue',markersize=12)
#set the y-limits of the current axes
plt.ylim(1,8)
#set the x-limits of the current axes
plt.xlim(1,8)
"""(1.0, 8.0)"""
#set the x axis label of the current axis
plt.xlabel('x-axis')
#set the y axis label of the current axis
plt.ylabel('y-axis')
#set a title 
plt.title("display marker")
#show a legend on the plot
plt.legend()
#display a figure
plt.show()
#################################
#bar graph
#write a python program to display
#a bar chart of the popularity of programming language
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.xticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
########################################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color='blue')
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.xticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
#####################################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity,color='blue')#here we need to give thebarh so the graph will be turned
plt.ylabel("languages")
plt.xlabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.yticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
################################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.barh(x_pos,popularity)#without mentioning the color bydefault the bargraph will have blue color
#here we need to give thebarh so the graph will be turned
plt.ylabel("languages")
plt.xlabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.yticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
####################################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['blue','red','black','yellow','cyan','green'])
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.xticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
########################################
import matplotlib.pyplot as plt
x=['java','python','php','javascript','c#','c++']
popularity=[22.2,17.6,8.8,8,7.7,6.7]
x_pos=[i for i,_ in enumerate(x)]
plt.bar(x_pos,popularity,color=['black','yellow'])#if we donot give all different colors so the colors mentioned will be repeated
plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("popularity of programming language\n"+"worldwide,oct 2017 compared to the year ago")
plt.xticks(x_pos,x)
#turn on grid
plt.minorticks_on()#it will display the grd
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.show()
##############################
#histogram
#the graph have right side as a long tail is right skewed an vice a verse for left skewed
#the graph should be equally distributed else if it is right/left skewed then it gives wrong result
import matplotlib.pyplot as plt
blood_sugar=[113,85,90,150,149,88,93,115,135,80,77,82,129]
plt.hist(blood_sugar,rwidth=0.8)
#by default nember of bins is set to 10
plt.hist(blood_sugar,rwidth=0.5,bins=4)


####################33333
plt.xlabel("sugar level")
plt.ylabel("number of patients")
plt.title("blood sugar chart")
plt.hist(blood_sugar,bins=[80,100,125,150],rwidth=0.95,color='blue')
####################################33
#boxplot
#import libraries
import matplotlib.pyplot as plt
import numpy as np
#creating dataset
np.random.seed(10)
data=np.random.normal(100,20,200)
fig=plt.figure(figsize=(10,7))
#creating plot
plt.boxplot(data)
#show plot
plt.show()
###################################
#in this graph down side is outliers ie some of the data is out of the range
#creating the dataset
import matplotlib.pyplot as plt
import numpy as np
#creating dataset
np.random.seed(10)
data1=np.random.normal(100,10,200)
data2=np.random.normal(90,20,200)
data3=np.random.normal(80,30,200)
data4=np.random.normal(70,40,200)
data=[data1,data2,data3,data4]
fig=plt.figure(figsize=(10,7))
#creating axes instance
ax=fig.add_axes([0,0,1,1])
#creating the plot
bp=ax.boxplot(data)
#show plot







