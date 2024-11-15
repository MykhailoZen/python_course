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
from abc import ABC, abstractmethod


class Animal(ABC):

    def __init__(self, name: str, animal_id: int):
        self.animal_id = animal_id
        self.name = name

    def __str__(self):
        return f'Class: {self.__class__.__name__}, Name: {self.name}, ID: {self.animal_id}'

    def __eq__(self, other):
        if isinstance(other, Animal):
            return self.animal_id == other.animal_id
        return False

    @abstractmethod
    def play_sound(self):
        pass


class Predators(Animal):
    def play_sound(self):
        print("Roar")


class Biords(Animal):
    def play_sound(self):
        print("Honk")


class Wolf(Predators):
    def play_sound(self):
        super().play_sound()
        print("I will ate you!")


class Lion(Predators):
    pass


class Bioson(Animal):
    def play_sound(self):
        print("Moo")


class Parrtot(Biords):
    pass


class Goose(Biords):
    pass


class Zoo:

    def __init__(self):
        self._animals = []

    def adding_annimal(self, animal_to_add: Animal):
        self._animals.append(animal_to_add)
        return self

    def removing_annimal(self, animal_to_remove: Animal):
        self._animals.remove(animal_to_remove)
        return self

    def errase_annimal(self):
        self._animals.clear()
        return self

    @property
    def animals(self):
        return self._animals


if __name__ == '__main__':
    wolf = Wolf("Akello", 3)
    lion = Lion("Simba", 3)
    bioson = Bioson("Pumba", 4)
    parrtot = Parrtot("Iago", 6)
    goose = Goose("Martyn", 7)
    zoo = Zoo()
    zoo.adding_annimal(wolf).adding_annimal(lion).adding_annimal(bioson).adding_annimal(parrtot).adding_annimal(goose)
    for animal_zoo in zoo.animals:
        print(animal_zoo)
        animal_zoo.play_sound()
    print("--------------------")
    print(isinstance(wolf, Animal))
    print(isinstance(wolf, Predators))
    print(isinstance(wolf, Wolf))
    print(wolf == lion)
    print("--------------------")
    print(isinstance(zoo, Animal))
    print(wolf == zoo)
    print(wolf != goose)
