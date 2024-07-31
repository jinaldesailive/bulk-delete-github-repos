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
    myresponse = requests.delete(os.path.join(url, repo), headers=headers)
    if myresponse.status_code == 204:
        print(f"Successfully deleted {repo}.")
    elif myresponse.status_code == 404:
        print(f"Repository {repo} not found.")
    else:
        print(f"Failed to delete {repo}: {myresponse.status_code} {myresponse.text}")
