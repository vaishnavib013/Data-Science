# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 21:17:55 2024

@author: Vaishnavi
"""
#type casting
a=12.5
print(type(a))
int(a)
str(a)

#complex
c1=5
c2=3j
type(c2)
c=c1+c2
c.real
c.imag

#bool
b=True
type(b)
d=bool(input("enter"))
print(d)
print(type(d))

#
s,e=5,20
for i in range(s,e+1):
    if i==e:
        print("end")
    else:
        print(i)
        
#
ab="    hello this is me talking to you all  "
print(type(ab))
print(ab[::-1])
print(ab.upper())
print(ab.lower())
print(ab.strip()) 
print(ab.lstrip())
print(ab.rstrip())  
print(ab.replace('me','vaishnavi'))    
print(ab.split("me"))  
print(ab.find("me"))  
ac="have a good day"
bc=ab+ac
print(ab+" "+ac)
#######################
ad=11
print(ab+ad)
print(f"{ab} and my age is {ad}")

bd="lets start {1} and my age is {0}"
print(bd.format(ab,ad))
#########################33
abc="hello ,\"marry go round\""
print(abc)
##################3
z=['a','b','c']
print(z)
z.append('d')
z.extend('e')
z.clear()
z1=z.copy()
z1.extend(z)
z.insert(2,"f")
print(z,z1)
z.count("b")
z.pop(2)
z.remove("f")
z.reverse()
z.sort()
z
z.sort(reverse=True)
z

y=('a','b','c')
y[2]='d'
x=list(y)
z=tuple(x)
print(z)
#####################
d={'a':'1','b':'2','c':3}
print(d)
print(type(d))
print(d.items)#it will cretae the object
print(d.items())
print(d.keys())
print(d.values())
print(d.get('b'))#to find
print(len(d))
d['d']='4'
d.values()
d.items()
d.pop('d')
for i in d:
    print(i)
for i in d:
    print(d[i])
for key,value in d.items():
    print("%s=%s"%(key,value))

d1=d.copy()
d1
d1=0
d=dict.fromkeys(d,d1)
d.update({'b':4})
d
    
x="hello world this is me"
print(x.split(" "))   
    
    
    
    