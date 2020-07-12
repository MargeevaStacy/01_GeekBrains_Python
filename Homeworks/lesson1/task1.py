a = 15
b = 35
c = a ** 2 + b
print(c)
c = b // a
print(c)
c = b % a
print(c)

amount = int(input('Введите сумму рублей для конвертации в доллары: '))
ex_rate = 65
dollars = round(amount / ex_rate, 2)
print(amount, 'рублей =', dollars, 'долларов')

height = int(input('Давайте рассчитаем ваш Индекс Массы тела.\nВведите ваш рост (см): '))
kgs = int(input('Введите ваш вес (кг): '))
result = kgs / ((height / 100) ** 2)
print(f'Индекс массы тела = {result:.1f}')

text = input('Введите текст для подсчета его длины: ')
result = len(text)
print(f'Длина текста: {result} символов')




