'''
Script from Justin Seitz's https://learn.automatingosint.com/ Course
and Modified for Python 3 by Micah Hoffman

this recursively grabs that followers from a single person

'''

from twitter_keys import *

import json
import requests
import time
import networkx as nx

recurse = 2 
username = 'webbreacher'


#
# Main Twitter API function for getting friends and followers from a username
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

    #time.sleep(3)

    if response.status_code == 200:

        result = json.loads(response.content)

        return result

    return None


#
# Function that looks up a Twitter ID and returns Name (Screen_name)
#
def id_lookup(id, next_cursor=None):

    url = 'https://api.twitter.com/1.1/users/show.json?user_id='+str(id)
    response = requests.get(url, auth=oauth)

    #time.sleep(3)

    if response.status_code == 200:

        result = json.loads(response.content)
        #acct = '{} ({}, {})'.format(response['name'], response['screen_name'], response['id'])
        #print('     Looked up {} and resolved to {}'.format(id,result['screen_name']))
        return result['screen_name']
    print(response.status_code)
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


#
# MAIN
#

# create the graph object
graph = nx.DiGraph()

# Get friends (returns ID # in list) 
friends = get_all_friends_followers(username, 'friends')
print('[*] Retrieved {} friends for {}'.format(len(friends),username))


print('[*] Converting {} friend IDs to screen names'.format(username))
# Convert each friend ID to a screen_name
friend_names_list = []
for friend_id in friends:
    if friend_id is not None:
        f = id_lookup(friend_id)
        print(friend_id,f)
        #friend_names_list.extend(id_lookup(friend_id))
    else:
        continue

print('[*] Connecting {} friends to username'.format(username))
# Connect username to named friends
for friend in friend_names_list:
    graph.add_edge(username,friend)


# Get followers (returns ID # in list) 
followers = get_all_friends_followers(username, 'followers')
print('[*] Retrieved {} followers for {}'.format(len(followers),username))

print('[*] Converting {} follower IDs to screen names'.format(username))
# Convert each follower ID to a screen_name
follower_names_list = []
for follower_id in followers:
    if follower_id > 0:
        follower_names_list.extend(id_lookup(follower_id))
    else:
        continue


print('[*] Connecting {} followers to username'.format(username))
# Connect username to named followers
for follower in follower_names_list:
    graph.add_edge(follower,username)


# Write GEXF file
print('[*] Writing outfile')
nx.write_gexf(graph,"outfile.gexf")

print('[***] Finished')