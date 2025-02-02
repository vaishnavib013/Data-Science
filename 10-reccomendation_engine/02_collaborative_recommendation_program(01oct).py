# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 08:45:02 2024

@author: Vaishnavi
#go throught the algebra related to this 
"""
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#load the csv file
file_path="C:/10-Reccomendation_engine/game.csv"
data=pd.read_csv(file_path)

#step1:create a user-item (rows:users,columns:games,values:rating)
user_item_matrix=data.pivot_table(index='userId',columns='game',values='rating')

"""pivot_table:this function reshapes the dataframe into a matrix where:
    each row represents a user(identified by userId)
    each column represents a game (identified by game )
    the values in the matrix represents the ratings that user gave the game """
    
#step2 fill NAN values with 0 (assumming no rating means the game has not been rated)
user_item_matrix_filled=user_item_matrix.fillna(0)
"""this line replace any missing values(Nans)
in the user -item matrix with 0,
indicating that the user did not rate that particular game """
"""pivot_table:this function reshapes the DataFrame into a matrix where:
    Each row represents a user (identified by userId)
    """
#step 3:compute the cosine similarity between users based on raw ratings
user_similarity=cosine_similarity(user_item_matrix_filled)

#convert similarity matrix to a Data Frame for easy reference
user_similarity_df=pd.DataFrame(user_similarity,index=user_item_matrix.index,columns=user_item_matrix.index)

#step4:Function to get the game recommendations for a specific user based on 
def get_collaborative_recommendation_for_user(user_id,num_recommendation=5):
    #get the similarity scores for the input user with all other users:
    similar_users=user_similarity_df[user_id].sort_values(ascending=False)
    
    #get the most similar users(excluding the user themselves)
    similar_users=similar_users.drop(user_id)
    
    #select the top N similar users to limit the noise(eg.,top 50 users)
    top_similar_users=similar_users.head(50)
    #this selects the top 50 most similar users to limit noise in the recommendation system
    #get ratings of these similar users,weighted by their similarity score
    weighted_ratings=np.dot(top_similar_users.values,user_item_matrix_filled.loc[top_similar_users.index])
    #np.dot:this computes the dot product between the similarity scores of thr top similar users and
    #their corresponding ratings in the user-item matrix.
    #the result is an array of weighted ratings for each game.
    #normalize by the sum of similarities
    sum_of_similarities=top_similar_users.sum()
    
    if sum_of_similarities >0:
        weighted_ratings/=sum_of_similarities
        #the weighted ratings are normalized by dividing by the sum of similarities 
        #to avoid biasing towards users with higher ratings
        
        
    #recommend games that the user hasn't rated yet
    user_ratings=user_item_matrix_filled.loc[user_id]
    unrated_games=user_ratings[user_ratings==0]
    #this identifies the games that tje target user has not rated(ie.,rated 0)
    
    #get the weighted scores for unrated games
    game_recommendations=pd.Series(weighted_ratings,index=user_item_matrix_filled.columns).loc[unrated_games.index]
    #this creates a pandas Series from the weighted ratings
    #and filters it to include only the unrated games.
    #finally,it sorts the recommendations in descending order
    
    return game_recommendations.sort_values(ascending=False).head(num_recommendation)

#example usage:get recommendations for a user with ID 3
recommended_games=get_collaborative_recommendation_for_user(user_id=3)

#print the recommended games
print("Recommended games for user 3:")
print(recommended_games)
"""game
'Splosion Man         0.0
Resogun               0.0
Resogun: Heroes       0.0
Retro City Rampage    0.0
Retro/Grade           0.0
dtype: float64"""

#for different user_id we get different ratings
recommended_games=get_collaborative_recommendation_for_user(user_id=22)

#print the recommended games
print("Recommended games for user 22:")
print(recommended_games)
"""Recommended games for user 22:
game
Alan Wake: The Writer                 0.728709
Command & Conquer 3: Tiberium Wars    0.666940
World of Tanks                        0.666940
'Splosion Man                         0.000000
Retro City Rampage                    0.000000
dtype: float64"""