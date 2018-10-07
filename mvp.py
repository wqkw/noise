import config as config
import tweepy
import random

def run():
    # Specify what to search for on twitter
    SEARCH_TERM = 'stablecoin'

    # Authentication
    auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
    auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)

    # Retrieve tweets with search term
    search_res = api.search(SEARCH_TERM, count=100, result_type='recent', include_entities=True)

    # Filter to only get tweets with links
    res_with_urls = filter(lambda x: len(x.entities['urls']) > 0, search_res)

    # Retrieve urls from status objects
    urls = map(lambda x: x.entities['urls'][0]['expanded_url'], res_with_urls)

    # Remove tweet links with twitter in the url
    urls = filter(lambda x: x.find('https://twitter.com') == -1, urls)

    # Remove duplicates
    urls = list(set(urls))

    # The particular url to post
    if len(urls) == 0:
        print('No tweets with urls, returning None')
        return None
    else:
        use_url = urls[0]

    # Posts the url
    adj = random.choice(['Interesting', 'Cool', 'Fascinating', 'Intriguing', 'Compelling', 'Great'])
    noun = random.choice(['article', 'piece', 'feature'])
    outtro = random.choice(['Definitely worth checking out!', 'Check it out!', 'Worth giving it a read!'])
    status_format = '{} {} on #{}. {} {}'.format(adj, noun, SEARCH_TERM, outtro ,use_url)
    val = api.update_status(status_format)
    return val.id


if __name__ == '__main__':
    ret_val = run()
