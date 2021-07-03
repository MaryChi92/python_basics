import re
from collections import Counter
REMOTE_ADDR_REGEX = '\d+\.\d+\.\d+\.\d+'

with open('nginx_logs.txt', 'r+') as f:
    logs_list = []
    while True:
        s = f.readline()
        remote_addr = re.search(REMOTE_ADDR_REGEX, s)
        if remote_addr:
            logs_list.append(remote_addr[0])
        if not s:
            break
    cnt = Counter(logs_list).most_common(1)
    print(cnt)
    