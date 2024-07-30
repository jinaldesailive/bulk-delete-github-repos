import os
import requests
import sys

organization = sys.argv[1] # or user
token = sys.argv[2] # token needs delete_repo permission

url = 'https://api.github.com/repos/{}'.format(organization)

headers = {'Accept': 'application/vnd.github.v3+json',
           'Authorization': 'token {}'.format(token)}


lines = [line.strip() for line in open('todelete.txt')] # todelete.txt is a txt with repository names. One per line.

for repo in lines:
    print(os.path.join(url, repo))
    myrequest = requests.delete(os.path.join(url, repo), headers=headers)
    print(myrequest.content)
