# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for
# wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g. output in print command should be like "class
# Lion name Alex id 2".
class Zoo:
    def __init__(self):
        self._animals = []

    def adding(self, animal):
        self._animals.append(animal)
        return self

    def removing(self, animal):
        self._animals.remove(animal)
        return self

    @property
    def animals(self):
        return self._animals


class Wolf:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal
    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'


class Lion:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'

class Bioson:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'

class Parrtot:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'

class Goose:
    def __init__(self, name: str, id_animal: int):
        self.name = name
        self.id_animal = id_animal

    def __str__(self):
        return f'class {self.__class__.__name__} name {self.name} id {self.id_animal}'

    def play_sound(self):
        return f'I {self.__class__.__name__} can say Roar!'

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
