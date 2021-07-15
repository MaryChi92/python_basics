class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки: {self.title}')


a_1 = Pen('ручка')
a_1.draw()
a_2 = Pencil('карандаш')
a_2.draw()
a_3 = Handle('маркер')
a_3.draw()
