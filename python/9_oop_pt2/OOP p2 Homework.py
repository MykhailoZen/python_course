# Practice - coding:
# Write a function that takes a list of numbers as input and returns a new list containing the square of each number using
# the functional approach.
# Write a function that takes a list of numbers as input and returns a new list containing only the even numbers.
# Write a function that calculates the factorial of a number using the functional approach.
# Capitalize the first letter of each word in a sentence "hello world, how are you?".
# Given a list of students and their marks as tuples:
# scores = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
# Write a function that calculates the average score of the students in the list. The function should take the list of tuples as input and return the average score.
from abc import ABC, abstractmethod


class Zoo:
    def __init__(self):
        self._animals_list = []

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

    @abstractmethod
    def play_sound(self):
        pass


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
    wolf = Wolf("Peter", 1)
    lion = Lion("Jack", 2)
    bizon = Bison("Lucy", 3)
    parrot = Parrot("Zaza", 4)
    goose = Goose("Colin", 5)

    zoo = Zoo()
    zoo.animals_adding(wolf).animals_adding(lion).animals_adding(bizon).animals_adding(parrot).animals_adding(goose)

    for animal_in_zoo in zoo.animals_list:
        print(f"{animal_in_zoo}, I am doing {animal_in_zoo.play_sound()}")
