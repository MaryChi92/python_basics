# from functools import wraps


def val_checker(my_argument):
    def _val_checker(func):
        # @wraps(func)
        def wrapper(*args):
            if my_argument(*args):
                result = func(*args)
                return result
            else:
                raise ValueError(f'wrong val {", ".join(map(str, args))}')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


a = calc_cube(5)
print(a)

b = calc_cube(-5)
print(b)
