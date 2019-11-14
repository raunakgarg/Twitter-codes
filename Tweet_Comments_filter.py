# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:26:40 2019

@author: garg_raunak
@comments - this code will fetch all comments in any perticular tweet and get 
            all the handles commeted in that tweet so that those handles can be used to promote buisness       
            This will help buisnesses to  interect with the big twitter users for promotions.
"""
import pandas as pd

#https://twitter.com/dhurtladki/status/1194528574927073281?s=20
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
dir(api)

users = api.show_friendship(screen_name="dhurtladki", )
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





replies=[] 
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)  
for full_tweets in tweepy.Cursor(api.user_timeline,screen_name=name,timeout=999999).items(10):
  for tweet in tweepy.Cursor(api.search,q='to:'+name,result_type='recent',timeout=999999).items(1000):
    if hasattr(tweet, 'in_reply_to_status_id_str'):
      if (tweet.in_reply_to_status_id_str==full_tweets.id_str):
        replies.append(tweet.text)
  print("Tweet :",full_tweets.text.translate(non_bmp_map))
  for elements in replies:
       print("Replies :",elements)
  replies.clear()
















