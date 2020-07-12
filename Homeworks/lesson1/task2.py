print('Добрый день! Вас приветствует программа по конвертации секунд в формат "чч:мм:сс".')

while True:
    try:
        n = abs(int(input("\033[0m{}".format('Пожалуйста, введите число секунд для преобразования: '))))
        sec_in_hour = 3600
        sec_in_min = 60
        hours = n // sec_in_hour
        minutes = (n - hours * sec_in_hour) // sec_in_min
        seconds = n - hours * sec_in_hour - minutes * sec_in_min
        print(n, 'секунд = '"{:0>2}:{:0>2}:{:0>2}".format(hours, minutes, seconds))
        break
    except ValueError:
        print("\033[31m{}".format('Произошла ошибка. Вы ввели значение, которое невозможно преобразовать в формат'
                                  ' "чч:мм:сс". Попробуйте еще раз.'))