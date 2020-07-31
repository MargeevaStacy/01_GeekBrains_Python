def my_sum(a: float, b: float, c: float = 22.0) -> float:
    """Функция суматор двух эллементов
    :param a: float
    :param b: float
    :return: float
    """
    result = a + b + c
    return a + b + c


def my_map(func, iter_obj):
    print(1)
    idx = 0
    for itm in iter_obj:
        print(2)
        yield func(itm)
        print(3)
        yield f'{idx}--{itm}'
        idx += 1
    print(4)



def my_zip(*args):
    result = []
    tmp = min(args, key=len)
    for idx, itm in enumerate(tmp):
        temp = []
        for item in args:
            temp.append(item[idx])
        result.append(tuple(temp))
    return result


def some_f(*args, **kwargs):
    print(type(kwargs))


for itm in my_map(lambda x: x ** 2, [11, 12, 13, 14]):
    print(itm)
my_sum(b=5, c=6, a=4)
