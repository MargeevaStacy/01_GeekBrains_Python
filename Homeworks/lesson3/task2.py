"""Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя: имя, фамилия,
год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""

# Вариант 1


def user_profile(**kwargs):
    return print(kwargs)


questions = {
    'Имя': ('Введите имя: ', str),
    'Фамилия': ('Введите фамилию: ', str),
    'Год рождения': ('Введите год рождения: ', int),
    'Город проживания': ('Введите город проживания: ', str),
    'Email': ('Введите email: ', str),
    'Телефон': ('Введите телефон: ', int)
}

user_data = {}
for key, value in questions.items():
    while True:
        user_answer = input(f'{value[0]}\n')
        try:
            user_answer = value[1](user_answer)
        except ValueError as e:
            print(f'{e}\nПовторите ввод данных.')
            continue
        user_data[key] = user_answer
        break

user_profile(**user_data)


# Вариант 2


def user_profile1(name, surname, birth_year, city, email, phone):
    return print(f'Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город проживания: {city}, Email: {email}, Телефон: {phone}')


u_name = input('Введите имя: ')
u_surname = input('Введите фамилию: ')
while True:
    u_birth_year = input('Введите год рождения: ')
    if u_birth_year.isdigit():
        u_birth_year = int(u_birth_year)
        break
    print('Произошла ошибка. Введите год рождения числом.')
u_city = input('Введите город проживания: ')
u_email = input('Введите email: ')
u_phone = input('Введите телефон: ')

user_profile1(name=u_name, surname=u_surname, birth_year=u_birth_year, city=u_city, email=u_email, phone=u_phone)

"""Решение преподавателя

def user_data(name: str,
              surname: str,
              birth_year: int,
              city: str,
              email: str,
              phone: int
              ):
    "
    Отображает данные о пользователе на экране
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: None
    "
    return f"{name} {surname} {birth_year} года рождения, " \
           f"в городе {city}. Контакты: {email}, {phone} "


def user_data_kw(**kwargs) -> str:
    "
    Отображает данные о пользователе на экране
    :param name: str
    :param surname: str
    :param birth_year: int
    :param city: str
    :param email: str
    :param phone: int
    :return: str
    "

    name = kwargs.get('name', '')
    surname = kwargs.get('surname', '')
    birth_year = kwargs.get('birth_year', '')
    city = kwargs.get('city', '')
    email = kwargs.get('email', '')
    phone = kwargs.get('phone', '')

    return f"{name} {surname} {birth_year} года рождения, в городе {city}. Контакты: {email}, {phone} "
"""
