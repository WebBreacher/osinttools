from twitter_keys import *

import csv
import json
import requests
import time


logfile   = 'rockville.csv'
latitude  = 39.106011097700915
longitude = -77.09330247246095
radius    = 2

#
# Send request to Twitter API
#
def send_geo_radius_request(latitude, longitude, radius, max_id=None):

    url = 'https://api.twitter.com/1.1/search/tweets.json'

    params = {
        'q':        '',
        'geocode':  '%f,%f,%fkm' % (latitude, longitude, radius),
        'count':    200,
    }

    if max_id is not None:
        params['max_id'] = max_id

    # send request to Twitter
    response = requests.get(url, params=params, auth=oauth)

    if response.status_code == 200:

        tweets = json.loads(response.content)

        return tweets

    return None


#
# Takes a latitude, longitude and radius
#
def geo_search(latitude, longitude, radius):
    geo_tweet_list  = []
    max_id          = 0

    while True:

        # request some tweets in a geographic area
        tweet_list = send_geo_radius_request(latitude, longitude, radius, max_id)

        # bail out of the loop if we don't get any new tweets
        if tweet_list is None or len(tweet_list['statuses']) == 0:
            break

        # grab the oldest Tweet
        oldest_tweet = tweet_list['statuses'][-1]

        # set max_id to latest max_id we retrieved, minus 1
        max_id = oldest_tweet['id'] - 1

        geo_tweet_list.extend(tweet_list['statuses'])

        print('[*] Retrieved: %d Tweets (max_id: %d)' % (len(geo_tweet_list), max_id))

        # sleep to handle rate limiting
        time.sleep(3)

    # return the full Tweet list
    return geo_tweet_list


#
# Print and log the results.
#
def log_results(tweets, logfile):

    field_names = ['latitude', 'longitude', 'date', 'user', 'text']

    with open(logfile, 'w', newline='') as fd:

        writer = csv.DictWriter(fd, fieldnames=field_names)

        writer.writeheader()

        for tweet in tweets:

            # Tweet was geotagged
            if tweet.get('geo', None):
                latitude, longitude = tweet['geo'].get('coordinates')

            # Retweeted Tweet that was geotagged
            elif tweet.get('retweeted_status', None):
                latitude, longitude = tweet['retweeted_status']['geo'].get('coordinates')

            # For some reason we have no geographic information, set to zero
            else:
                latitude  = 0.0
                longitude = 0.0

            row = {
                'latitude':   latitude,
                'longitude':  longitude,
                'date':       tweet['created_at'],
                'user':       tweet['user']['screen_name'],
                'text':       tweet['text'].encode('utf-8')
            }

            output = '%f,%f,%s,%s,"%s"' % (
                row['latitude'],
                row['longitude'],
                row['date'],
                row['user'],
                row['text'].decode('utf-8')
            )

            print(output)

            writer.writerow(row)

    return


tweets = geo_search(latitude, longitude, radius)

log_results(tweets, logfile)