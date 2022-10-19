import json
from os import getenv
import requests

# {
#    "title":"Page 2",
#    "type":"page",
#    "body":{
#       "storage":{
#          "representation":"storage",
#          "value":"a sdas as s ad"
#       }
#    },
#    "Space":{
#       "key":"CSHR1"
#    },
#    "ancestors":[
#       {
#          "id":"1212418"
#       }
#    ]
# }
HEADERS = {
        # 'Authentication': f'Basic {tok}', 
        'Content-Type': 'application/json'
        }


def get_page(url, tok, id):
    auth=('admin', 'admin')
    resp = requests.get(url=f'{url}/{id}', headers=HEADERS, allow_redirects=True, auth=auth)
    return resp


def create_page(url, tok, ctype, key , parent, title , body):
    payload = {
        "title":title,
        "type": "page",
        "body":{
            "storage":{
                "representation":"storage",
                "value": body
            }
        },
        "space":{
            "key": key
        },
        "ancestors":[
            {
                "id": parent
            }
        ]
    }
    json_payload = json.dumps(payload)
    
    print(json_payload)
    auth=(getenv("ATLAS_LOCAL_USER"), getenv("ATLAS_LOCAL_PASS"))
    resp = requests.post(url=url, headers=HEADERS, data=json_payload, allow_redirects=True, auth=auth)
    return resp


def get_space(url, token, key):
    auth=(getenv("ATLAS_LOCAL_USER"), getenv("ATLAS_LOCAL_PASS"))
    resp = requests.get(url=f'{url}/rest/api/space/{key}', headers=HEADERS, allow_redirects=True, auth=auth)
    return resp


def create_space(url, token, key, title, description):
    payload = {
        "key": key,
        "name":title,
        "description": {
            "plain": {
                "value": description,
                "representation": "plain"
            }
        },
        # "metadata": {}
        
    }
    json_payload = json.dumps(payload)
    print(json_payload)
    auth=(getenv("ATLAS_LOCAL_USER"), getenv("ATLAS_LOCAL_PASS"))
    resp = requests.post(url=f'{url}/rest/api/space', headers=HEADERS, data=json_payload, allow_redirects=True, auth=auth)
    return resp
