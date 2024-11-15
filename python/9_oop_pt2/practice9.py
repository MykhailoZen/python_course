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


class Zoo:
    def __init__(self):
        self._animals_list = []

    def add_animal(self, animal_to_add):
        self._animals_list.append(animal_to_add)
        return self

    def remove_animal(self, animal_to_remove):
        self._animals_list.remove(animal_to_remove)
        return self

    @property
    def animals_list(self):
        return self._animals_list


class Animal(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return f"Class {self.__class__.__name__} with name {self.name} has id {self.id}"

    @abstractmethod
    def play_sound(self):
        pass


class Predators(Animal):
    def play_sound(self):
        print(f"{self.name} say 'Roar'")


class Birds(Animal):
    def play_sound(self):
        print(f"{self.name} say 'Honk'")


class Wolf(Predators):
    def play_sound(self):
        super().play_sound()
        print(f"{self.name}: I will eat you")


class Lion(Predators):
    pass


class Bioson(Animal):
    def play_sound(self):
        return f"{self.name} say 'Moo'"


class Parrot(Birds):
    pass


class Goose(Birds):
    pass


if __name__ == "__main__":
    wolf = Wolf("Boris", 13)
    lion = Lion("Simba", 14)
    bioson = Bioson("Vasja", 15)
    parrot = Parrot("Kesha", 16)
    goose = Goose("Koniec", 17)

    zoo = Zoo()
    zoo.add_animal(wolf).add_animal(lion).add_animal(bioson).add_animal(parrot).add_animal(goose)

    for animal_in_zoo in zoo.animals_list:
        print(animal_in_zoo)

    wolf.play_sound()