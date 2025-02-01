# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:09:54 2024

@author: Vaishnavi
"""

"""hw:flipcart->extract the review ,
replace the mobile lang,tokenization 
and do all the nlp working on it"""
#find index of the letter pretty is present
text="This watch is so preety I luv it.This watch was gr8 "
text.index("preety")#Out[1]: 17

#find the index of the word
text.split().index("preety")#Out[2]: 4

#reverse the word
text.split()[4][::-1]#Out[3]: 'yteerp'

#it will do the tokenize
words=text.split()
words

#1st word of the text
firstword=words[0]
firstword#Out[7]: 'This'

#last word of the text
lastword=words[-1]
lastword#Out[6]: 'gr8'
print(words)


#concatinate 1st and last words
print(firstword+" "+lastword)#This gr8

#reverse the text
print(" ".join(word[::-1] for word in words))
#sihT hctaw si os yteerp I vul sihT.ti hctaw saw 8rg
###########################
#tokenization of words in sentence
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize (text)
print(words)
#['This', 'watch', 'is', 'so', 'preety', 'I', 'luv', 'it.This', 'watch', 'was', 'gr8']
#################################
#parts of speech
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
"""Out[18]: 
[('This', 'DT'),
 ('watch', 'NN'),
 ('is', 'VBZ'),
 ('so', 'RB'),
 ('preety', 'JJ'),
 ('I', 'PRP'),
 ('luv', 'VBP'),
 ('it.This', 'JJ'),
 ('watch', 'NN'),
 ('was', 'VBD'),
 ('gr8', 'JJ')]
"""
##############################3
#replace the mobile lang words to original form
text="This watch is so preety I luv it.This watch was gr8 "
text.replace("preety","pretty")
#Out[19]: 'This watch is so pretty I luv it.This watch was gr8 '
text.replace("preety","pretty").replace("luv","love")
#Out[20]: 'This watch is so pretty I love it.This watch was gr8 '
#############################
#autocorrect the words
from autocorrect import Speller
#declare the function Speller defined for english language
#declare the en for the english language 
spell=Speller(lang='en')
spell("awsume")
#Out[94]: 'assume'
####################
import nltk
nltk.download('punkt')
from nltk import word_tokenize
text="This watch is so preety I lov it.This watch was gr8 "
#let us first tokenize this sentence
sentence3=word_tokenize(text)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)
#o/p:This watch is so pretty I lov it.This watch was gr8
###################################
#tokenize the sentence
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("This watch is so preety I luv it. This watch was gr8. ")
sent
#Out[40]: ['This watch is so preety I luv it.', 'This watch was gr8.']
################################
import re
text="This watch is so preety I luv it.This watch was gr8.It is 100 times better in performance "
pattern ='It is [^\d]*(\d*)'
matches=re.findall(pattern, text)
matches
#Out[49]: ['100']
#####################################
import re
text="This watch is so preety I luv it.This watch was gr8.It is 100 times better in performance from model 2265"
pattern='It is [^\d]*(\d*)([^\n]*)'
matches=re.findall(pattern, text)
matches
##########3
import re
text="""
This watch is so preety I luv it
This watch was great.
It is times better in performance.
Its id was 9123565755"""
pattern ='(\d{10})'
matches=re.findall(pattern, text)
matches
#Out[127]: ['9123565755']
############################
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match(' (\d+)',text)
#Out[140]: '9123565755'

###################################
get_pattern_match(r'This (.*)\n',text).strip()

get_pattern_match(r'This watch is *\n(.*)\great ',text).strip()
#error







