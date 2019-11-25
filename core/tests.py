import time

from core.utils import host
from core.requester import requester

def passive_tests(url, acao_header):
	root = host(url)
	if acao_header == '*':
		return 'Wildcard value'
	if root:
		if root != host(acao_header):
			print(acao_header)
			return 'Third party allowed'
		elif url.startswith('http://'):
			return 'HTTP origin allowed'
		else:
			return False
	else:
		return 'Invalid value'

def active_tests(url, root, scheme, delay):
	acao_header = requester(url, scheme, 'example.com')
	if acao_header:
		if acao_header == (scheme + 'example.com'):
			return 'Origin reflected'
	time.sleep(delay)
	acao_header = requester(url, scheme, root + '.example.com')
	if acao_header:
		if acao_header == (scheme + root + '.example.com'):
			return 'Post-domain wildcard'
	time.sleep(delay)
	acao_header = requester(url, scheme, 'd3v' + root)
	if acao_header:
		if acao_header == (scheme + 'd3v' + root):
			return 'Pre-domain wildcard'
	time.sleep(delay)
	acao_header = requester(url, '', 'null')
	if acao_header:
		if acao_header == 'null':
			return 'Null origin allowed'
	time.sleep(delay)
	acao_header = requester(url, scheme, root + '%60.example.com')
	if acao_header:
		if '`.example.com' in acao_header:
			return 'Broken parser'
	if root.count('.') > 1:
		time.sleep(delay)
		spoofed_root = root.replace('.', 'x', 1)
		acao_header = requester(url, scheme, spoofed_root)
		if acao_header:
			if host(acao_header) == spoofed_root:
				return 'Unescaped regex'
		time.sleep(delay)
	acao_header = requester(url, 'http', root)
	if acao_header:
		if acao_header.startswith('http://'):
			return 'HTTP origin allowed'
		else:
			return passive_tests(url, acao_header)
