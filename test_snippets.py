from tweepy import OAuthHandler
import config as config
import tweepy

auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

# needs tweet mode = 'extended' in order to get correct urls
# https://stackoverflow.com/questions/46957834/tweepy-instead-of-getting-the-url-shared-in-the-twitter-im-getting-the-tweet
t = api.get_status(1047889419406123009, tweet_mode = 'extended')
t.entities['urls']