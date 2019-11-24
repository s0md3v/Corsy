import tld
import json

def load_file(path):
    with open(path, 'r') as f:
        result = [line.rstrip('\n').encode('utf-8').decode('utf-8') for line in f]
    return '\n'.join(result)

def host(string):
	if string and '*' not in string:
		try:
			return tld.get_fld(string, fix_protocol=True)
		except:
			return False

def load_json(file):
	return json.loads(load_file('./db/details.json'))
