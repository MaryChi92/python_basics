def main(argv):
    program, file_1, file_2, file_3 = argv
    with open(file_1, 'a', encoding='utf-8') as f:
        users = ['Иванов,Иван,Иванович', 'Петров,Петр,Петрович', 'Федоров,Федор,Федорович', 'Дудь,Юрий,Александрович',
                 'Варламов,Илья,Александрович', 'Кац,Максим,Евгеньевич', 'Qwerty Qwe Q']
        for user in users:
            f.write(f'{user}\n')

    with open(file_2, 'a', encoding='utf-8') as f:
        hobbies = ['скалолазание,охота', 'горные лыжи', 'танцы', 'футбол',
                 'путешествия, урбанистика', 'покер']
        for hobby in hobbies:
            f.write(f'{hobby}\n')

    with open(file_1, 'r+', encoding='utf-8') as f_users, open(file_2, 'r+', encoding='utf-8') as f_hobby:
        while True:
            user = f_users.readline().replace(',', ' ').strip()
            hobby = f_hobby.readline().replace(',', ', ').strip()
            user_hobby_str = f'{user}: {hobby}\n'
            with open(file_3, 'a+', encoding='utf-8') as f_user_hobby:
                f_user_hobby.write(user_hobby_str)
            if not user and not hobby:
                break

    with open(file_3, 'r', encoding='utf-8') as f_user_hobby:
        print(f_user_hobby.read())


if __name__ == '__main__':
    import sys

    exit(main(sys.argv))
    