"""Для списка реализовать обмен значений соседних элементов, т.е. значениями обмениваются элементы с индексами 0 и 1,
2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения списка элементов
необходимо использовать функцию input().
"""

user_answer = list(input('Введите элементы для формирования списка: '))
print(f'Первоначальный список: {user_answer}')
i = 0
for el in user_answer:
    if i + 1 < len(user_answer):
        user_answer[i], user_answer[i + 1] = user_answer[i + 1], user_answer[i]
        i += 2
print(f'Измененный список: {user_answer}')

"""Решение преподавателя

user_answer = input('введите элементы черзе запятую')
user_list = user_answer.split(',')

idx = 0
while idx < len(user_list[:-1]):
    user_list[idx], user_list[idx + 1] = user_list[idx + 1], user_list[idx]
    idx += 2
print(user_list)
"""
