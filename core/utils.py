import tld
import json


def host(string):
    if string and '*' not in string:
        return tld.get_fld(string, fix_protocol=True, fail_silently=True)

def load_json(file):
    with open(file) as f:
        return json.load(f)
