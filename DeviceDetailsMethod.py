# -*- coding: utf-8 -*-
"""
Created on Fri Feb 15 22:13:06 2019

@author: S533488
"""

def DeviceDetails(TweetsData):
    from textblob import TextBlob
    import sys, tweepy
    import matplotlib.pyplot as plt
    import pickle
    import numpy as np
    import datetime
    from collections import Counter
    
    device_details = [tweet.source for tweet in TweetsData]
    TwitterWebClient = 0
    TweetDeck = 0
    TwitterIphone = 0
    SocialFlow = 0
    TwitterMediaStudio = 0

    for device in device_details:
        if str(device) == "Twitter Web Client":
            TwitterWebClient = TwitterWebClient + 1;
        elif str(device) == "TweetDeck":
            TweetDeck = TweetDeck + 1
        elif str(device) == "Twitter for iPhone":
            TwitterIphone = TwitterIphone + 1
        elif str(device) == "SocialFlow":
            SocialFlow = SocialFlow + 1  
        else: 
            TwitterMediaStudio = TwitterMediaStudio + 1
     
    Devices = ('Twitter Web Client', 'TweetDeck', 'Twitter for iPhone', 'SocialFlow', 'TwitterMediaStudio')
    y_pos = np.arange(len(Devices))
    NoOfTimesDeviceUsed = [TwitterWebClient,TweetDeck,TwitterIphone,SocialFlow,TwitterMediaStudio]
 
    plt.bar(y_pos, NoOfTimesDeviceUsed, align='center', alpha=0.5)
    plt.xticks(y_pos, Devices, fontsize=10, rotation=90)
    plt.ylabel('Number of times device used')
    plt.title('How many types each device used') 
    plt.show()