import urllib3
import requests
from core.colors import bad

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Added better error handling.
# Added verbose options.

def requester(url, scheme, headers, origin):
    headers['Origin'] = scheme + origin
    try:
        response = requests.get(url, headers=headers, verify=False).headers
        for key, value in response.items():
            if key.lower() == 'access-control-allow-origin':
                return response
    except requests.exceptions.RequestException as e:
        if 'Failed to establish a new connection' in str(e):
            print ( ' ' + bad + ' ' + url + ' seems to be down')
