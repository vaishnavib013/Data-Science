# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 09:27:32 2024

@author: Vaishnavi
"""
#COMPLETED
#basics of ptython(LIST,DICTIONARY,TUPLES,SETS,)
#advance python(DECORATORS,LIST COMPREHENSION,)
#python for DS(DATAFRAMES)
"""
#PYTHON FOR NLP
#NLP:natural language processing
to convert the reviews (mobile language like gm,gn,tc)
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
#data scientist:stastics(deep learning),ml,ts,ai,python,sql,tabular/powerbi,nlp
#data analatics:excel,python,sql,tabular/powerbi,nlp
#test basics of python,advance python ,python for data science
#PYTHON FOR NLP
# web scraping>filter>leminization>(preprocessing)>vector>applied to ml
#FEATURE ENGINEERING IS A PROCESS OF EXTRATING FEATURES FROM RAW DATA """


########interview questions on nlp will be on stemming,lematizer etc...

#STart from basics of nlp
sentence="we are learning textmining from sanjivani AI"
sentence.index("learning")#if we want to know the position of learning 
#output:7 # this we saw by text
sentence.split().index("textmining")#it will split the words in list and count the position
#output:3 beacuse it is located on 3 position
sentence.split()
#if you want to see the list 
#output:['we', 'are', 'learning', 'textmining', 'from', 'sanjivani', 'AI']

#suppose we want to print any word in reverse order
sentence.split()[2][::-1]
#output:gninrael

#suppose want to print first and last word of the sentence
words=sentence.split()#tokenization
first_word=words[0]
first_word
last_word=words[-1]
last_word
#now we want to concate the first and last word
concat_word=first_word+" "+last_word
concat_word
#output:'we AI'

#we want to print even words from the sentences
[words[i] for i in range(len(words)) if i%2==0]
#words having odd length will not be printed
#output:['we', 'learning', 'from', 'AI']

#now we want to display only AI
sentence[-2:]
#it will start from -3,-2,-1 i.e.AI
#output:'AI'

#suppose we want to display entire sentence in reverse order
sentence[::-1]
#output:'IA inavijnas morf gninimtxet gninrael era ew'

#suppose we want to select each word and print in reversed 
words
print(" ".join(word[::-1]for word in words))
#output:ew era gninrael gninimtxet morf inavijnas IA

#####################
#tokenization:splitting of words(seprating words)
#nltk is a pacakage where all the functions of that thing is present
import nltk
nltk.download('punkt')
from nltk import word_tokenize
words=word_tokenize("i am reading nlp fundamentals")
print(words)
#output:['we', 'are', 'learning', 'textmining', 'from', 'sanjivani', 'AI'] here the words will be seprated by commas this is tokenization

#parts of speech(pos) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
#output:['we', 'PRP'),('are', 'VBP'),('learning', 'VBG'),('textmining', 'VBG'),('from', 'IN'),('sanjivani', 'NN'),('AI', 'NNP')]

#stop words from nltk library
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords') 
stop_words=stopwords.words('English')
#you can verify 179 stop words in variable exploral
print(stop_words)

#13-06-24
#normalization this convert into human readable form 
sentence2="i visisted my from ind on 14-02-19"
normalized_sentence=sentence2.replace("my","malaysia").replace("ind","india")#here we replacing my with malaysia and ind to india #if we have to do more words then use .replace and same process
normalized_Sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)

#AUTOCOREECT PACAKAGE FOR AUTO COREECTION OF WORDS
# suppose there is mistake of spelling with the help of autocorrection is will be sorted
#declare the function speller defined fot english
#declare en for the english language 
#for marathi it will be mr

from autocorrect import Speller
spell=Speller(lang='en')
spell("engilish")

#autocorrection for sentences
import nltk
nltk.download('punkt')
from nltk import word_tokenize
sentence3="ntural langage processin deals wiith the aart of extract"
sentence3=word_tokenize(sentence3)
corrected_sentence=" ".join([spell(word) for word in sentence3])
print(corrected_sentence)

#STEMMING:removing ing,ed etc from words
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("jumping")
stemmer.stem("jumped")
stemmer.stem("playing")

#LEMATIZER:one words having many meaning or other name suppose khushi is there khushi has some pet names 
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programms")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")

#chunking (shallow parsing) identifying named entities
import nltk
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="we are learning nlp in python by sanjivaniai "
#first we will tokenize
nltk.download('averaged_perceptron_tagger')
words=word_tokenize(sentence4)
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words,binary=True)
[a for a in i if len(a)==1]

#sentence tokenization
from nltk.tokenize import sent_tokenize
sent=sent_tokenize("we are learning nlp in python")
sent
#output:['we are learning nlp in python']

from nltk.wsd import lesk
sentence1="keep your savings in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
#output:synset('savings_bank.n.02)
sentence2="it is so risky to drive over the banks of rivers"
print(lesk(word_tokenize(sentence2),'bank'))
#output:synset('bank.v.07')


