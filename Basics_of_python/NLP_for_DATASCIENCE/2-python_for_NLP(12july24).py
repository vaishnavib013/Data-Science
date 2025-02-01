# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:11:16 2024

@author: Vaishnavi
"""
#12-06-2024
"""
COMPLETED
basics of ptython(LIST,DICTIONARY,TUPLES,SETS,)
advance python(DECORATORS,LIST COMPREHENSION,)
python for DS(DATAFRAMES)
"""
#data scientist-statistics(deep learning),ML,TS,AI,python,sql,tabular/powerbi,nlp
#data analytics-excel,python,sql,tabular/powerbi,nlp
#PYTHON FOR NLP
#NLP:natural language processing
"""to convert the reviews (mobile language like gm,gn,tc)
into the english language then into the numeric 
array and then applying to the machine learning

extract the information/text from the reviews and convert into 
tabular form then apply 

chatgpt is a nlp application

web scrapping:
(data acquisition):scapping/extractiong the 
text from the reviews or ratings like in amazon

text summarization is also the application of ML .ie 
converting all the reviews from the customer
and will give the summarize details or info
about the product

preprocessing:stemming,lemmatization,tokenization

feature engineering:
feature engineering is a process of extracting
features from the raw data
like eg:classifying animal as dog or cat
features are ear,nose,eyes

web scraping->filter->leminization(preprocessing)->vector->applied to ML
normalization-converting into the readable form lnguage
"""

##############################
#text mining
sentence="we are learning textmining from sanjivani AI"
#giving position to each of them"
###if we want to know the location or position of learning
sentence.index("learning")
#Out[2]: 7
###it will show learning at position 7
##this is going to show character position from 0 including spaces
#####################################

#textmining word
#we want to know the position textmining word
#tokenization:choking your sentence into words/tokens
#eg:sentence="we are learning textmining from sanjivani AI"
#choking:["we","are","learing",...and so on]
sentence.split().index("learning")
#Out[3]: 2
###it will split the words in list and count the position
#if you want to see the list select sentence.split()
#it will show o/p as 2
####################################

#suppose we want to print any word in reverse order
sentence.split()[2][::-1]
#Out[4]: 'gninrael'
#[start:end:-1(start)] will start from -1,-2,-3 till
#learing will be printed as Out[4]: 'gninrael'

#########################
#suppose we want to print 1st and last word of the sentence
words=sentence.split()#it will do tokenization (it is going to generate the list)
first_word=words[0]
first_word#Out[7]: 'we'
last_word=words[-1]
last_word#Out[9]: 'AI'

##########################
#now we want to concate the 1st and last words
concate_word=first_word+" "+last_word
concate_word#o/p: 'we AI'
#we need to give the space between the words

##################################
#we want to print even words from the sentences
[words[i] for i in range (len(words)) if i%2==0]
#Out[12]: ['we', 'learning', 'from', 'AI']
#words with odd length wont be printed
##################################
#we want to print the odd words from the sentence
[words[i] for i in range (len(words)) if i%2!=0]
#Out[13]: ['are', 'textmining', 'sanjivani']

#######################################
sentence
#now we want to display only AI
sentence[-2:]
#Out[15]: 'AI'
sentence[-3:]
#Out[16]: ' AI'
#here space will be there
#########################
#suppose we want to display entire sentence in reverse order
sentence[::-1]
#Out[17]: 'IA inavijnas morf gninimtxet gninrael era ew'

##################################
#suppose we want to select each word and print in reversed order
words
#Out[18]: ['we', 'are', 'learning', 'textmining', 'from', 'sanjivani', 'AI']
print(" ".join(word[::-1] for word in words))
#list comprehension...it will join the words in the reverse order
#o/p:ew era gninrael gninimtxet morf inavijnas IA
###################################
#tokenization
#here first go on anaconda environments
#then go to the root base click on play button 
#then go open terminal->then type pip install nltk
#download that package

import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize ("I am rreading NLP Fundamentals")
print(words)
#o/p:['I', 'am', 'reading', 'NLP', 'Fundamentals']
#tokenization-splitting of words
############################
#parts of speech(pos)tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
"""Out[28]: 
[('I', 'PRP'),
 ('am', 'VBP'),
 ('rreading', 'VBG'),
 ('NLP', 'NNP'),
 ('Fundamentals', 'NNS')]"""
#go on google->search for nltk pos_tags
#NNP-propernoun,
#vb-verb and many more
########################################
#stop words from nltk library
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
stop_words=stopwords.words('English')
#stop_words
##you can verify that 179 stop words are there in variable explorer
print(stop_words)

#cc,dt,ex,fw,vbd,nnp,and many more 36 are there parts of speech

###########################################

#13-06-2024

sentence_words=word_tokenize(sentence)
print(sentence_words)

##now let us filter the sentence1 using stop_words
sentence_no_stops=" ".join([words for words in sentence_words])
print(sentence_no_stops)
sentence_words


##you can notice that am,of, themmost,popular,in thare missing
###############################333
#normalization-converting into thr readable language
#suppose we want to replace words in string
sentence2="I visited my from ind on 14-02-19"
normalized_sentence=sentence2.replace("my","malaysia").replace("ind","india")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
#o/p:I visited malaysia from india on 14-02-2020
######################################
#first go anaconda environments ->base root->pause->open terminal->type pip install autocorrect
#suppose we want auto correction in the sentence for the english language 
from autocorrect import Speller
#declare the function Speller defined for english language
#declare the en for the english language 
spell=Speller(lang='en')
spell("engilish")
spell("goodi")
#Out[10]: 'english'

########################################
#suppose we want to correct whole sentence
import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3="ntural lanagage processin deals withh the aart of extrat sentiiiments"
#let us first tokenize this sentence
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)
#o/p:natural language processing deals with the part of extra sentiiimentss
#########################
#stemming:getting the original occurrance of the words like eating will be eat
#remove ing,ed,etc
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")#Out[21]: 'program'
stemmer.stem("programmed")#Out[22]: 'program'
stemmer.stem("jumping")#Out[23]: 'jump'
stemmer.stem("jumped")#Out[24]: 'jump'

###################################
"""ready reference"""
#lematizer:mapping all the words to the one word
#eg:aurangabad and sambhajinagar belongs to one place
#so we will be denoting one word for it
#lematizer looks into dictionary words
"""#eg:excellent,good,awesome,great represents 1 word
#so computation time will be increased as cpu will 
consider all this words as different words 
so we will make all this words as refered to one word
It will decrrease the computation time
"""
import nltk
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")
"""check this"""
#################################
##chunking(Shallow Parsing)Identifying named entitites
import nltk
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="we are learning NLP in python by SanjivaniAI"
##First we will tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]
"""Out[24]: [Tree('NE', [('NLP', 'NNP')]), Tree('NE', [('SanjivaniAI', 'NNP')])]"""
############################
#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning NLP in python.")
sent
#Out[14]: ['we are learning NLP in python.']

##############################
#he went to bank and checked account it was almost 0
#looking this he went ot the river bank and was crying
import nltk
nltk.download("wordnet")
from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
###o/p:Synset('savings_bank.n.02')
sentence2="it is so risky to drive over the banks of river"
print(lesk(word_tokenize(sentence2),'bank'))
#o/p:Synset('bank.v.07')
###################################
#14-06-2024
"""removing special characters

