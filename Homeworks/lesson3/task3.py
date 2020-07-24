"""Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
аргументов.
"""


# Функция с использованием метода sort
def my_func2(v1: int, v2: int, v3: int) -> int:
    """Функция, принимающая 3 позиционных аргумента и считающая сумму двух наибольших аргументов."""
    init_list = [v1, v2, v3]
    init_list.sort(reverse=True)
    sum_v = init_list[0] + init_list[1]    # sum(sorted(init_list )[:2])
    return sum_v


# Функция с использованием функции min и sum
def my_func3(v1: int, v2: int, v3: int) -> int:
    """Функция, принимающая 3 позиционных аргумента и считающая сумму двух наибольших аргументов."""
    func_list = [v1, v2, v3]
    sum_v = sum(func_list) - min(func_list)
    return sum_v


# Функция с использованием альтернативы функции min и sum
def my_func4(v1: int, v2: int, v3: int) -> int:
    """Функция, принимающая 3 позиционных аргумента и считающая сумму двух наибольших аргументов."""
    func_list = [v1, v2, v3]
    i = 0
    min_v = func_list[i]
    while i < func_list.index(v3):
        if min_v > func_list[i + 1]:
            min_v = func_list[i + 1]
        i += 1
    sum_v = v1 + v2 + v3 - min_v
    return sum_v


# Самая костыльная функция
def my_func(v1: int, v2: int, v3: int) -> int:
    """Функция, принимающая 3 позиционных аргумента и считающая сумму двух наибольших аргументов."""
    if v1 > v2:
        if v2 > v3:
            sum_v = v1 + v2
        else:
            sum_v = v1 + v3
    elif v1 > v3:
        sum_v = v1 + v2
    else:
        sum_v = v2 + v3
    return sum_v


print(my_func2(23, 11, 48))
print(my_func2(124, 345, 11))
print(my_func2(5, 23, 45))

print(my_func3(23, 11, 48))
print(my_func3(124, 345, 11))
print(my_func3(5, 23, 45))

print(my_func4(23, 11, 48))
print(my_func4(124, 345, 11))
print(my_func4(5, 23, 45))

print(my_func(23, 11, 48))
print(my_func(124, 345, 11))
print(my_func(5, 23, 45))


"""Решение преподавателя

def my_func(a, b, c):
    return max(a + b, b + c, c + a)


# можно lambda
my_func2 = lambda a, b, c: max(a + b, b + c, c + a)

assert my_func(1, 2, 3) == 5, 'my_func(1, 2, 3)'
assert my_func(2, 7, 0) == 9, 'my_func(2, 7, 0)'
assert my_func(5, 9, 22) == 31, 'my_func(5, 9, 22)'
assert my_func(-22, 3, 7) == 10, 'my_func(-22, 3, 7)'

assert my_func2(1, 2, 3) == 5, 'my_func2(1, 2, 3)'
assert my_func2(2, 7, 0) == 9, 'my_func2(2, 7, 0)'
assert my_func2(5, 9, 22) == 31, 'my_func2(5, 9, 22)'
assert my_func2(-22, 3, 7) == 10, 'my_func2(-22, 3, 7)'
"""
