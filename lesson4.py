import sys

# from functools import reduce as native_reduce
# from math import (
#     pow,
#     hypot,
#     cos,
#     tan
# )
#
#
# import functools
# import time
import datetime as dt


#
#
# # native_reduce = reduce
#
#
# def reduce(func, data):
#     result = func(*data[:2])
#     for itm in data[2:]:
#         result = func(result, itm)
#     return result
#
#
# a = [2, 3, 4, 5]
#
# # functools.reduce(lambda x, y: x * y, a)
#
# start = time.time()
#
# for itm in a:
#     print(a)
#     time.sleep(1)
#
# end = time.time()
# print(end - start)
# dt.datetime.strftime()


def logger(func):
    def cloner(*args, **kwargs):
        date = dt.datetime.now()
        print(f'{date.strftime("%Y/%m/%d %H:%M")} - {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{func.__name__} DONE')
        return result

    return cloner


@logger
def one(a, b):
    return sum([a, b])


@logger
def two(a, b):
    return a * b


def my_cycle(data):
    idx = 0
    while True:
        yield data[idx]
        idx = idx + 1 if idx + 1 < len(data) else 0


# one = logger(one)

print(two.__name__)

# ask = {
#     'one': one,
#     'two': two,
# }
# print(sys.argv)
# _, funk_name, a, b, *__ = sys.argv
#
# print(ask[funk_name](int(a), int(b)))
