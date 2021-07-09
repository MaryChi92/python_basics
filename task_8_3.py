def type_logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'\tcall {func.__name__}({", ".join(map(str, args))}: {type(*args)})')
        return result
    return wrapper


@type_logger
def calc_cube(x):
    return x ** 3


# @type_logger
# def calc_sum(*args):
#     return sum(args)


a = calc_cube(3)
print(a)

b = calc_cube(9.5)
print(b)

# c = calc_sum(1, 5, 7)
# print(c)
