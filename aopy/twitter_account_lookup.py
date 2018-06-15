'''
Script from Justin Seitz's https://learn.automatingosint.com/ Course
and Modified for Python 3 by Micah Hoffman
'''

from twitter_keys import *

import json
import requests
import time


account = 'webbreacher'
#account = 817668451


#
# Main Twitter API function for sending requests
#
def send_request(account, next_cursor=None):

    if str(account).isdigit():
        url = 'https://api.twitter.com/1.1/users/show.json?user_id={}'.format(account)
    else:
        url = 'https://api.twitter.com/1.1/users/show.json?screen_name={}'.format(account)
    
    response = requests.get(url, auth=oauth)

    time.sleep(3)

    if response.status_code == 200:

        result = json.loads(response.content)

        return result

    return None

#
# MAIN
#
account_data = send_request(account)

print('ID, Name, Screen Name')
print('{}, {}, {}'.format(account_data['id'], account_data['name'], account_data['screen_name']))
