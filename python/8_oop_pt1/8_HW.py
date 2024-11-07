from dataclasses import dataclass


class Zoo:

    def __init__(self):
        self._animals = []

    def add_animal(self, value):
        return self._animals.append(value)

    def remove_animal(self, value):
        return self._animals.remove(value)

    def __str__(self):
        return f"{self._animals}"


@dataclass
class Wolf:
    name: str
    id: int

    @staticmethod
    def play_sound():
        return 'Roar'

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


@dataclass
class Lion:
    name: str
    id: int

    @staticmethod
    def play_sound():
        print('Roar')

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


@dataclass
class Bison:
    name: str
    id: int

    @staticmethod
    def play_sound():
        print('Moo')

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


@dataclass
class Parrot:
    name: str
    id: int

    @staticmethod
    def play_sound():
        print('honk')

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


@dataclass
class Goose:
    name: str
    id: int

    @staticmethod
    def play_sound():
        print('honk')

    def __str__(self):
        return f'class {type(self).__name__} name {self.name} id {self.id}'


# test the class Zoo

oliva_zoo = Zoo()
gdansk_zoo = Zoo()

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.add_animal('tiger')

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.add_animal('lion')
gdansk_zoo.add_animal('cow')

print(oliva_zoo)
print(gdansk_zoo)

oliva_zoo.remove_animal('tiger')
print(oliva_zoo)
print(gdansk_zoo)

# test classes with animals

white_wolf = Wolf('Bone', 4535)
print(white_wolf)
print(white_wolf.play_sound())
