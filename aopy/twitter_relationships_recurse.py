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

    if response.status_code == 200:

        result = json.loads(response.content)

        return result

    return None


#
# Function that looks up a Twitter ID and returns Name (Screen_name)
#
def id_lookup(ids, next_cursor=None):
    counter = 0
    all_users = []
    
    while counter <= len(ids):
        params = ids[counter:counter+100]
        
        #join all the integer Twitter IDs
        all_params = ', '.join(str(param) for param in params)
        
        #strip all spaces from the string
        url = 'https://api.twitter.com/1.1/users/lookup.json?user_id=' + all_params.replace(' ','')
        response = requests.get(url, auth=oauth)

        if response.status_code == 200:
    
            results = json.loads(response.content)
            #acct = '{} ({}, {})'.format(response['name'], response['screen_name'], response['id'])
            #print('     Looked up {} and resolved to {}'.format(id,result['screen_name']))
            for result in results:
                all_users.extend([result['screen_name']])
        
        elif response.status_code == 429:
            print('!!! You are being rate-limited by Twitter: {}'.format(response.status_code))
    
        else:
            print('!!! Got non-200 HTTP response code: {}'.format(response.status_code))
    
        counter += 100

    return all_users

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
friend_names_list = id_lookup(friends)

print('[*] Connecting {} friends to username'.format(username))
# Connect username to named friends
for friend in friend_names_list:
    graph.add_edge(username,friend)


# Get followers (returns ID # in list) 
followers = get_all_friends_followers(username, 'followers')
print('[*] Retrieved {} followers for {}'.format(len(followers),username))

print('[*] Converting {} follower IDs to screen names'.format(username))
# Convert each follower ID to a screen_name
follower_names_list = id_lookup(followers)

print('[*] Connecting {} followers to username'.format(username))
# Connect username to named followers
for follower in follower_names_list:
    graph.add_edge(follower,username)


# Write GEXF file
print('[*] Writing outfile')
nx.write_gexf(graph,"outfile.gexf")

print('[***] Finished')