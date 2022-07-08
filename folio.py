import requests
import env


okapi_token = None
refresh_token = None


def okapi_headers():
    headers = {
        'Accept': 'application/json',
        'Accept-encoding': 'gzip, deflate, br',
        'Accept-language': 'en-US',
        'Content-type': 'application/json',
        'Origin': env.origin,
        'Referer': '%s/' % env.origin,
        'User-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.64 Safari/537.36',
        'X-okapi-tenant': env.tenant
    }

    global okapi_token
    if okapi_token is not None:
        headers['X-okapi-token'] = okapi_token

    return headers


def login():
    global okapi_url

    payload = {'tenant': env.tenant, 'username': env.username, 'password': env.password}
    print('Tenant %s: log in as %s/%s...' % (env.tenant, env.username, env.password))

    global okapi_url
    request = requests.post('%s/authn/login' % okapi_url, json=payload, headers=okapi_headers())

    status = request.status_code

    if status == 201:
        print('Logged in')
        global okapi_token, refresh_token
        okapi_token = request.json()['okapiToken']
        refresh_token = request.json()['refreshToken']
    else:
        print('Failed to log in')


def get(path):
    return requests.get('%s/%s' % (okapi_url, path), headers=okapi_headers())


def post(path, json):
    return requests.post('%s/%s' % (okapi_url, path), json=json, headers=okapi_headers())
