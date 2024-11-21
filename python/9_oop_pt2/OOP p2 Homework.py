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


class Fauna(ABC):
    def __init__(self, name: str, animalid: int, color: str):
        self.name = name
        self.animalid = animalid
        self.color = color

    def __str__(self):
        return (f'I am object of class {self.__class__.__name__}. My name is {self.name}, my id is {self.animalid} '
                f'and my color is {self.color}.')

    def __eq__(self, other):
        if isinstance(other, Fauna):
            return self.color == other.color
        return False

    def __lt__(self, other):
        if isinstance(other, Fauna):
            return self.animalid < other.animalid
        return False

    @abstractmethod
    def play_sound(self):
        pass


class Predator(Fauna):
    def play_sound(self):
        print('I am doing Roar')


class Bird(Fauna):
    def play_sound(self):
        print('I am doing Honk!')


class Cattle(Fauna):
    def play_sound(self):
        print('I am doing Moo!')


class Wolf(Predator):
    def play_sound(self):
        super().play_sound()
        print(f'I am strong and fierce!')


class Lion(Predator):
    pass


class Bison(Cattle):
    pass


class Parrot(Bird):
    pass


class Goose(Bird):
    pass


class Zoo:
    def __init__(self):
        self._animals_list = []

    def animals_adding(self, animal_for_adding: Fauna):
        self._animals_list.append(animal_for_adding)
        return self

    def animals_deleting(self, animals_for_deleting: Fauna):
        self._animals_list.append(animals_for_deleting)
        return self

    @property
    def animals_list(self):
        return self._animals_list


if __name__ == "__main__":
    wolf = Wolf("Peter", 1, "gray")
    lion = Lion("Jack", 2, "red")
    bizon = Bison("Lucy", 3, "black")
    parrot = Parrot("Zaza", 4, "green")
    goose = Goose("Colin", 5, "white")

    zoo = Zoo()
    zoo.animals_adding(wolf).animals_adding(lion).animals_adding(bizon).animals_adding(parrot).animals_adding(goose)

    for animal_in_zoo in zoo.animals_list:
        print(animal_in_zoo)

        animal_in_zoo.play_sound()

        print(isinstance(wolf, Wolf))
        print(isinstance(wolf, Predator))
        print(isinstance(wolf, Fauna))
        print(wolf == lion)
        print(bizon == goose)
        print(parrot != lion)
        print(wolf == Zoo)
        print(wolf < parrot)
        print(bizon < goose)
