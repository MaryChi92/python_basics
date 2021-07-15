class Road:
    _width = 0
    _length = 0

    def __init__(self, width, length, mass_cm, cm):
        Road._width = width
        Road._length = length
        self.mass_cm = mass_cm
        self.cm = cm

    def mass_asphalt(self):
        total_mass = Road._width * Road._length * self.mass_cm * self.cm
        print(f' {total_mass / 1000} т.')


a = Road(20, 5000, 25, 5)
a.mass_asphalt()
