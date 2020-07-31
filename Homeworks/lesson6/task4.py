# homework lesson: 6, task:4

"""
Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""


class Car:
    def __init__(self, color: str, name: str, speed: float = 0, is_police: bool = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Car is go')

    def stop(self):
        print('Car stopped')

    def turn(self, direction):
        if direction in ('left', 'right'):
            print(f'Car turn to {direction}')

    def show_speed(self):
        if not self.is_police and self.speed > 40:
            print(1)
        print(self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('ALARM')
        print(self.speed)


class SportCar(Car):
    pass


class WorkCar(Car):
    pass


class PoliceCar(Car):
    def __init__(self, color, name, is_sherif):
        self.is_sherif = is_sherif
        super().__init__(color, name, float('inf'), True)


temp = PoliceCar('red', 'Merthy', False)

print(1)
