"""Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

values = input('Введите числа через пробел: ')
sum_values = 0

with open('task5_file.txt', 'w', encoding='UTF-8') as file:
    file.write(values)

with open('task5_file.txt', 'r', encoding='UTF-8') as file:
    values = file.read().split(' ')
    for el in values:
        try:
            el = int(el)
            sum_values += el
        except ValueError:
            sum_values += 0
print(f'Сумма введенных чисел: {sum_values}')

"""Решение преподавателя

import os
import random

file_path = os.path.join(os.path.dirname(__file__), 'task5.txt')

to_file_numbers = [random.randint(1, 200) for _ in range(random.randint(10, 250))]
print(sum(to_file_numbers))

with open(file_path, 'w', encoding='UTF-8') as file:
    to_file_str = ' '.join(map(str, to_file_numbers))
    file.write(to_file_str)

with open(file_path, 'r', encoding='UTF-8') as file:
    numbers = map(int, file.read().split(' '))

print(sum(numbers))
print(sum(numbers))


# assert sum(to_file_numbers) == sum(numbers), 'Сработал ASSERT'
"""
