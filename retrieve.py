import tweepy
from tweepy import OAuthHandler
import config as config

# print(config.access_token_secret)

# consumer_key = 'YOUR-CONSUMER-KEY'
# consumer_secret = 'YOUR-CONSUMER-SECRET'
# access_token = 'YOUR-ACCESS-TOKEN'
# access_secret = 'YOUR-ACCESS-SECRET'
#
# auth = OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_secret)
#
# api = tweepy.API(auth)

import tweepy

auth = tweepy.OAuthHandler(config.api_key, config.api_secret)
auth.set_access_token(config.access_token, config.access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)