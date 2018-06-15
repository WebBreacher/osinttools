from twitter_keys import *

import json
import requests
import time


#account = 'jms_dot_py'
account = 817668451


#
# Main Twitter API function for sending requests
#
def send_request(url, next_cursor=None):

    response = requests.get(url, auth=oauth)

    time.sleep(3)

    if response.status_code == 200:

        result = json.loads(response.content)

        return result

    return None



#
# MAIN
#

if str(account).isdigit():
    url = 'https://api.twitter.com/1.1/users/show.json?user_id={}'.format(account)
else:
    url = 'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(account)

account_data = send_request(url)

print(account_data)
exit()

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


