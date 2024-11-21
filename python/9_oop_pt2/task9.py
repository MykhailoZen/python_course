from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.hi_word: str = ""

    def __str__(self):
        return f"Class {self.__class__.__name__} name {self.name} id {self.id}"

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.hi_word == other.hi_word
        return False

    def say_hello(self):
        print(f"Hello I'm {self.name}")

    # @abstractmethod
    # def play_sound(self):
    #     pass


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
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.hi_word = "Roar"

    def say_hello(self):
        super().say_hello()
        print(self.hi_word)


class Lion(Animal):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.hi_word = "Roar"

    def say_hello(self):
        super().say_hello()
        print(self.hi_word)


class Bison(Animal):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.hi_word = "Moo"

    def say_hello(self):
        super().say_hello()
        print(self.hi_word)


class Parrot(Animal):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.hi_word = "Honk"

    def say_hello(self):
        super().say_hello()
        print(self.hi_word)


class Goose(Animal):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.hi_word = "Honk"

    def say_hello(self):
        super().say_hello()
        print(self.hi_word)


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

    wolf.say_hello()
    lion.say_hello()
    bison.say_hello()
    parrot.say_hello()
    goose.say_hello()

    print(wolf == lion)
    print(lion == bison)
    print(parrot == goose)
