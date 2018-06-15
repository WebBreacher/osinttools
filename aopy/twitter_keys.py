from requests_oauthlib import OAuth1

# authentication pieces
client_key    = ''
client_secret = ''
token         = ''
token_secret  = ''

# the base for all Twitter calls
base_twitter_url = 'https://api.twitter.com/1.1/'

# setup authentication
oauth = OAuth1(client_key, client_secret, token, token_secret)
