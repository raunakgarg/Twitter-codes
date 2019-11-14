# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 09:27:47 2019

@author: garg_raunak
@comments - this code will fetch all your followers twitter handles and seprate them in files 
            based on their follwers(for example - all followers having their followers in 
            range (10000,20000) in twitter1.csv file)
            
            This will help buisnesses to  interect with the big twitter users for promotions
"""
import pandas as pd
import os
from tweepy import OAuthHandler
import tweepy
consumer_key = 'nwSwrRieacbulih58WC2vqO21'
consumer_secret = 'IStJbH45VdBIQK8FzAXHyA2iZRWx1jW5KSil8BQ6kLoBS4gomZ'
access_token = '3239874566-2y1xTQM5JAC93Y8cnoTg2mOvIURIxONtZlGj0Lp'
access_secret = 'SglXmOxC5n4ehsPEMqYtxLmBKXueuZNsvUvd8AShuBKYT'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
api.followers_ids
users = tweepy.Cursor(api.followers, screen_name="raunakgarg2").items()
temp = []
while True:
    try:
        user = next(users)
    except tweepy.TweepError:
        user = next(users)
    except StopIteration:
        break
    temp.append("@" + user.screen_name + ' ='+str(user.followers_count))
len(temp)    
dataset = pd.DataFrame(temp, columns =['handle'])
new = dataset["handle"].str.split("=", n = 1, expand = True) 
dataset["handle_name"] = new[0]
dataset["followers"] = new[1]
dataset[["followers"]] = dataset[["followers"]].apply(pd.to_numeric)
dataset = dataset.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
dataset2 = dataset[dataset['followers'].between(10000, 20000)] 
dataset2.rename(columns={'followers':'followers between 10000 and 20000'}, inplace=True)
os.makedirs("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2", exist_ok=True) 
dataset2.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter1.csv")
dataset3 = dataset[dataset['followers'].between(5000, 10000)] 
dataset3.rename(columns={'followers':'followers between 5000 and 10000'}, inplace=True)
dataset3.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter2.csv")
dataset4 = dataset[dataset['followers'].between(2000, 5000)] 
dataset4.rename(columns={'followers':'followers between 2000 and 5000'}, inplace=True)
dataset4.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter3.csv")
dataset5 = dataset[dataset['followers'].between(1000, 2000)] 
dataset5.rename(columns={'followers':'followers between 1000 and 2000'}, inplace=True)
dataset5.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter4.csv")
dataset6 = dataset[dataset['followers'].between(400, 1000)] 
dataset6.rename(columns={'followers':'followers between 400 and 1000'}, inplace=True)
dataset6.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter5.csv")
dataset7 = dataset[dataset['followers'].between(200, 400)] 
dataset7.rename(columns={'followers':'followers between 200 and 400'}, inplace=True)
dataset7.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\raunakgarg2\\twitter6.csv")

#dataset.dtypes
