"""Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

user_answer = input('Введите несколько слов через пробел: ').split(' ')
for ind, el in enumerate(user_answer, 1):
    if len(el) < 10:
        print(ind, el)
    else:
        print(ind, el[:10])

"""Решение преподавателя
user_words = input()
idxt = 0
for idx, word in enumerate(user_words.split(' ')):
    print(f'{idxt}:{word[:10]}')
    idxt += 1
"""
