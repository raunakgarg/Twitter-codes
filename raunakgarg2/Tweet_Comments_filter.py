# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:26:40 2019

@author: garg_raunak
@comments - this code will fetch all comments in any perticular tweet and get 
            all the handles commeted in that tweet so that those handles can be used to promote buisness       
            This will help buisnesses to  interect with the big twitter users for promotions.
"""
import pandas as pd
from tweepy import OAuthHandler
import tweepy
import time
timestr = time.strftime("%Y%m%d-%H%M%S")
consumer_key = 'nwSwrRieacbulih58WC2vqO21'
consumer_secret = 'IStJbH45VdBIQK8FzAXHyA2iZRWx1jW5KSil8BQ6kLoBS4gomZ'
access_token = '3239874566-2y1xTQM5JAC93Y8cnoTg2mOvIURIxONtZlGj0Lp'
access_secret = 'SglXmOxC5n4ehsPEMqYtxLmBKXueuZNsvUvd8AShuBKYT'
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True,
				   wait_on_rate_limit_notify=True)
dir(api)
api = tweepy.API(auth)

# update these for whatever tweet you want to process replies to
name = 'dhurtladki'
tweet_id = '1194528574927073281'

replies=[]
for tweet in tweepy.Cursor(api.search,q='to:'+name, result_type='recent', timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
        if (tweet.in_reply_to_status_id_str==tweet_id):
            replies.append(tweet.text)

len(replies)    
dataset = pd.DataFrame(replies, columns =['replies'])
dataset['replies'] = dataset['replies'].str.replace('@dhurtladki', '')
dataset.replies.map(lambda x: x.startswith('@'))
dataset['replies'] = dataset['replies'].astype(str)
dataset.dtypes
dataset['handles'] = dataset['replies'].str.extract(r'@(\S+)')
dataset = dataset.dropna(axis = 0) 
dataset['handles'] = '@' + dataset['handles'].astype(str)
dataset
dataset.to_csv("C:\\Users\\gargrau.corpdom\\Desktop\\python_by_ganeshan\\Twitter codes\\Comment_handles\\"+ tweet_id +" "+timestr+".csv")




