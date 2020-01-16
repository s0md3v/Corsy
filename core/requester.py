import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def requester(url, scheme, headers, origin):
    headers['Origin'] = scheme + origin
    response = requests.get(url, headers=headers, verify=False).headers
    for key, value in response.items():
        if key.lower() == 'access-control-allow-origin':
            return response
