import json
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
    HEADERS = {
        # 'Authentication': f'Basic {tok}', 
        'Content-Type': 'application/json'
        }
    print(json_payload)
    auth=('admin', 'admin')
    resp = requests.post(url=url, headers=HEADERS, data=json_payload, allow_redirects=True, auth=auth)
    return resp

