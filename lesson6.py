import random


class Animal:
    __population = []

    def __init__(self, animal_type, mass, is_herbivorous, habitat, say_str):
        """
        :param animal_type:
        :param mass:
        :param is_herbivorous:
        :param habitat:
        :param say_str:
        """

        self.animal_type = animal_type
        self.mass = mass
        self.is_herbivorous = is_herbivorous
        self.habitat = habitat
        self.say_str = say_str
        Animal.__population.append(self)

    def say(self):
        print(self.say_str)

    def breeding(self, any_obj):
        if isinstance(any_obj, Animal) and any_obj.habitat == self.habitat:
            result = Animal(self.animal_type,
                            any_obj.mass,
                            self.is_herbivorous,
                            any_obj.habitat,
                            f'{self.say_str}-{any_obj.say_str}'
                            )
            return result
        else:
            raise TypeError('Неможно размножать это')

    def population(self):
        return self.__population[:]


class Human(Animal):
    __names = [
        'Саша',
        'Женя',
        'Валя'
    ]

    def __init__(self, name, sex, surname, mass):
        self.name = name
        self.surname = surname
        self.sex = sex
        super().__init__('Homo', mass, False, 'City', f'Hello')

    def breeding(self, any_obj):
        if isinstance(any_obj, type(self)) and self.sex != any_obj.sex:
            result = Human(random.choice(self.__names), self.surname, random.choice(('M', 'F')), 3.6)
            return result
        else:
            raise TypeError('Неможно размножать это')

    def say(self):
        super().say()
        print(f'Меня зовут {self.name}')


dolphin = Animal('Mammal', 65, False, 'Sea', 'Iaiakiki')
dog = Animal('Mammal', 25, False, 'Home', 'wof-wof')
horse = Animal('Mammal', 200, True, 'Prairie', 'frrrrrr')
rabbit = Animal('Mammal', 2, True, 'Home', 'CCCCCHrumHrum')

homo1 = Human('Vasya', 'M', 'Ivanov', 76)
homo2 = Human('Anna', 'F', 'Karenina', 55)
print(1)
