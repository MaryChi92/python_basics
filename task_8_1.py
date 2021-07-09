import re
RE_EMAIL_PARSER = re.compile(r'(?P<key>[^@]+)(?=@)@(?<=@)(?P<val>\S+\.[a-z]+)')


def email_parse(email_address):
    # print(*map(lambda x: x.groupdict(), RE_EMAIL_PARSER.finditer(i)), sep=', ')
    a = [*map(lambda x: x.groupdict(), RE_EMAIL_PARSER.finditer(i))]
    if not a:
        raise ValueError(f'wrong email: {email_address}')
    return a


if __name__ == '__main__':
    e = ['andrew@yandex.ru', '123@gmail.com', 'aaaaa']
    for i in e:
        print(email_parse(i))


# if __name__ == '__main__':
#     e = ['andrew@yandex.ru', '123@gmail.com', 'aaaaa']
#     try:
#         for i in e:
#             print(email_parse(i))
#     except ValueError:
#         print(f'wrong email')
