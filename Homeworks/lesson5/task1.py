"""Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об
окончании ввода данных свидетельствует пустая строка.
"""

while True:
    user_answer = input('Введите текст для записи в файл: ')
    if user_answer:
        with open('task1_file.txt', 'a', encoding='UTF-8') as file:
            file.write(f'{user_answer}\n')
    else:
        break


"""Решение преподавателя

import os
from pathlib import Path

file_path = os.path.join(os.path.dirname(__file__), 'task1.txt')

with open(file_path, 'w', encoding='UTF-8') as file:
    while True:
        user_data = input('введите данные\n')
        if not user_data:
            break
        file.write(f'{user_data}\n')
"""
