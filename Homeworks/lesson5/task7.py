"""Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.

Пример строки файла: firm_1 ООО 10000 5000.

Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.

Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).

Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].

Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import os
import json

file_path1 = os.path.join(os.path.dirname(__file__), 'task7_file.txt')
file_path2 = os.path.join(os.path.dirname(__file__), 'task7_file.json')

with open(file_path1, 'r', encoding='UTF-8') as file:
    profit_list = []
    profit_dict = {}
    loss_dict = {}
    for line in file:
        line = line.split()
        profit = int(line[2]) - int(line[3])
        if profit > 0:
            print(f'{line[0]} в прибыли на: {profit:,}')
            profit_list.append(profit)
            profit_dict[line[0]] = profit
        elif profit == 0:
            print(f'{line[0]} - нулевая прибыль.')
            loss_dict[line[0]] = profit
        else:
            print(f'{line[0]} в убытке на: {profit:,}')
            loss_dict[line[0]] = profit
    avg_profit = round(sum(profit_list) / len(profit_list), 1)
    print(f'Средняя прибыль по прибыльным компаниям: {avg_profit:,}')

fin_list = [profit_dict, {'avg_profit': avg_profit}, loss_dict]

with open(file_path2, 'w', encoding='UTF-8') as file:
    json.dump(fin_list, file)
