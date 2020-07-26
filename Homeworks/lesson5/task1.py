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
