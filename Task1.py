# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 11:37:15 2024

@author: Vaishnavi
"""

import bs4
from bs4 import BeautifulSoup as bs
import requests
link="https://www.amazon.in/product-reviews/B08HNGK3B7"
page=requests.get(link)
page
page.content
## now let us parse the html page
soup=bs(page.content,'html.parser')
print(soup.prettify())
#when you parse HTML using BeautifulSoup, you are converting the 
#raw HTML content of a web page into a structured format, 
#like a tree, where you can easily locate and manipulate individual 
#elements (such as tags, attributes, or text).

#page.content=> provides the raw HTML content,
#while soup.prettify()=> offers a formatted, human-readable version of the parsed HTML content.

## now let us scrap the contents
names=soup.find_all('span',class_="a-profile-name")
names
### but the data contains with html tags,let us extract names from html tags
cust_names=[]
for i in range(0,len(names)):
    cust_names.append(names[i].get_text())
    
cust_names
len(cust_names)
cust_names.pop(-1)
cust_names.pop(-1)
cust_names.pop(-1)
cust_names.pop(-1)
len(cust_names)


### There are total 11 users names 
#Now let us try to identify the titles of reviews

title_rate=soup.find_all('a',class_='review-title')
tr_list = [x.text.strip() for x in title_rate]
tr_list
len(tr_list)
ratings = []
reviews = []

# Process each entry in tr_list
for i in tr_list:
    rating, review = i.split('\n', 1)
    ratings.append(rating)
    reviews.append(review)
ratings 
reviews 
rate = [int(i[0]) for i in ratings]
print(rate)
len(rate )
len(reviews )




## now let us scrap review body
reviews=soup.find_all("div",class_="a-row a-spacing-small review-data")
reviews
review_body=[]
for i in range(0,len(reviews)):
    review_body.append(reviews[i].get_text())
review_body
review_body=[ reviews.strip('\n\n')for reviews in review_body]
review_body
len(review_body)

    

##########################################
###convert to csv file
import pandas as pd
df=pd.DataFrame()
df['customer_names']=cust_names
df['review_title']=reviews
df['rate']=rate
df['review_body']=review_body
df
df.to_csv('C:\8-Text Mining\Text_MIning\Amazon_shoes_reviews.csv',index=True)
########################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob

df=pd.read_csv("C:\8-Text Mining\Text_MIning\Amazon_shoes_reviews.csv")
df.head()
df['polarity']=df['review_body'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']