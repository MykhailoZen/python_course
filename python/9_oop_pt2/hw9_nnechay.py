# Create a Python file with the next classes:
# 1) Create the class "Zoo" with a protected list named "animals"
# 2) Add methods for adding and removing elements from the list.
# 3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
# Each class should have fields: name(str), id(int) and constructor.
# Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
# Create method which represents the current class object as a string e.g. output in print command should be like "class Lion name Alex id 2".

class Zoo:

    def __init__(self):
        self.animals = []

    def add_animal(self, include):
        """
        :param include: Element of the Animal class like Lion('<name>', id)
        :return:
        """
        return self.animals.append(include)

    def remove_animal(self, exclude):
        """
        :param include: Element of the Animal class like Lion('<name>', id)
        :return:
        """
        return self.animals.remove(exclude)

class Animal:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.__class__.__name__} {self.name}'

    def play_sound(self):
        pass

class Lion(Animal):
    def play_sound(self):
        return 'Roar'


class Wolf(Animal):
    def play_sound(self):
        return 'Roar'


class Bioson(Animal):
    def play_sound(self):
        return 'Moo'


class Goose(Animal):
    def play_sound(self):
        return 'Honk'

class Parrot(Animal):
    def play_sound(self):
        return 'Honk'


if __name__ == "__main__":

    my_animal_1 = Lion('Aaaa', 1)
    my_animal_2 = Bioson('Bbbb', 2)
    my_animal_3 = Wolf('Cccc', 3)
    my_animal_4 = Parrot('Dddd', 4)
    my_animal_5 = Goose('Eeee', 5)

    my_zoo = Zoo()
# Animals adding
    my_zoo.add_animal(my_animal_1)
    my_zoo.add_animal(my_animal_2)
    my_zoo.add_animal(my_animal_3)
    my_zoo.add_animal(my_animal_4)
    my_zoo.add_animal(my_animal_5)

    print('___Added animals___')
    for x in my_zoo.animals:
        print(f'{x} {x.name} with the "{x.id}" id says "{x.play_sound()}"')

    my_zoo.remove_animal(my_animal_4)
    my_zoo.remove_animal(my_animal_2)

    print('___Animals in my zoo after removing___')
    for x in my_zoo.animals:
        print(f'{x} {x.name} with the "{x.id}" id says "{x.play_sound()}"')
