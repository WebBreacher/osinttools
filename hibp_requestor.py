#!/usr/bin/python3

# Written by Micah Hoffman
# For the SANS OSINT course SEC487
#
# Script to read email addresses from a file and
# look them up in HaveIBeenPwned.com using API

import requests
import sys
import time

# Disables SSL warning
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# If a command line argument was submitted, use it for email list
try:
    emailList = sys.argv[1]
except:
    print("! ERROR ! You need to specify a file name when calling the program")
    print("          For example: python3 hibp_requestor.py emails")
    exit(1)


# Read file specified on the command line
with open(emailList) as f:
    read_data = f.readlines()

# Cycle through the emails in the file and make a request to HIBP for each
# The email strings have a CRLF at end which we .strip() off
for email in read_data:
    # Check to see if the input has an "@" symbol. If not, skip it.
    if '@' not in email:
        continue
    url = 'https://haveibeenpwned.com/api/v2/breachedaccount/' + email.strip()
    headers = {'User-Agent': 'SANS SEC487 Checker'}
    r = requests.get(url, headers=headers, verify=False)
    print(email.strip())  
    
    # If the server sends a 200 response code then there is data
    if (r.status_code == 200):
        # Iterate through the list of the results and print the Name of the breach
        for site in r.json():
           print ('  !! Found in the breach: {0}, Breach Date: {1}'.format(site['Title'], site['BreachDate']))
    else:
        # Anything other than a response code of 200 and we assume no breach
        print('    Not breached')
    
    print ()
    # Per HIBP API rules, we need to rate limit > 1800ms
    time.sleep(2)
