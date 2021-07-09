import re

PARSER_REGEX = '[ "\[\]-]+'

with open('nginx_logs.txt', 'r+') as f:
    while True:
        s = f.readline()
        parsed_list = re.split(PARSER_REGEX, s)
        print(parsed_list[:8])
        if not s:
            break
