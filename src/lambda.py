import json
import requests
import os

url = 'https://test.com/api'

def generate_access_token():
    client_id = os.environ['client_id']
    client_secret = os.environ['client_secret']

    scope = f'api://{client_id}/.default'

    token_url = url + '/oauth2/token'

    d = {
        "client_id": client_id,
        "scope": scope,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }

    r = requests.post(token_url, data=d)

    return r.json()['access_token']

def launch_request():
    token = generate_access_token()

    request_url = url + "/v2/master/o9PreSalesTechnical2/Item"

    payload = ""
    headers = {
    'Authorization': f'Bearer {token}',
    }

    return requests.request("GET", request_url, headers=headers, data=payload)

def lambda_handler(event, context):
    response = launch_request()

    print(response.json())
    
    return {
        'statusCode': response.status_code,
        'body': response.json()
    }
