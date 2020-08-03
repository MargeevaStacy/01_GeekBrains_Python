"""Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.

К типам одежды в этом проекте относятся пальто и костюм.

У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).

Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.

Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Clothes:
    clothes_dict = {
        'total_materials': 0,
        'coat': 0,
        'suit': 0
    }

    def __init__(self, clothes_type):
        self.clothes_type = clothes_type

    def __str__(self):
        return f'{self.clothes_type}'


class Coat(Clothes):

    def __init__(self, v):
        super().__init__(clothes_type='coat')
        self.v = v
        Clothes.clothes_dict['total_materials'] += round(self.v / 6.5 + 0.5, 2)
        Clothes.clothes_dict[self.clothes_type] += round(self.v / 6.5 + 0.5, 2)

    @property
    def coat_materials(self):
        return round(self.v / 6.5 + 0.5, 2)


class Suit(Clothes):

    def __init__(self, h):
        super().__init__(clothes_type='suit')
        self.h = h
        Clothes.clothes_dict['total_materials'] += round(2 * self.h + 0.3, 2)
        Clothes.clothes_dict[self.clothes_type] += round(2 * self.h + 0.3, 2)

    @property
    def suit_materials(self):
        return round(2 * self.h + 0.3, 2)


cl1 = Coat(50)
print(cl1, cl1.coat_materials)

cl2 = Suit(15)
print(cl2, cl2.suit_materials)

print(Clothes.clothes_dict)

cl3 = Coat(50)
cl4 = Suit(15)
print(Clothes.clothes_dict)
