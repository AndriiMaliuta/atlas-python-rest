import base64
from os import getenv
import requests
import services


if __name__ == '__main__':
    main_url = "http://localhost:7190"
    rest_url = "/rest/api/content"
    # token = base64.b64encode(b'admin:admin')
    token = getenv('ATLAS_LOCAL_TOKEN')
    
    for a in range(2, 16):
        resp = services.create_page(f'{main_url}{rest_url}', token, 'page', 'TEST3', '1572928', f'python page {a}', 'lorem asd asd das  d ds')
        print(resp.content)
