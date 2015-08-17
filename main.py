#coding: utf-8
import tweepy
import datetime

# Authentication:
consumer_key = '********'
consumer_secret = '********'
access_token = '********'
access_token_secret = '********'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def add_tomori_nao(status_object):
    splited_array = status_object.text.split()
    url = 'https://twitter.com/kokodeikku_bot/status/' + str(status_object.id)
    return splited_array[1] + ' ' + splited_array[2] + ' ' + u'友利奈緒' + url.decode('utf8')

recent_tweets = api.user_timeline('kokodeikku_bot')
new_tweets = []

now_minute = datetime.datetime.now().minute

for i in recent_tweets:
    post_minute = i.created_at.minute
    if post_minute == now_minute - 1:
        tweet = add_tomori_nao(i)
        api.update_status(status=tweet.encode('utf8'))
    elif post_minute < now_minute - 1:
        break
