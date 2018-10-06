import config as config
import tweepy

SEARCH_TERM = 'stablecoin'

# Authentication
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

#  Retrieve tweets with search term
search_res = api.search(SEARCH_TERM, count=100, result_type='recent', include_entities=True)
# Filter to only get tweets with links
res_with_urls = filter(lambda x: len(x.entities['urls']) > 0, search_res)

# Retrieve urls from status objects
urls = map(lambda x: x.entities['urls'][0]['expanded_url'],res_with_urls)

# Remove tweet links with twitter in the url
urls = filter(lambda x: x.find('https://twitter.com') == -1, urls)

# Remove duplicates
urls = list(set(urls))

print(list(urls))