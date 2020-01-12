import tweepy as tp
import time
import os

# credentials to login to twitter api

consumer_key = ''
consumer_secret = ''
access_token = ''
access_secret = ''

#loggin in to bot

auth = tp.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tp.API(auth)

os.chdir('skaters')

# iterates over pictures in models folder

for skater_image in os.listdir('.'):
    api.update_with_media(skater_image)
    time.sleep(6)