special characters ,as you know ,
are non-alphanumeric characters.
These characters are most often found in comments,
references,currency numbers etc
These characters add no value to text-understanding
and induce noice into algorithms 
for that regex package is used

"""
""" go on google and search for-> regex101.com
then ->choose the python language->choose/select/write the sentence
in the test string->select the pattern and write in that pattern column
->u will see the description """
import re#to import regex
chat1='Hello,I am having an issue with my order # 412889912 '
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern, chat1)
matches
#Out[11]: ['412889912']
##########################
chat2='Hello,I am having an issue with my order 412889912 '
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern, chat2)
matches
#Out[12]: ['412889912']
##################################
chat3='my order 412889912 is having an issue,I was charged'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern, chat3)
matches
#Out[13]: ['412889912']

#####################################
#it will be difficult to remember this all so will define in the function
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)
#Out[10]: '412889912'
#########################################
#18-06-2024


##################################33333
import re
chat1='Hi:you ask lot of questions 1235678912,abc@xyz.com'
chat2='Hi:here it is:(123)-567-8912,abc@xyz.com'
chat3='Hi:yes,phone:1235678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#Out[16]: 'abc@xyz.com'
#Out[17]: 'abc@xyz.com'
#Out[18]: 'abc@xyz.com'

###################################
#so if we want to print the "(" so we will "\(" for it 
#to extract the phone number
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
#so,here "\"states that we want as it is 
#"\d"we want digits as it is
#"{}"-we want that many number
#"|"-it acts as "or"
#get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
#Out[20]: ('', '(123)-567-8912')
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
#Out[21]: ('1235678912', '')

###############################333
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)

'''
get_pattern_match(r'age (\d+)',text)
#Out[33]: '52'
#here we want digits upto whatever it may be for that we give (\d+)
#here r is there bcoz as on regex there already *r"* ppattern is there
#we want text only after age
get_pattern_match(r'Born(.*)\n',text).strip()
#Out[26]: 'Elon Reeve Musk'
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
#Out[27]: 'June 28, 1971'
#to print the next line after born statements 
get_pattern_match(r'\(age.*\n(.*)',text)
#Out[28]: 'Pretoria, Transvaal, South Africa'

#extracting info from amazon,wikipidia
#####################################

#19-06-2024
import re
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Citizenship	
South Africa
Canada
United States
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner, CTO and Executive Chairman of X (formerly Twitter)
President of the Musk Foundation
Founder of The Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)

'''
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
    
get_pattern_match('order[^\d]*(\d*)',chat1)
##############################
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
"""Out[11]: 
{'age': 52,
 'name': 'Elon Reeve Musk',
 'birth_date': 'June 28, 1971',
 'birth_place': 'Pretoria, Transvaal, South Africa'}
