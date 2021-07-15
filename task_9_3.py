class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}


class Position(Worker):

    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(f'Сотрудник - {full_name}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'ЗП с учетом премии {total_income}')


staff_1 = Position('Kale', 'Williams', 'manager', 3000, '2000')
staff_1.get_full_name()
staff_1.get_total_income()
