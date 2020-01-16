import urllib3
import requests

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip',
    'DNT': '1',
    'Connection': 'close',
}

def requester(url, scheme, origin):

    headers['Origin'] = scheme + origin
    response = requests.get(url, headers=headers, verify=False).headers
    return response.get('Access-Control-Allow-Origin', None)

