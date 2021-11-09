class ComplexNumber:
    def __init__(self, real_number, imaginary_number):
        self.real_number = int(real_number)
        self.imaginary_number = int(imaginary_number)

    def __add__(self, other):
        result = f'{self.real_number + other.real_number} + {self.imaginary_number + other.imaginary_number}i'
        return result

    def __mul__(self, other):
        result = f'{self.real_number * other.real_number - self.imaginary_number * other.imaginary_number} + {self.real_number * other.imaginary_number + self.imaginary_number * other.real_number}i'
        return result


if __name__ == '__main__':
    complex_number_1 = ComplexNumber(5, 3)
    complex_number_2 = ComplexNumber(6, 9)
    add_res = complex_number_1 + complex_number_2
    mul_res = complex_number_1 * complex_number_2
    print(add_res, '\n', mul_res, sep='')
