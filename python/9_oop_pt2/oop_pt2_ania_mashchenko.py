# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the
# animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g.
# output in print command should be like "class Lion name Alex id 2".
from abc import ABC, abstractmethod

class Animals(ABC):
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __eq__(self, other):
        if isinstance(other, Animals):
            return self.name == other.name
        return False

    def __str__(self):
        return f"I am an animal of class {self.__class__.__name__} and my name is {self.name} and my id is {self.id}"

    @abstractmethod
    def play_sound(self):
        pass


class Birds(Animals):
    def play_sound(self):
        print("Honk!")

class Predator(Animals):
    def play_sound(self):
        print("Roar")

class Bison(Animals):
    def play_sound(self):
        print("Moo!")

class Wolf(Predator):
    pass

class Lion(Predator):
    def play_sound(self):
        super().play_sound()
        print("I'm the king of animals")

class Goose(Birds):
    pass

class Parrot(Birds):
    pass

class Zoo:
    def __init__(self):
        self._animals_list = []

    def animals_adding(self, animals_for_adding: Animals):
        self._animals_list.append(animals_for_adding)
        return self

    def animals_removing(self, animals_for_removing: Animals):
        self._animals_list.remove(animals_for_removing)
        return self

    @property
    def animals_list(self):
        return self._animals_list


if __name__ == "__main__":
    lion = Lion("King",5)
    wolf = Wolf("Tom", 7)
    parrot = Parrot("Dan", 8)
    goose = Goose("Harry", 4)
    bison = Bison("Jack", 52)

    zoo = Zoo()
    zoo.animals_adding(lion).animals_adding(parrot).animals_adding(wolf).animals_adding(goose).animals_adding(bison)

    for animal_in_zoo in zoo.animals_list:
        print(animal_in_zoo)

    print(parrot)

    lion.play_sound()
    bison.play_sound()
    parrot.play_sound()

    print(lion != wolf)







