import os
import tld
import json
import tempfile


def host(string):
    if string and '*' not in string:
        return tld.get_fld(string, fix_protocol=True, fail_silently=True)


def load_json(file):
    with open(file) as f:
        return json.load(f)


def format_result(result):
    new_result = {}
    for each in result:
        if each:
            for i in each:
                new_result[i] = each[i]
    return new_result


def create_url_list(target_url, inp_file):
    urls = []
    if inp_file:
        with open(inp_file, 'r') as file:
            for line in file:
                if line.startswith(('http://', 'https://')):
                    urls.append(line.rstrip('\n'))
    if target_url and target_url.startswith(('http://', 'https://')):
        urls.append(target_url)
    return urls


def prompt(default=None):
    editor = 'nano'
    with tempfile.NamedTemporaryFile(mode='r+') as tmpfile:
        if default:
            tmpfile.write(default)
            tmpfile.flush()

        child_pid = os.fork()
        is_child = child_pid == 0

        if is_child:
            os.execvp(editor, [editor, tmpfile.name])
        else:
            os.waitpid(child_pid, 0)
            tmpfile.seek(0)
            return tmpfile.read().strip()


def extractHeaders(headers):
    headers = headers.replace('\\n', '\n')
    sorted_headers = {}
    matches = re.findall(r'^?(.*?):\s(.*?)[\n$]', headers)
    for match in matches:
        header = match[0]
        value = match[1]
        try:
            if value[-1] == ',':
                value = value[:-1]
            sorted_headers[header] = value
        except IndexError:
            pass
    return sorted_headers
