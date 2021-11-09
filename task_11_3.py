class NotNumError(Exception):
    def __init__(self, message="Remind you to enter numbers only"):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class UserData:
    num_list = []

    def __init__(self, user_data):
        self.user_data = user_data

    def creating_list(self):
        if not self.user_data.isdigit():
            raise NotNumError()
        else:
            UserData.num_list.append(self.user_data)

    def __str__(self):
        return f'{UserData.num_list}'


def run():
    while True:
        try:
            u_data = input('Enter any number or "stop": ')
            if u_data == 'stop':
                break
            else:
                UserData(u_data).creating_list()
        except NotNumError as e:
            print(e)
    print(UserData.num_list)


if __name__ == '__main__':
    run()
