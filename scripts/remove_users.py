"""
    Request deletion of users via command line
"""

__author__ = "Filipe Rocha"
__date__ = "2021-12-13"
__version__ = "1.0.0"
__email__ = "filipe.fsrocha@gmail.com"

import requests
import json
import sys
import argparse
import json

argv = sys.argv[1:]

if not argv:
    print("Usage: Options and arguments [-h] -burl  -tk  [-sz] [-blocked] [-ssl]")
    sys.exit(2)

parser = argparse.ArgumentParser('Options and arguments')
parser.add_argument('-burl', '--baseurl', required=True, metavar='', help='API base url')
parser.add_argument('-tk', '--token', required=True, metavar='', help='Authorization token')
parser.add_argument('-sz', '--size', metavar='', help='Total records to be processed')
parser.add_argument('-blocked', metavar='', help='Include blocked users, default value True')
parser.add_argument('-ssl', metavar='', help='Enable ssl, default value False')

args = vars(parser.parse_args())

# Create headers
headers = {
    'Authorization': 'bearer {0}'.format(args['token']),
    'Content-Type': 'application/json'
}

# Create payload
limit = args['size'] if args['size'] else 1000
include_blocked = args['blocked'] if args['blocked'] else True
enabled_ssl = args['ssl'] if args['ssl'] else False

payload = {
    'pagination': {
        'pageNumber': 0,
        'pageSize': limit
    },
    'includeBlocked': include_blocked
}

print('Requested deletion process')

delete_users = []

req = requests.post('{0}/platform/user/queries/listUsers'.format(args['baseurl']), data=json.dumps(payload), headers=headers, verify=enabled_ssl)
results = req.json()

for user in results['users']:
    if user['username'] != 'admin':
        print('User added for deletion: {0}'.format(user['username']))
        delete_users.append(user['username'])

try:
    requests.post('{0}/platform/user/signals/deleteUsers'.format(args['baseurl']), data=json.dumps({ 'usernames': delete_users }), headers=headers, verify=enabled_ssl)
    print('Requested deletion process, you will receive a notification on the platform at the end of the process!')
    print('Total users sent for deletion: {}'.format(len(delete_users)))
    delete_users.clear()
except Exception as e:
    print('An error occcurred when requesting to delete: {0}'.format(e))

print('Finalized deletion process')