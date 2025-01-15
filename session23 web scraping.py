# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 09:36:53 2024

@author: Vaishnavi
"""
#WEBSCRAPING
#go on google and search for-> regex101.com
#STEPS:
#1.CHOOSE PYTHON LANGAUGAE
#2.CHOOSE THE SENTENCE
#3.CHOOSE THE PATTERN

""" removing special character
special character as you know are non-aplhanumeric character.
these character are most often found in comments references currency number etc
these character add no values to text understanding and induce noise ito alogorithm
for that regex pacakage is used"""

import re# enivornment > pip install regex
chat1='Hello I am having an issue with my order #412889912'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat1)
matches

chat2='I have a problem with my order number 412889912'
pattern ='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

chat3='my order 412889912 is having an issue, i was charged 300$ but online it says 280$'
pattern='order[^\d]*(\d*)'
matches=re.findall(pattern,chat2)
matches

# if we dont want to use re.findall 
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)

#18-06-2004
#how to extract email from chat
chat1='you ask lot of questions 12345678912,abc@xyz.com'
chat2='here it is:(123)-567-8912,abc@xyz.com'
chat3='yes,phone:12345678912 email:abc@xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat1)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat2)
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9]*',chat3)
#output:Out[21]: 'abc@xyz.com'
#how to extract phone no from chat
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat1)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat2)
get_pattern_match('(\d{10})|(\(\d{3}\)-\d{3}-\d{4})',chat3)
#output:1.('1234567891', '')
#putput:2('', '(123)-567-8912')
#output:3('1234567891', '')

text="""Born	Elon Reeve Musk
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
​(m. 2013; div. 2016)​"""

get_pattern_match(r'age (\d+)', text)
get_pattern_match(r'Born(.*)\n',text).strip()
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)
#output 1:Out[31]: '52'
#output 2:'Elon Reeve Musk'
#output 3:Out[34]: 'June 28, 1971'
#output 4:Out[35]: 'Pretoria, Transvaal, South Africa'

---------------------------------------------------------------
-------------------------'19/06/2024'------------------------
---------------------------------------------------------------


text='''Born	Mukesh Dhirubhai Ambani
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
Tina Ambani (sister-in-law)'''

def extract_personal_info(text):
    age=get_pattern_match('age (\d+)', text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return{
        'age':int(age),
        'name':full_name.strip(),
        'birth_date':birth_date.strip(),
        'birth_place':birth_place.strip()
        }
extract_personal_info(text)
    

#Pdf reading(Extraction)

from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader

#Creating pdf reader object
reader=PdfReader('D:/1-Python/kopargaon-part-1.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from pdf file
page=reader.pages[1]

#Extracting text from page
text=page.extract_text()
print(text)



from PyPDF2 import PdfFileReader
#importing required modules
from PyPDF2 import PdfReader

#Creating pdf reader object
reader=PdfReader('C:/1-Python/matrix_basics.pdf')

#printing number of pages in pdf file
print(len(reader.pages))

#getting a specific page from pdf file
page=reader.pages[1]

#Extracting text from page
text=page.extract_text()
print(text)


---------------------------------------------------------------
---------------------------'20/06/2024'-------------------------
---------------------------------------------------------------

#Extractiing info from twit
import re
sentence="sharad twitted , witnessing 68th republic day India from Rajpath ,\new Delhi ,Mesmorizing performance of indian Army!"
re.sub(r'([^\s\w]_)+', ' ', sentence).split()

#Extracting n -grams from sentence
     
import re
def n_gram_extraction(input_str,n):
    tokens=re.sub(r'([^\s\w]/_)+', ' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])

n_gram_extraction("The cute little boy is playing with kitten",2)

n_gram_extraction("The cute little boy is playing with kitten",3)



#Extracting all twitterhandles from following text

text = '''
Follow our leader Elon musk on twitter here: https://twitter.com/elonmusk, more information 
on Tesla's products can be found at https://www.tesla.com/. Also here are leading influencers 
for tesla related news,
https://twitter.com/teslarati
https://twitter.com/dummy_tesla
https://twitter.com/dummy_2_tesla
'''

pattern='https://twitter.com/([a-zA-Z0-9_]+)'
re.findall(pattern,text)
            

#Extracting partticular word 
text = '''
Concentration of Risk: Credit Risk
Financial instruments that potentially subject us to a concentration of credit risk consist of cash, cash equivalents, marketable securities,
restricted cash, accounts receivable, convertible note hedges, and interest rate swaps. Our cash balances are primarily invested in money market funds
or on deposit at high credit quality financial institutions in the U.S. These deposits are typically in excess of insured limits. As of September 30, 2021
and December 31, 2020, no entity represented 10% or more of our total accounts receivable balance. The risk of concentration for our convertible note
hedges and interest rate swaps is mitigated by transacting with several highly-rated multinational banks.
Concentration of Risk: Supply Risk
We are dependent on our suppliers, including single source suppliers, and the inability of these suppliers to deliver necessary components of our
products in a timely manner at prices, quality levels and volumes acceptable to us, or our inability to efficiently manage these components from these
suppliers, could have a material adverse effect on our business, prospects, financial condition and operating results.
'''
pattern = 'Concentration of Risk:([^\n]*)'
re.findall(pattern,text)

#Extract Number Orders
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern='FY(\d{4} (?:Q[1-4]|S[1-2]))' #? : match this
matches=re.findall(pattern,text)
matches


###########################################
text='''
Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches

#################################################################
#Extracting  notes, names from this text
text = '''
Note 1 - Overview
Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”) was incorporated in the State of Delaware on July 1, 2003. We design, develop, manufacture and sell high-performance fully electric vehicles and design, manufacture, install and sell solar energy generation and energy storage
products. Our Chief Executive Officer, as the chief operating decision maker (“CODM”), organizes our company, manages resource allocations and measures performance among two operating and reportable segments: (i) automotive and (ii) energy generation and storage.
Beginning in the first quarter of 2021, there has been a trend in many parts of the world of increasing availability and administration of vaccines
against COVID-19, as well as an easing of restrictions on social, business, travel and government activities and functions. On the other hand, infection
rates and regulations continue to fluctuate in various regions and there are ongoing global impacts resulting from the pandemic, including challenges
and increases in costs for logistics and supply chains, such as increased port congestion, intermittent supplier delays and a shortfall of semiconductor
supply. We have also previously been affected by temporary manufacturing closures, employment and compensation adjustments and impediments to
administrative activities supporting our product deliveries and deployments.
Note 2 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated balance sheet as of September 30, 2021, the consolidated statements of operations, the consolidated statements of
comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September
30, 2021 and 2020 and the consolidated statements of cash flows for the nine months ended September 30, 2021 and 2020, as well as other information
disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2020 was derived from the audited
consolidated financial statements as of that date. The interim consolidated financial statements and the accompanying notes should be read in
conjunction with the annual consolidated financial statements and the accompanying notes contained in our Annual Report on Form 10-K for the year
ended December 31, 2020.
'''

pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern,text)
matches

###################################################################33
#Extract Financial periods from a company
text = '''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text)
matches



text = '''
The gross cost of operating lease vehicles in Fy2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion. 
'''
pattern='FY\d{4} Q[1-4]'
matches=re.findall(pattern,text,flags=re.IGNORECASE)
matches


-------------------------------------------------------------------
#Assignment 
text='''Thanks Flipkart for delivering the product in ontime. 
The color of the watch is not pink... On other platforms like amazon
the same watch was at Rs.1299 i bought it from flipkart just at
Rs.1000.
it is available in .cream color,black color,white color.
This is a cream color.... But in day and nght this are
 different color shade are shown... Nice watch .
 Also good deisgned include good fetures. 
 The all watch faces including ediing ysstem are done in noise fit App. 
 '''
import re
import nltk 
from nltk import word_tokenize
word=word_tokenize(text)
word

from nltk import sent_tokenize
sent=sent_tokenize(text)
sent

re.sub(r'([^\s\w]_)+', ' ', text).split()

from autocorrect import Speller
spell=Speller(lang='en')
spell(text)

rep=text.replace("noise","Boat")
rep

rep=re.sub(r'Noise','Boat',text,flags=re.IGNORECASE)
rep

pattern='Rs.(\d+)'
matches=re.findall(pattern,text)
matches

pattern='([^\n]*) color'
matches=re.findall(pattern,text)
matches


----------------------------------------------------------------
-----------------------"21/06/2024"-----------------------------
----------------------------------------------------------------

from nltk import ngrams
#extraction of n-grams with nltk
list(ngrams("The cute little boy is playing with kitten".split(),2))
list(ngrams("The cute little boy is playing with kitten".split(),3))

#########################################################

from textblob import TextBlob
blob=TextBlob("The cute little boy is playing with kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)

############################################################

from tensorflow.keras.preprocessing.text import text_to_word_sequence
sentence="sharad twitted , witnessing 68th republic day India from Rajpath ,\new Delhi ,Mesmorizing performance of indian Army!"
text_to_word_sequence(sentence)
###########################################################

#Tokenization using TextBlob

from textblob import TextBlob
sentence="sharad twitted , witnessing 68th republic day India from Rajpath ,\new Delhi ,Mesmorizing performance of indian Army!"
blob=TextBlob(sentence)
blob.words

#Tweet Tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence)

##############################################################
from nltk.tokenize import MWETokenizer
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence.split())
mwe_tokenizer.tokenize(sentence.replace('!',' ').split())


