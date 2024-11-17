# Practice - coding:
# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bison, Parrot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g.
# output in print command should be like "class Lion name Alex id 2".
from abc import ABC, abstractmethod


class Zoo:
    def __init__(self):
        self._animals_list = []

    @abstractmethod
    def animals_adding(self, animal_for_adding):
        self._animals_list.append(animal_for_adding)
        return self

    def animals_deleting(self, animals_for_deleting):
        self._animals_list.append(animals_for_deleting)
        return self

    @property
    def animals_list(self):
        return self._animals_list


class Fauna(ABC):
    def __init__(self, name, animalid):
        self.name = name
        self.animalid = animalid

    def __str__(self):
        return f'I am object of class {self.__class__.__name__}. My name is {self.name}, my id is {self.animalid}'

class Mammals(Fauna):
    def play_sound(self):
        return f'I am doing {self.play_sound}!'


class Birds(Fauna):
    def play_sound(self):
        return f'I am doing {self.play_sound}!'


class SoundRoar(Mammals):
    def my_sound(self):
        return f'I am doing {self.my_sound}!'

class SoundHonk(Birds):
    def my_sound(self):
        return f'I am doing {self.my_sound}!'

class SoundOther(Mammals, Birds):
    def my_sound(self):
        return f'I am doing {self.my_sound}!'

class Wolf(SoundRoar):
    def play_sound(self):
        return "Roar!"

class Lion(SoundRoar):
    def play_sound(self):
        return "Roar!"


class Bison(SoundOther):
    def play_sound(self):
        return "Moo!"


class Parrot(SoundHonk):
    def play_sound(self):
        return "Honk!"


class Goose(SoundHonk):
    def play_sound(self):
        return "Honk!"


if __name__ == "__main__":
    wolf = Wolf(name="Peter", animalid=1)
    lion = Lion(name="Jack", animalid=2)
    bizon = Bison(name="Lucy", animalid=3)
    parrot = Parrot(name="Zaza", animalid=4)
    goose = Goose(name="Colin", animalid=5)

    zoo = Zoo()
    zoo.animals_adding(wolf).animals_adding(lion).animals_adding(bizon).animals_adding(parrot).animals_adding(goose)

    for animal_in_zoo in zoo.animals_list:
        print(f"{animal_in_zoo}, I am doing {animal_in_zoo.play_sound()}")
