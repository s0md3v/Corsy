import urllib3
import requests
from core.colors import bad

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Added better error handling.
# Added verbose options.

def requester(url, scheme, headers, origin):
    headers['Origin'] = origin
    try:
        response = requests.get(url, headers=headers, verify=False)
        headers = response.headers
        for key, value in headers.items():
            if key.lower() == 'access-control-allow-origin':
                return headers
    except requests.exceptions.RequestException as e:
        if 'Failed to establish a new connection' in str(e):
            print ('%s %s is unreachable' % (bad, url))
        elif 'requests.exceptions.TooManyRedirects:' in str(e):
        	print ('%s %s has too many redirects' % (bad, url))
    return {}
