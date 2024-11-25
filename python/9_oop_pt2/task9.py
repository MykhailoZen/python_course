from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.hi_word: str = ""

    def __str__(self):
        return f"I'm from the class {self.__class__.__name__} my name is {self.name} id {self.id}"

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.hi_word == other.hi_word
        return False

    @abstractmethod
    def say_hello(self):
        print(f"I'm doing {self.hi_word}")


class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, element: Animal):
        self._animals.append(element)
        return self

    def remove(self, element: Animal):
        self._animals.remove(element)
        return self

    @property
    def animals(self):
        return self._animals


class Wolf(Animal):
    def say_hello(self):
        self.hi_word = "Roar"
        super().say_hello()


class Lion(Animal):
    def say_hello(self):
        self.hi_word = "Roar"
        super().say_hello()


class Bison(Animal):
    def say_hello(self):
        self.hi_word = "Moo"
        super().say_hello()


class Parrot(Animal):
    def say_hello(self):
        self.hi_word = "Honk"
        super().say_hello()


class Goose(Animal):
    def say_hello(self):
        self.hi_word = "Honk"
        super().say_hello()


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
        animal.say_hello()

    print(wolf == lion)
    print(lion == bison)
    print(parrot == goose)
