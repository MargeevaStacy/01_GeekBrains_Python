print('Добрый день! Вас приветствует программа, которая поможет определить финансовый результат вашей фирмы.')

revenue = int(input('Пожалуйста, введите размер выручки: '))
costs = int(input('Пожалуйста, введите размер издержек: '))
profit = revenue - costs
if revenue > costs:
    profitability = round(profit / revenue, 2)
    print(f'Поздравляем, ваше предприятие прибыльно!\nРазмер выручки составляет: {profit:,}'
          f'\nРентабельность выручки: {profitability:,}')
    employees = int(input('Пожалуйста, введите число сотрудников, работающих в вашей фирме: '))
    profit_per_employee = round(profit / employees, 2)
    print(f'Прибыль на 1 сотрудника составляет: {profit_per_employee:,}')
else:
    print(f'К сожалению, ваше предприятие убыточно. Размер убытка: {profit:,}')
