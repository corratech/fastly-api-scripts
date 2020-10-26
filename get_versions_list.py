#!/usr/bin/env python3

from configparser import ConfigParser as cp
import ast
import json
import requests

fcfg = cp()
fcfg.read('config.ini')

api_url_base = fcfg.get('fastly','api_url')
api_token = fcfg.get('fastly','token')
fastly_service_id = fcfg.get('fastly','service_id')

headers = {'Fastly-Key': api_token,
           'User-Agent': 'Fastly-Client-007',
           'Accept': 'application/json',
           'Accept-Encoding': 'gzip, deflate, br'}

def get_response():

    api_url = '{0}service/{1}/version'.format(api_url_base,fastly_service_id)
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        return json.dumps(response.content.decode('utf-8'), indent=2)
    else:
        return None

print (ast.literal_eval(get_response()))