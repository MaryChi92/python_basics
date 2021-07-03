"""Наверно тут все можно было сделать просто через строки, но я увидела, что сущетвуют регулярные выражения, захотелось
опробовать их (хотя понимаю, что теряю адрес в формате IPv6). У меня выходил IndexError - не знала, как его избежать,
применила try-except. В общем, очень жду разбор дз)))"""

import re
REMOTE_ADDR_REGEX = '\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'

with open('nginx_logs.txt', 'r+') as f:
    logs_list = []
    while True:
        s = f.readline()
        remote_addr = re.search(REMOTE_ADDR_REGEX, s)
        try:
            a = s.split('"')[1]
            if remote_addr:
                b = a.split(' ')
                log_tuple = (remote_addr[0], b[0], b[1])
                logs_list.append(log_tuple)
        except IndexError:
            print('IndexError')
        if not s:
            break
    print(logs_list)
    