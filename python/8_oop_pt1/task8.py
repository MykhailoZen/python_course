from abc import ABC, abstractmethod


class Animals(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"

    @abstractmethod
    def play_sound(self):
        pass


class Zoo():
    def __init__(self):
        self._animals = []

    def add(self, element: Animals):
        self._animals.append(element)
        return self

    def remove(self, element: Animals):
        self._animals.remove(element)
        return self

    @property
    def animals(self):
        return self._animals


class Wolf(Animals):
    sound = "Roar"

    def play_sound(self):
        print(self.sound)


class Lion(Animals):
    sound = "Roar"

    def play_sound(self):
        print(self.sound)


class Bison(Animals):
    sound = "Moo"

    def play_sound(self):
        print(self.sound)


class Parrot(Animals):
    sound = "Honk"

    def play_sound(self):
        print(self.sound)


class Goose(Animals):
    sound = "Honk"

    def play_sound(self):
        print(self.sound)


if __name__ == '__main__':
    wolf = Wolf("Alex", 1)
    lion = Lion("Tom", 2)
    bison = Bison("Sarah", 3)
    parrot = Parrot("Patric", 4)
    goose = Goose("Chloe", 5)
    zoo = Zoo()
    zoo.add(wolf).add(lion).add(bison).add(parrot).add(goose)
    for x in zoo.animals:
        print(x)
