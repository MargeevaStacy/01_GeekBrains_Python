"""Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""

import os

file_path1 = os.path.join(os.path.dirname(__file__), 'task4_file1.txt')
file_path2 = os.path.join(os.path.dirname(__file__), 'task4_file2.txt')

ru_values = ['Один', 'Два', 'Три', 'Четыре']
idx = 0

with open(file_path2, 'w', encoding='UTF-8') as file2:
    with open(file_path1, 'r', encoding='UTF-8') as file1:
        for line in file1:
            line = line.split()
            line[0], ru_values[idx] = ru_values[idx], line[0]
            idx += 1
            file2.write(f'{" ".join(line)}\n')
