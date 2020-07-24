"""Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться сумма
чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь введенных
чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение
программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.
"""

sum_el = 0
stop_list = ['q', 'Q', 'й', 'Й']  # На случай, если пользователь работает на русской раскладке)
stop_marker = 0

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
user_answer = input('Введите числа через пробел: ').split(' ')

while True:
    for el in user_answer:
        if el in stop_list:
            stop_marker = 1
            break
        else:
            try:
                int_el = int(el)
                sum_el += int_el
            except ValueError:
                print('Не все данные, которые вы ввели, являются числами.')

    """При нажатии Enter должна выводиться сумма чисел.
    Сумма чисел будет подсчитана, даже если не все введенные элементы - это числа.
    Если вместо числа вводится специальный символ, сумма чисел до этого символа плюсуется к предыдущей сумме, 
    а выполнение программы завершается.
    """
    print(f'Сумма введенных чисел: {sum_el}.')

    if stop_marker == 1:
        break
    else:
        user_answer = input('\nДля выхода из программы введите "q", для продолжения - введите числа через пробел и '
                            'нажмите Enter: ').split(' ')
        if user_answer in stop_list:
            break


"""Решение преподавателя

def insert_sum(*args):
    result = 0
    exit_flag = False
    for itm in args:
        try:
            result += float(itm) if itm else 0
        except ValueError as e:
            if itm == 'q':
                exit_flag = not exit_flag
                break
    return result, exit_flag


user_sum = 0
while True:
    user_input = input('введите числа через пробел\n').split(' ')
    result_summ, user_exit = insert_sum(*user_input)
    user_sum += result_summ
    print(f'сумма: {user_sum}')

    if user_exit:
        print('Досвидания')
        break
"""
