"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
пользователя, предусмотреть обработку ситуации деления на ноль.
"""


def num_division(num_1, num_2):
    """Функция принимает 2 числа и выполняет деление 1-го числа на 2-е."""
    result = num_1 / num_2
    return print(f'Результат деления {num_1} на {num_2}: {result:.1f}')


while True:
    try:
        user_num1 = float(input('Введите первое число: '))
        break
    except ValueError:
        print('Произошла ошибка. Пожалуйста, попробуйте еще раз.')

while True:
    try:
        user_num2 = float(input('Введите второе число: '))
    except ValueError:
        print('Произошла ошибка. Пожалуйста, попробуйте еще раз.')
    else:
        if user_num2 == 0:
            print('Деление на 0 невозможно. Введите другое число.')
        else:
            break

num_division(user_num1, user_num2)

"""Решение преподавателя

def division(a: float, b: float) -> float:
    "делит а на b
    :param a:
    :param b:
    :return: float or None"
    try:
        return a / b
    except ZeroDivisionError as e:
        print('Нельзя делить на ноль')


division2 = lambda a, b: a / b if b else None

assert division(4, 2) == 4, 'division(4, 2) SOME TEXT'
assert division(14, 2) == 7, 'division(14, 2)'
assert division(0, 2) == 0, 'division(0, 2)'
assert division(-22, 4) == -5.5, 'division(-22, 4)'
assert division(1, 0) is None, 'division(1, 0)'
"""
