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
