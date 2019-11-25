#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

from core.utils import load_file, load_json, host
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
parser.add_argument('-u', help='single url', dest='url')
parser.add_argument('-l', help='list with urls', dest='list')
parser.add_argument('-d', help='request delay', dest='delay', type=float, default=0)
args = parser.parse_args()

target_list = args.list
target_url = args.url
delay = args.delay

def cors(target):
	if target.startswith(('http://', 'https://')):
		parsed = urlparse(target)
		root = host(target)
		url = "%s://%s" % (parsed.scheme, parsed.netloc)
		result = active_tests(url, root, parsed.scheme, delay)

		if result:
			print('%s Misconfiguration found!' % good)
			print('%s URL: %s' % (info, target))
			print('%s Title: %s' % (info, result))
			print('%s Description: %s' % (info, details[result.lower()]['Description']))
			print('%s Severity: %s' % (info, details[result.lower()]['Severity']))
			print('%s Exploitation: %s\n' % (info, details[result.lower()]['Exploitation']))
		else:
			print('%s No misconfiguration found on %s.\n' % (bad, target))
	else:
		print('%s Please use https://%s not %s.\n' % (bad, target, target))

details = load_json('./db/details.json')

if target_url:
	cors(target_url)
elif target_list:
	for url in filter(None, load_file(target_list).split("\n")):
		cors(url)
else:
	print(parser.format_help().lower())
