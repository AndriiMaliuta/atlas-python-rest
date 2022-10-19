from datetime import datetime
from os import getenv
from confl import services

if __name__ == '__main__':
    start = datetime.now()
    main_url = "http://localhost:7190"
    rest_url = "/rest/api/content"
    URL = f'{main_url}{rest_url}'
    # token = base64.b64encode(b'admin:admin')
    token = getenv('ATLAS_LOCAL_TOKEN')

    # resp = services.get_page(URL, token, 1572930)

    for a in range(1, 100):
        resp = services.create_page(URL, token, 'page', 'PY1', '1900549', f'python page {a}', 'lorem asd asd das  d ds')
        print(resp.content)

    # resp = services.create_space(main_url, token, "PY1", "PY1", "")
    print(resp.content)

    print(datetime.now() - start)