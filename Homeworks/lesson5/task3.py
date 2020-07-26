"""Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. Определить,
кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины
дохода сотрудников.
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task3_file.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    text = file.read()

text = text.split('\n')
employees = []
salary = 0

print('Список сотрудников, имеющих оклад менее 20 тыс.:')
for line in text:
    values = line.split(' ')
    if int(values[1]) < 20000:
        employees.append(values[0])
        salary += int(values[1])
        print(values[0])
print(f'Средняя величина дохода сотрудников: {round(salary / len(employees)):,}')
