# -*- coding: utf-8 -*-
"""Created on Thu Oct 17 08:40:39 2024
@author: Vaishnavi
"""
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfTransformer
######################Loading the dataset
email_data=pd.read_csv("C:/11-KNN/sms_raw_NB.csv",encoding="ISO-8859-1")
##These sms are in text form ,open the dataframe and there are ham or spam
###cleaning the data
#the function tokenizes the text and removes words
#with fewer than 4 characters 
import re
def cleaning_text(i):
    i=re.sub("[^A-Z a-z""]+"," ",i).lower()
    w=[]
    ##everything else A to Z and a to z is going to convert to space and 
    #we will take each row and tokeinze
    for word in i.split(" "):
        if len(word)>3:
            w.append(word)
    return(" ".join(w))
##Testing above function with sample text
    cleaning_text("Hope you are having good week.just checking")
    cleaning_text("hope i can i understand your feeling12321.123.hi how are")
    cleaning_text("Hi how are you")
##Note the dataframe size is 5559 ,2,now removing empty spaces
#removing empty rows
email_data=email_data.loc[email_data.Message !=" ",:]
email_data.shape
##you can use count vectorizer which is directly converts a collection of documnet
##first we will split the data
from sklearn.model_selection import train_test_split
email_train,email_test=train_test_split(email_data,test_size=0.2)

#splits each email into a list of words 
##creating matrix of token count for entire dataframe
def split_into_words(i):
    return[word for word in i.split(" ")]
##defining the preparation of email text into word count matrix format
#CountVectorizer:converts the email into a matric of token counts
#.fit():learns the vocabulary form the text data
#.transform():converts text data into a token count matrix
emails_bow=CountVectorizer(analyzer=split_into_words).fit(email_data.Message)
#defining bow for all dataframes
all_emails_matrix=emails_bow.transform(email_data.Message)
train_email_matrix=emails_bow.transform(email_train.Message)
#for testing messages
test_email_matrix=emails_bow.transform (email_test.Message)
#learning term weighting and normalizing entire emails
tfidf_transformer=TfidfTransformer().fit(all_emails_matrix)
##preparing TFIDF for train emails
train_tfidf=tfidf_transformer.transform(train_email_matrix)
train_tfidf.shape
test_tfidf=tfidf_transformer.transform(test_email_matrix)
test_tfidf.shape
##now apply naive bayes
from sklearn.naive_bayes import MultinomialNB as MB
classifier_mb=MB()
classifier_mb.fit(train_tfidf,email_train.type)

#email_train.type:this is the column 

#the .type attribute refers to that specific column
#in the email_train dataframe



###evaluation on test data
test_pred_m=classifier_mb.predict(test_tfidf)

#calculating accuracy
accuracy_test_m=np.mean(test_pred_m==email_test.type)
accuracy_test_m
#evaluation on test data accuracy matrix
from sklearn.metrics import accuracy_score
accuracy_score(test_pred_m,email_test.type)
pd.crosstab(test_pred_m,email_test.type)

#Training Data accuracy
train_pred_m=classifier_mb.predict(train_tfidf)
accuracy_train_m=np.mean(train_pred_m==email_train.type)
accuracy_train_m
###






classifier_mb_lap=MB(alpha=3)
classifier_mb_lap.fit(train_tfidf,email_train.type)
##accuracy after tuning
test_pred_lap=classifier_mb_lap.predict(test_tfidf)
accuracy_test_lap=np.mean(test_pred_lap==email_test.type)
accuracy_test_lap
accuracy_score(test_pred_lap,email_test.type)

from sklearn.metrics import accuracy_score
accuracy_score(test_pred_lap,email_test.type)
pd.crosstab(test_pred_lap,email_test.type)

#training data accuracy
train_pred_lap=classifier_mb_lap.predict(train_tfidf)
accuracy_train_lap=np.mean(train_pred_lap==email_train.type)
accuracy_train_lap






