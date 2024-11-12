from abc import abstractmethod
from dataclasses import dataclass


# Task 1:
class Zoo:

    def __init__(self, zoo):
        self._zoo = zoo
        self._animals = []

    @property
    def zoo(self):
        return self._zoo

    @zoo.setter
    def zoo(self, value):
        self._zoo = value

    def add_animal(self, value):
        return self._animals.append(value)

    def remove_animal(self, value):
        return self._animals.remove(value)

    def clear_animals(self):
        self._animals.clear()

    def __str__(self):
        return f"List of animals in {self._zoo} is {self._animals}"


# test Task 1:

oliva_zoo = Zoo('Oliva Zoo')
gdansk_zoo = Zoo('Gdansk Zoo')

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.zoo = 'New Oliva Zoo'
oliva_zoo.add_animal('tiger')

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.add_animal('lion')
gdansk_zoo.add_animal('cow')

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.remove_animal('tiger')
gdansk_zoo.clear_animals()

print(oliva_zoo)
print(gdansk_zoo)


# Task 2:

@dataclass
class Animals:
    name: str
    id: int

    @abstractmethod
    def play_sound(self):
        pass

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


class Wolf(Animals):
    def play_sound(self):
        print('Roar')


class Lion(Animals):
    def play_sound(self):
        print('Roar')


class Bison(Animals):
    def play_sound(self):
        print('Moo')


class Parrot(Animals):
    def play_sound(self):
        print('honk')


class Goose(Animals):
    def play_sound(self):
        print('honk')


# test Task 2:

white_wolf = Wolf('Bone', 4535)
black_parrot = Parrot('Ara', 696)

print()
print(white_wolf)
white_wolf.play_sound()

print(black_parrot)
black_parrot.play_sound()
