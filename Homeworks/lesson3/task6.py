"""Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом. Каждое слово
состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с
заглавной буквы. Необходимо использовать написанную ранее функцию int_func().
"""


def int_func(text: str) -> str:
    """Функция, превращающая слово из маленьких латинских букв в слово с заглавной буквы.
    Работает только с 1 словом или с первым словом в предложении."""
    first_letter = text[0].upper()
    return first_letter + text[1:]


def int_func1(text: str) -> str:
    """Функция, превращающая слово или предложение, состоящее из маленьких латинских букв в слово или предложение,
    начинающееся с заглавной буквы."""
    result = text.title()
    return result


def int_func2(text: str) -> str:
    """Функция, превращающая слово или предложение, состоящее из маленьких латинских букв в слово или предложение,
    начинающееся с заглавной буквы."""
    text = text.split(' ')
    temp = []
    for el in text:
        word = el[0].upper() + el[1:]
        temp.append(word)
    text = ' '.join(temp)
    return text


print(int_func('my name is anastasia and i am learning python'))
print(int_func1('my name is anastasia and i am learning python'))
print(int_func2('my name is anastasia and i am learning python'))


"""Решение преподавателя

def int_func(string: str):
    return ''.join((string[0].upper(), string[1:])) if string else string


def user_temp(string: str):
    return ' '.join(map(int_func, string.split(' ')))


assert int_func('колбаса') == 'Колбаса', "int_func('колбаса')"
assert int_func('самса') == 'Самса', "int_func('самса')"
assert int_func('') == '', "int_func('')"

assert user_temp('колбаса с сыром') == 'Колбаса С Сыром', "user_temp('колбаса с сыром')"
assert user_temp('самса с ветчиной') == 'Самса С Ветчиной', "user_temp('самса с ветчиной')"
assert user_temp('') == '', "user_temp('')"
"""
