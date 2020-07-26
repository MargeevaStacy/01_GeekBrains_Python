""" Необходимо создать (не программно) текстовый файл, где каждая строка описывает:
учебный предмет и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
Вывести словарь на экран.

Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""

import os

file_path = os.path.join(os.path.dirname(__file__), 'task6_file.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    text = file.read().split('\n')

courses_dict = {}
for lines in text:
    text = lines.split(': ')
    course = text[0]
    hours = text[1].replace('(', ' ').split()
    sum_hours = sum([int(el) for el in list(hours) if el.isdigit()])
    courses_dict[course] = sum_hours
print(courses_dict)
