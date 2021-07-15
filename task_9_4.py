class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        print(f'Машина {self.name} включила мигалки и поехала') if self.is_police is True else print(f'Машина {self.name} поехала')

    def stop(self):
        print(f'Машина {self.name} остановилась')

    def turn(self):
        direction = ''
        while direction != 'q':
            direction = input('Едем налево или направо? ')
            if direction == 'налево' or direction == 'направо':
                print(f'Машина повернула {direction}')
            elif direction == 'q':
                Car.stop(self)
                break
            else:
                direction = input('Ложное направление. Едем дальше налево или направо? ')

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч')


class TownCar(Car):
    max_allowed_speed = 60

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч') if 60 > self.speed > 0 else PoliceCar.fine(PoliceCar, self)


class SportCar(Car):
    pass


class WorkCar(Car):
    max_allowed_speed = 40

    def show_speed(self):
        print(f'Скорость машины {self.speed} км/ч') if 40 > self.speed > 0 else PoliceCar.fine(PoliceCar, self)


class PoliceCar(Car):

    def fine(self, other):
        print(f'Водитель {other.name}, за превышение скорости на {other.speed - other.max_allowed_speed} км/ч вам '
              f'выписан штраф!')


car_1 = TownCar('Ferrari', 'Red', 50)
car_1.show_speed()
car_2 = WorkCar('CAT', 'Yellow', 50)
car_2.show_speed()
car_3 = PoliceCar('Ford', 'White', 60, True)
car_3.go()
car_1.go()
car_1.turn()
