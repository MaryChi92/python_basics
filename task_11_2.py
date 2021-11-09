"""Полчаса выясняла, почему не работает код и выходит ошибка с текстом о том, что у класса - исключения нет атрибута
message. И потом увидела, что каким-то чудесным образом был не конструктор у меня, а def __int__ ...)))
И тут я представила, сколько можно убить времени на поиск ошибки в реальном проекте!"""


class ExceptionZeroDivision(Exception):
    def __init__(self, message="Can't divide by zero"):
        self.message = message

    def __str__(self):
        return f'{self.message}'


class Division:
    def __init__(self, dividend=input('Enter first number: '), divisor=input('Enter second number: ')):
        self.dividend = dividend
        self.divisor = divisor

    def division(self):
        try:
            if int(self.divisor) == 0:
                raise ExceptionZeroDivision()
            result = int(self.dividend) / int(self.divisor)
        except ExceptionZeroDivision as e:
            return e
        except ValueError:
            return 'You need to enter numbers'
        else:
            return result

    def __str__(self):
        return f'{self.division()}'


if __name__ == '__main__':
    example = Division()
    print(example)
