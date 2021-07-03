import json
from itertools import zip_longest

with open("users.csv", 'r+', encoding='utf-8') as f_users, open("hobby.csv", 'r+', encoding='utf-8') as f_hobby:
    our_dict = {}
    users_list = f_users.readlines()
    hobbies_list = f_hobby.readlines()
    if len(users_list) >= len(hobbies_list):
        our_dict = dict(zip_longest(users_list, hobbies_list[:len(users_list)]))
        with open('users_hobby.json', 'w', encoding='utf-8') as f_users_hobby:
            json.dump(our_dict, f_users_hobby)
    else:
        exit(1)

with open('users_hobby.json', 'r', encoding='utf-8') as f_users_hobby:
    our_dict = json.load(f_users_hobby)
    print(our_dict)