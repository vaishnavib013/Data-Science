# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 09:38:46 2024

@author: Vaishnavi
"""
#import neceessary libraries
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

#load the csv file
file_path="C:/10-Reccomendation_engine/Entertainment.csv"
data=pd.read_csv(file_path)

#step1:normalize the review scores
#we use MinMaxScaler to scale the reviews between 0 to 1
scaler=MinMaxScaler()
data['Normalized_Reviews']=scaler.fit_transform(data[['Reviews']])

#step2:Compute the cosine similarity between titles based onthe normalized reviews
cosine_sim_reviews=cosine_similarity(data[['Normalized_Reviews']],data[['Normalized_Reviews']])








