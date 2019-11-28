#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from core.utils import load_json, host
from core.tests import active_tests
from core.colors import white, green, info, bad, good, grey, end

try:
	from urllib.parse import urlparse
except ImportError:
	from urlparse import urlparse

print('''
    %sＣＯＲＳＹ  %s{%sv0.2-beta%s}%s
''' % (green, white, grey, white, end))

parser = argparse.ArgumentParser()
parser.add_argument('-u', help='target url', dest='url')
parser.add_argument('-d', help='request delay', dest='delay', type=float, default=0)
parser.add_argument('-k', help='Allow insecure server connections when using SSL', dest='insecure', action='store_true')
args = parser.parse_args()

target_url = args.url
delay = args.delay
insecure = args.insecure

def cors(target, delay, scheme=False):
	url = target
	if not target.startswith(('http://', 'https://')):
		url = scheme + '://' + url
	root = host(url)
	parsed = urlparse(url)
	netloc = parsed.netloc
	scheme = parsed.scheme
	url = scheme + '://' + netloc
	active = active_tests(url, root, scheme, delay, insecure)
	return active

details = load_json('./db/details.json')

if target_url:
	if target_url.startswith(('http://', 'https://')):
		result = cors(target_url, delay)
		if result:
			print('%s Misconfiguration found!' % good)
			print('%s Title: %s' % (info, result))
			print('%s Description: %s' % (info, details[result.lower()]['Description']))
			print('%s Severity: %s' % (info, details[result.lower()]['Severity']))
			print('%s Exploitation: %s' % (info, details[result.lower()]['Exploitation']))
		else:
			print('%s No misconfiguration found.' % bad)
	else:
		print('%s Please use https://example.com not example.com' % bad)
else:
	print('\n' + parser.format_help().lower())
