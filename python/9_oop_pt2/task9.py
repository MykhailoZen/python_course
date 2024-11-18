from abc import ABC, abstractmethod

class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, element):
        self._animals.append(element)
        return self

    def remove(self, element):
        self._animals.remove(element)
        return self

    @property
    def animals(self):
        return self._animals

class Animal(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Class {self.__class__.__name__} name {self.name} id {self.id}"

    @abstractmethod
    def play_sound(self):
        pass

class Wolf(Animal):
    def play_sound(self):
        return "Roar"

class Lion(Animal):
    def play_sound(self):
        return "Roar"

class Bison(Animal):
    def play_sound(self):
        return "Moo"

class Parrot(Animal):
    def play_sound(self):
        return "Honk"

class Goose(Animal):
    def play_sound(self):
        return "Honk"

if __name__ == '__main__':
    wolf = Wolf("Alex", 1)
    lion = Lion("Tom", 2)
    bison = Bison("Sarah", 3)
    parrot = Parrot("Patric", 4)
    goose = Goose("Chloe", 5)

    zoo = Zoo()
    zoo.add(wolf).add(lion).add(bison).add(parrot).add(goose)
    for animal in zoo.animals:
        print(animal)