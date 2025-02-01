# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 09:06:59 2024

@author: Vaishnavi
"""

"""1. Implement a simple Named Entity Recognition (NER) 
function that identifies named entities in a sentence. The 
function should return a list of these named entities.
For example, given the sentence "Ramesh lives in 
Mumbai", the function should return ["Ramesh", 
"Mumbai"].
Text1: “James is the author of Atomic Habits”
Text2: “Aarti works at Accenture”
"""
import nltk
nltk.download('punkt')
from nltk import word_tokenize
text1=word_tokenize("jamesh is the author of atomic habits")
text2=word_tokenize("aarti works at accenture")
print(text1)
print(text2)

"""
 2.Design a function that classifies a text as either "spam" 
or "imp" (non-spam) based on the presence of certain 
keywords. For example, if the text contains words like 
"buy", "free", "offer", or "click", it should be classified as 
"spam". If these words are not present, the text should be 
classified as "imp". The function should return the 
appropriate classification.
Text1: “Buy 1 Get 1 Free”
Text2: “Meeting is scheduled at 12 PM ”
Text2: “Click on the link below to see the offer.”
"""
import re
text="""Buy 1 Get 1 Free"""
pattern="Free | Buy | Offer | CLick"
check_text=re.findall(pattern,text)
if (check_text is None):
    print("imp")
else:
    print("spam")

import re
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        print("spam")
    else:
        print("imp")
    
get_pattern_match('\ Free | \ Buy | \ Offer | \ CLick',text)
text="""Meeting is scheduled at 12 PM """
text="""Buy 1 Get 1 Free"""
text="""Click on the link below to see the offer."""

"""3. Create a function that should return a list of stemmed 
words.
e.g [‘running’] = [‘run’]

"""
list = ['painful','standing','abstraction','magically']
import nltk
stemmer=nltk.stem.PorterStemmer()
for i in list:
    print(stemmer.stem(list[i]))

print(" ".join(word[::-1] for word in words))



"""
4. Implement a function that takes a list of tokens (words) 
and removes all stopwords from it. For example, if the 
input tokens are ["This", "is", "a", "test"] and 
the stopwords are ["is", "a", "the"], the function should 
return ["This", "test"].
Stopwords = [“is”,”a”,”the”, “an”,”she”]
Sentence1: “an apple is on the table.”
Sentence2: “She is an engineer.”
 5 . Perform lemmatzation on the given text
 text= "Dancing is an art. Students should be taught 
dance as a subject in schools . I danced in many of my 
school function. Some people are always hesitating 
to dance."""
import re
import nltk
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")
