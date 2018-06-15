from twitter_keys import *

import json
import requests
import time


#
# Main Twitter API function for sending requests
#
def send_request(screen_name, relationship_type, next_cursor=None):

    api_url = 'https://api.twitter.com/1.1/%s/ids.json' % relationship_type

    params = {
        'screen_name':  screen_name,
        'count':        5000,
    }

    if next_cursor is not None:
        params['cursor'] = next_cursor

    response = requests.get(api_url, params=params, auth=oauth)

    time.sleep(3)

    if response.status_code == 200:

        result = json.loads(response.content)

        return result

    return None


#
# Function that contains the logic for paging through results
#
def get_all_friends_followers(username, relationship_type):

    account_list = []
    next_cursor  = None
    accounts     = {}

    while next_cursor not in (-1,0):

        accounts    = send_request(username, relationship_type, next_cursor)

        # break out of the loop if we don't receive any accounts
        # or the call fails
        if accounts is None:

            break

        account_list.extend(accounts['ids'])

        print('[*] Downloaded %d of type %s' % (len(account_list), relationship_type))

        next_cursor = accounts.get('next_cursor', None)

    return account_list


username = 'jms_dot_py'

friends   = get_all_friends_followers(username, 'friends')
followers = get_all_friends_followers(username, 'followers')

print('[**] Retrieved %d friends' % len(friends))
print('[**] Retrieved %d followers' % len(followers))

snapshot_timestamp = time.time()

# store the friends
friends_file = '%s-%f-friends.txt' % (username, snapshot_timestamp)
with open(friends_file, 'w') as fd:
    for friend in friends:
        fd.write('%d\n' % friend)

print('[!] Stored friends in %s' % friends_file)

# store the followers
followers_file = '%s-%f-followers.txt' % (username, snapshot_timestamp)
with open(followers_file, 'w') as fd:
    for follower in followers:
        fd.write('%d\n' % follower)

print('[!] Stored followers in %s' % followers_file)
