#!/usr/bin/env python3

from configparser import ConfigParser as cp
import os
import sys
import ast
import json
import requests

fcfg = cp()
fcfg.read('config.ini')

if "REQ_ACL_ID" in os.environ:
    pass
else:
    print("Terminating: ACL ID env var not-found")
    sys.exit()

api_url_base = fcfg.get('fastly','api_url')
api_token = fcfg.get('fastly','token')
fastly_service_id = fcfg.get('fastly','service_id')
acl_id = os.environ['REQ_ACL_ID']

headers = {'Fastly-Key': api_token,
           'User-Agent': 'Fastly-Client-007',
           'Accept': 'application/json',
           'Accept-Encoding': 'gzip, deflate, br'}

#curl --location --request GET 'https://api.fastly.com/service/6njAD9xbxLtzGC5gI7t3WW/acl/4kE9NXXQnOOzggo39RwAuV/entries'

def get_response():

    api_url = '{0}service/{1}/acl/{2}/entries'.format(api_url_base,fastly_service_id,acl_id)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.dumps(response.content.decode('utf-8'), indent=2)
    else:
        return None

print (ast.literal_eval(get_response()))