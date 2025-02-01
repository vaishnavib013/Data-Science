# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 15:03:15 2024

@author: Vaishnavi
"""
#practice for nlp for test
import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="abc@gmail.com"
pattern1="Vaishnavi Badjate"
re.findall(pattern,text)
re.findall(pattern1,text)
##########################
import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="[a-z]*@gmail.com"""
pattern1="This is me [A-Za-z]* [A-Za-z]*([^\n]*)"
re.findall(pattern,text)
re.findall(pattern1,text)
############################
import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="abc@gmail.com"
pattern1="Vaishnavi Badjate"
re.findall(pattern,text)
re.findall(pattern1,text)


import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="[a-z]*@gmail.com"
pattern1="This is me [A-Za-z]*"
re.findall(pattern,text)
re.findall(pattern1,text)  

import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="[a-z]*@gmail.com"
pattern1="Vaishnavi Badjate"
re.findall(pattern,text)
re.findall(pattern1,text)

import re 
text="""Hello everyone.This is me Vaishnavi Badjate.
for more details contact me at abc@gmail.com"""
pattern="[a-z]*@gmail.com"
pattern1="This is me [A-Za-z]*([^\n]*)"
re.findall(pattern,text)
re.findall(pattern1,text)
#########################################
p1="[abc]"#this finds only the single character present in the text
re.findall(p1,text)
#o/p:Out[26]: ['a', 'a', 'a', 'a', 'a', 'c', 'a', 'c', 'a', 'a', 'b', 'c', 'a', 'c']
##############################33333333333333
p1="[abc]+"#this returns us all the combinations of abc available in the given text
re.findall(p1,text)
#Out[27]: ['a', 'a', 'a', 'a', 'a', 'c', 'ac', 'a', 'abc', 'a', 'c']
#######################################
p2="[^abc]"#this returns everthing excluding abc.
re.findall(p2,text)
"""Out[28]: 
['H',
 'e',
 'l',
 'l',
 'o',
 ' ',
 'e',
 'v',
 'e',
 'r',
 'y',
 'o',
 'n',
 'e',
 '.',
 'T',
 'h',
 'i',
 's',
 ' ',
 'i',
 's',
 ' ',
 'm',
 'e',
 ' ',
 'V',
 'i',
 's',
 'h',
 'n',
 'v',
 'i',
 ' ',
 'B',
 'd',
 'j',
 't',
 'e',
 '.',
 '\n',
 'f',
 'o',
 'r',
 ' ',
 'm',
 'o',
 'r',
 'e',
 ' ',
 'd',
 'e',
 't',
 'i',
 'l',
 's',
 ' ',
 'o',
 'n',
 't',
 't',
 ' ',
 'm',
 'e',
 ' ',
 't',
 ' ',
 '@',
 'g',
 'm',
 'i',
 'l',
 '.',
 'o',
 'm']
"""
p2="[^abc]+"#this includes all except the combination of abc
re.findall(p2,text)
"""Out[29]: 
['Hello everyone.This is me V',
 'ishn',
 'vi B',
 'dj',
 'te.\nfor more det',
 'ils ',
 'ont',
 't me ',
 't ',
 '@gm',
 'il.',
 'om']"""
p3="\n"#newline there or nor if there it returns \n
re.findall(p3,text)
############################
p4="[a-z]"#we will get the everything which is available in the give text between small a to z character.as a single character.
re.findall(p4,text)#capital "H" wont be included in it.also many of them 
###############################
p5="[A-Z]"#this will include only uppercase character
re.findall(p5,text)
#Out[32]: ['H', 'T', 'V', 'B']
###################################
p4="[a-z]+"
re.findall(p4,text)
"""Out[33]: 
['ello',
 'everyone',
 'his',
 'is',
 'me',
 'aishnavi',
 'adjate',
 'for',
 'more',
 'details',
 'contact',
 'me',
 'at',
 'abc',
 'gmail',
 'com']"""
p5="[A-Z]+"
re.findall(p5,text)#Out[34]: ['H', 'T', 'V', 'B']
##############################
p5="[^a-z]+"#excluding all the lowercase including spaces,fullstop,uppercase,symbols,numbers ,etc
re.findall(p5,text)
"""Out[36]: 
['H',
 ' ',
 '.T',
 ' ',
 ' ',
 ' V',
 ' B',
 '.\n',
 ' ',
 ' ',
 ' ',
 ' ',
 ' ',
 ' ',
 '@',
 '.']"""
########################
p6="[a-zA-Z]+"#including all the upper &lowercases character btwn a-z
re.findall(p6,text)
########################
p4="[.]"
re.findall(p4,text)
###############
p4="/.+/"
re.findall(p4,text)
#################
p4="[b|a]"#if a or b is encountered then it will return that value
re.findall(p4,text)
#Out[48]: ['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'b', 'a']
#########################
p4="[\s]+"#this will return without spaces
re.findall(p4,text)#\s stands for whitespaces
#################
p4="\S+"#\S this also returns the same ie non-whitespaces
re.findall(p4,text)
###################
p4="\d"#\d stands for digits
re.findall(p4,text)
#################
p4="\D"#\D stands for non-digits
re.findall(p4,text)
#################
p4="\w+"#this includes all the word character numbers,characters
re.findall(p4,text)
#################
p4="[a-zA-Z0-9_]+"#this includes all the word character 
re.findall(p4,text)
#################
p4="\x20"#returns all the spaces
re.findall(p4,text)
#################
p7="This is me([^\n]*)"
re.findall(p7,text)
###########################
text1='''Hello all contact me at 1382695787.
THis is id:abc123@gmail.com.
also you can apply on request on sanivani.org
(122)-(5435)-(564)'''
p8='\(\d{3}\)-\(\d{4}\)-\(\d{3}\)|\d{10}'
re.findall(p8,text1)
#for anyone of the character you want to print as it is use "\"which that character
#####################################
text1='''Hello all contact me at 1382695787.
THis is id:abc123@gmail.com.
also you can apply on request on id:sanivani.org
(122)-(5435)-(564)'''
p8="(?:(\d{10})|(\(\d{3}\)-\(\d{4}\)-\(\d{3}\)))"
re.findall(p8,text1)
#this is also going to return us two numbers 
#Out[83]: [('1382695787', ''), ('', '(122)-(5435)-(564)')]
################################33
#return the gmail
p9="id:[a-z0-9]*\@gmail.com|[a-z0-9]*\.org"
re.findall(p9,text1)
######################3
q1="id:[^\n]*"#here we get id:emails in such format if we don not give the brackets over there
re.findall(q1,text1)
#['id:abc123@gmail.com.', 'id:sanivani.org']
######################
q1="id:([^\n]*)"#here using brackets gives us only the emails using printing id: also
re.findall(q1,text1)
#Out[92]: ['abc123@gmail.com.', 'sanivani.org']
#########################
#to ignore the casesensitive
#using flags=re.IGNORECASE we wont affect the upper or lowercases 
q1="ID:[^\n]*"
p10=re.findall(q1,text1,flags=re.IGNORECASE)
p10

