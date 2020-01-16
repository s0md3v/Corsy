import sys
import time

from core.requester import requester
from core.utils import host, load_json

details = load_json(sys.path[0] + '/db/details.json')

def passive_tests(url, headers):
    root = host(url)
    acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
    if acao_header == '*':
        info = details['wildcard value']
        info['acao header'] = acao_header
        info['acac header'] = acac_header
        return {url : info}
    if root:
        if host(acao_header) and root != host(acao_header):
            info = details['third party allowed']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}


def active_tests(url, root, scheme, header_dict, delay):
    headers = requester(url, scheme, header_dict, 'example.com')
    if headers:
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and acao_header == (scheme + 'example.com'):
            info = details['origin reflected']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        elif not acao_header:
            return
        time.sleep(delay)

        headers = requester(url, scheme, header_dict, root + '.example.com')
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and acao_header == (scheme + root + '.example.com'):
            info = details['post-domain wildcard']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        time.sleep(delay)

        headers = requester(url, scheme, header_dict, 'd3v' + root)
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and acao_header == (scheme + 'd3v' + root):
            info = details['pre-domain wildcard']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        time.sleep(delay)

        headers = requester(url, '', header_dict, 'null')
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and acao_header == 'null':
            info = details['null origin allowed']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        time.sleep(delay)

        headers = requester(url, scheme, header_dict, root + '%60.example.com')
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and '`.example.com' in acao_header:
            info = details['broken parser']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        time.sleep(delay)

        if root.count('.') > 1:
            spoofed_root = root.replace('.', 'x', 1)
            headers = requester(url, scheme, header_dict, spoofed_root)
            acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
            if acao_header and host(acao_header) == spoofed_root:
                info = details['unescaped regex']
                info['acao header'] = acao_header
                info['acac header'] = acac_header
                return {url : info}
            time.sleep(delay)
        headers = requester(url, 'http', header_dict, root)
        acao_header, acac_header = headers['access-control-allow-origin'], headers.get('access-control-allow-credentials', None)
        if acao_header and acao_header.startswith('http://'):
            info = details['http origin allowed']
            info['acao header'] = acao_header
            info['acac header'] = acac_header
            return {url : info}
        else:
            return passive_tests(url, headers)
