'''
Script from Justin Seitz's https://learn.automatingosint.com/ Course
and Modified for Python 3 by Micah Hoffman
'''

from twitter_keys import *

import json
import requests
import time


#
# Download Tweets from a user profile
#
def download_tweets(screen_name, number_of_tweets, max_id=None):

    api_url  = '%s/statuses/user_timeline.json' % base_twitter_url

    params  = {
        'screen_name':  screen_name,
        'count':        number_of_tweets,
    }

    if max_id is not None:
        params['max_id'] = max_id

    # send request to Twitter
    response = requests.get(api_url, params=params, auth=oauth)

    if response.status_code == 200:

        tweets = json.loads(response.content)

        return tweets

    return None

#
# Takes a username and begins downloading all Tweets
#
def download_all_tweets(username):
    full_tweet_list = []
    max_id          = None
    oldest_tweet    = {}

    # loop to retrieve all the Tweets
    while True:

        # grab a block of 200 Tweets
        tweet_list   = download_tweets(username, 200, max_id)

        # if we didn't get any tweets, we are done
        if tweet_list is None or len(tweet_list) == 0:
            break

        # grab the oldest Tweet
        oldest_tweet = tweet_list[-1]

        full_tweet_list.extend(tweet_list)

        # set max_id to latest max_id we retrieved, minus 1
        max_id = oldest_tweet['id'] - 1

        print('[*] Retrieved: %d Tweets (max_id: %d)' % (len(full_tweet_list), max_id))

        # sleep to handle rate limiting
        time.sleep(3)

    # return the full Tweet list
    return full_tweet_list


full_tweet_list = download_all_tweets('jms_dot_py')

# loop over each Tweet and print the date and text
for tweet in full_tweet_list:

    print('%s\t%s' % (tweet['created_at'], tweet['text']))
