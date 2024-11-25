from functools import wraps


def strict(func):
    @wraps(func)
    def wrapped(a, b):
        if type(a) is func.__annotations__['a'] and type(b) is func.__annotations__['b']:
            return func(a, b)
        else:
            raise TypeError

    return wrapped


@strict
def sum_two(a: int, b: int) -> int:
    return a + b


# print(sum_two.__annotations__)
print(sum_two(1, 2))  # >>> 3
print(sum_two(1, 2.4))  # >>> TypeError
