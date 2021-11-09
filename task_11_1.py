class Date:
    date = '21-07-2021'

    @classmethod
    def str_to_num(cls):
        day, month, year = list(map(int, cls.date.split('-')))
        return day, month, year

    @staticmethod
    def num_validation(day, month, year):
        return f'The date {day}-{month}-{year} is correct!' if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 2021 else print('The correct values for day are 01-31; for month 01-12; for year 1900-2021! Please, try again.')


print(Date.str_to_num(), '\n', Date.num_validation(21, 12, 2021))
