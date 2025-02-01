# -*- coding: utf-8 -*-
"""
Created on 20 march & 21 march 2024
#dictionary
@author: Vaishnavi
"""

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
#to insert/add the new key:value pair in the existing dictionary we use dictname["key"]="value"
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
    
#accessing the values in the dictonary using for loop
for x in car:
    print(car[x])
#accessing the key values pair 
'''very important'''
for key,value in car.items():
    print("%s=%s" %(key,value))
    #or
    print(key,value)
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


