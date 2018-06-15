from twitter_keys import *

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

import json
import codecs


class StdOutListener(StreamListener):

    #
    # Receives messages as they come in from Twitter
    #
    def on_data(self, data):

        # convert from JSON to a dictionary
        tweet = json.loads(data)

        # log the Tweet to a file
        '''with codecs.open('tweets.log', 'ab', encoding='utf-8') as fd:
            fd.write('%s\r\n' % tweet)'''

        # print the tweet out
        print(tweet['text'], tweet['user']['screen_name'])

        return True

    #
    # Receives error messages from the Twitter API
    #
    def on_error(self, status):
        print('[!] ERROR: %s' % status)


l = StdOutListener()
auth = OAuthHandler(client_key, client_secret)
auth.set_access_token(token, token_secret)

stream = Stream(auth, l)

# These IDs re for CNNBreaking and BBCWorld Twitter accounts
#stream.filter(follow=['428333','742143'])
stream.filter(track=['osint','open source intel','sec487'])