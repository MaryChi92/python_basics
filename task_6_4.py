"""Откуда у меня берется строка в конце? Я думала, что методом strip удаляю пробелы, переносы. Как избиваться от лишней строки?"""
with open("users.csv", 'r+', encoding='utf-8') as f_users, open("hobby.csv", 'r+', encoding='utf-8') as f_hobby:
    while True:
        user = f_users.readline().replace(',', ' ').strip()
        hobby = f_hobby.readline().replace(',', ', ').strip()
        user_hobby_str = f'{user}: {hobby}\n'
        with open('user_hobby.txt', 'a+', encoding='utf-8') as f_user_hobby:
            f_user_hobby.write(user_hobby_str)
        if not user and not hobby:
            break

with open('user_hobby.txt', 'r', encoding='utf-8') as f_user_hobby:
    print(f_user_hobby.read())
