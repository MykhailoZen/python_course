# Practice - coding:
# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g. output in print command should be like
# "class Lion name Alex id 2".
import uuid
from abc import ABC, abstractmethod


class Zoo:

    def __init__(self):
        self._animals = []

    def adding_annimal(self, animal_to_add):
        self._animals.append(animal_to_add)
        return self

    def removing_annimal(self, animal_to_remove):
        self._animals.remove(animal_to_remove)
        return self

    @property
    def animals(self):
        return self._animals


class Animal(ABC):

    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    @abstractmethod
    def play_sound(self):
        pass

    def __str__(self):
        return f"Class: {self.__class__.__name__}, Name: {self.name}, ID: {self.id}"


class Wolf(Animal):
    def play_sound(self):
        return "Roar"


class Lion(Animal):
    def play_sound(self):
        return "Roar"


class Bioson(Animal):
    def play_sound(self):
        return "Moo"


class Parrtot(Animal):
    def play_sound(self):
        return "Honk"


class Goose(Animal):
    def play_sound(self):
        return "Honk"


if __name__ == "__main__":
    wolf = Wolf("Akello")
    lion = Lion("Simba")
    bioson = Bioson("Pumba")
    parrtot = Parrtot("Iago")
    goose = Goose("Martyn")
    zoo = Zoo()
    zoo.adding_annimal(wolf).adding_annimal(lion).adding_annimal(bioson).adding_annimal(
        parrtot
    ).adding_annimal(goose)
    for animal_zoo in zoo.animals:
        print(f"{animal_zoo}, Sound: {animal_zoo.play_sound()}")
