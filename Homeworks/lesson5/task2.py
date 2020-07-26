"""Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

import os
from string import punctuation

file_path = os.path.join(os.path.dirname(__file__), 'task2_file.txt')

with open(file_path, 'r', encoding='UTF-8') as file:
    text = file.read()

text = text.split('\n')
print(f'Число строк в файле: {len(text)}')

for idx, lines in enumerate(text, 1):
    clean_lines = ''.join(el for el in list(lines) if el not in set(punctuation))
    words = clean_lines.split()
    print(f'Число слов в строке {idx}: {len(words)}')
