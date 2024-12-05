# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for
# wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g. output in print command should be like "class
# Lion name Alex id 2".

# Practice
# Refactor your previous homework in an OOP way.
from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.id_animal == other.id_animal
        return False

    @abstractmethod
    def play_sound(self):
        pass


class Predator(Animal):
    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'


class Bird(Animal):
    def play_sound(self):
        return f'I {self.__class__.__name__} can say honk!'

    def warning_sound(self):
        print(f'I {self.__class__.__name__} worn you!')


class Wolf(Predator):
    pass


class Lion(Predator):
    pass


class Bioson(Animal):
    def play_sound(self):
        return f'I {self.__class__.__name__} can say Moo!'


class Parrtot(Bird):
    def warning_sound(self):
        super().warning_sound()
        print(f"I am Parrot")


class Goose(Bird):
    pass


class Zoo:
    def __init__(self):
        self._animals = []

    def adding(self, animal: Animal):
        self._animals.append(animal)
        return self

    def removing(self, animal: Animal):
        self._animals.remove(animal)
        return self

    @property
    def animals(self):
        return self._animals


if __name__ == '__main__':
    lion = Lion("Simba", 1)
    wolf = Wolf("Wolf1", 2)
    bioson = Bioson("Bioson1", 3)
    parrtot = Parrtot("Parrtot1", 4)
    goose = Goose("Goose1", 1)
    zoo = Zoo()
    zoo.adding(lion).adding(wolf).adding(bioson).adding(parrtot).adding(goose)
    for x in zoo.animals:
        print(x)
    print(lion == goose)
    print(f"----")
    parrtot.warning_sound()