"""
#########################
text='''
Born	Mukesh Dhirubhai Ambani
19 April 1957 (age 67)
Aden, Colony of Aden
(present-day Yemen)[1][2]
Nationality	Indian
Alma mater	
St. Xavier's College, Mumbai
Institute of Chemical Technology (B.E.)
Occupation(s)	Chairman and MD, Reliance Industries
Spouse	Nita Ambani ​(m. 1985)​[3]
Children	3
Parents	
Dhirubhai Ambani (father)
Kokilaben Ambani (mother)
Relatives	Anil Ambani (brother)
Tina Ambani (sister-in-law)
'''
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_information(text)
"""
Out[14]: 
{'age': 67,
 'name': 'Mukesh Dhirubhai Ambani',
 'birth_date': '19 April 1957',
 'birth_place': 'Aden, Colony of Aden'}
"""
################################
#ready reference
"""interview question:in one function ,
two parameters can be returned or not
so answer is yes .in the above function and
in the yeild keyword type of example we have used
"""
######################################
from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader('c:/1-python/kopargaon-part-1.pdf')
#printing number of pages in pdf file
print(len(reader.pages))
page=reader.pages[2]
#
text=page.extract_text()
print(text)
##################################
from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader
#creating a pdf reader object
reader=PdfReader('c:/1-python/matrix_basics.pdf')
#printing number of pages in pdf file
print(len(reader.pages))
page=reader.pages[2]
#this are the page number given which starts from 0 indexing
#so if we want 2 page then we need to give [3]
text=page.extract_text()
print(text)
###############################
#20-06-2024
#extractiong info from twitter
import re
sentence5="sharat twitted ,witnessing 68yh repulic day India from Rajpath,\new Delhi,Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+',' ',sentence5).split()
"""Out[3]: 
['sharat',
 'twitted',
 'witnessing',
 '68yh',
 'repulic',
 'day',
 'India',
 'from',
 'Rajpath',
 'ew',
 'Delhi',
 'Mesmorizing',
 'performance',
 'by',
 'Indian',
 'Army']"""
#########usecase :in election why got less votes was analyis by Ai
'''
re.sub(r'([^\s\w]|_)+',' ',some_string)
will replace sequences of non-alphanumeric characters
(including punctuation but excludng whitespace)
with a single space.This is commonly used to clean up text
by removing punctuation and other non-word characters,
making it easier to process for tasks like text analysis:
    '''
########################33333
###exrtracting n-grams-(use becoz republic and day are separated but wont have an accurate meaning so republic day wwill have an exact meaning)
#1.custom defined function
#2.NLTK
#3.TextBlob
############################333
#extracting n-grams using custom defined function
import re
def n_gram_extractor(input_str, n):
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        #this is logic for comparing 1st word with 1st+1 ie 2nd word
        print(tokens[i:i+n])
n_gram_extractor("the cute little boy is playing with kitten",2)
#it will pair 2 words together
"""['the', 'cute']
['cute', 'little']
['little', 'boy']
['boy', 'is']
['is', 'playing']
['playing', 'with']
['with', 'kitten']"""

n_gram_extractor("the cute little boy is playing with kitten",3)
#it will pair 3 words together
"""['the', 'cute', 'little']
['cute', 'little', 'boy']
['little', 'boy', 'is']
['boy', 'is', 'playing']
['is', 'playing', 'with']
['playing', 'with', 'kitten']"""

##############################






