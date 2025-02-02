# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:46:26 2024

@author: Vaishnavi
"""

from bs4 import BeautifulSoup as bs
import requests
link="https://www.imdb.com/title/tt0068646/reviews?ref=tt_urv"
page=requests.get(link)
page#Out[5]: <Response [200]>
page.content
soup=bs(page.content,'html.parser')
print(soup.prettify())
###########################
title=soup.find_all('a',class_="title")
title
len(title)#len(title)Out[17]: 25
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
len(review_title)#Out[91]: 25
review_title[:]=[title.strip('\n') for title in review_title]
review_title
len(review_title)
#len(review_title)
#Out[94]: 25

##########################
#we got 25 review title
#now let us scrap rating
#rating=soup.find_all('svg',class='ipl-icon ipl-star-icon')
rating=soup.find_all('span',class_='point-scale')
rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate
rate[:]=[r.strip('/') for r in rate]
rate
len(rate)#Out[116]: 23

rate.append('')
rate.append('')
len(rate)#Out[119]: 25
####################3

#now let us scrap the review body
#review=soup.find_all('div',class_='text show-more__control')
review=soup.find_all('div',class_='text')
review
review_body=[]
for i in range(0,len(review)):
    review_body.append(review[i].get_text())
review_body
len(review_body)#Out[132]: 25
###we got 25 review_body
###now we have to save the data in .csv file
#pip install textblob-this is for sentiment analysis
import pandas as pd
df=pd.DataFrame()
df['Review_Title']=review_title
df['Rate']=rate
df['Review']=review_body
df
####################
##3to create .csv file
df.to_csv('C:/8-text_mining/GodFather_reviews.csv')
####################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
sent="This is very excellent garden"
pol=TextBlob(sent).sentiment.polarity
pol#Out[146]: 1.0
df=pd.read_csv("C:/8-text_mining/GodFather_review.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
"""Out[152]: 
0     0.057229
1     0.283696
2     0.612500
3     0.276389
4     0.442500
5     0.149239
6     0.265476
7     0.401927
8     0.133346
9     0.309705
10    0.271324
11    0.142807
12    0.235417
13    0.221324
14    0.550000
15    0.151895
16    0.191168
17   -0.035511
18    0.330000
19    0.220242
20    0.201516
21    0.336979
22    0.301783
23    0.259833
24    0.316667
Name: polarity, dtype: float64"""
