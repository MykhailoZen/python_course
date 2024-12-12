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
        return self.animals.append(include)

    def remove_animal(self, exclude):
        return self.animals.remove(exclude)

class Lion:

    def __init__(self,  kind, name, id):
        self.kind = kind
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.kind}'

    def play_sound(self):
        return 'Roar'


class Wolf:

    def __init__(self,  kind, name, id):
        self.kind = kind
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.kind}'

    def play_sound(self):
        return 'Roar'


class Bioson:

    def __init__(self,  kind, name, id):
        self.kind = kind
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.kind}'

    def play_sound(self):
        return 'Moo'


class Goose:

    def __init__(self,  kind, name, id):
        self.kind = kind
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.kind}'

    def play_sound(self):
        return 'Honk'

class Parrot:

    def __init__(self,  kind, name, id):
        self.kind = kind
        self.name = name
        self.id = id

    def __str__(self):
        return f'{self.kind}'

    def play_sound(self):
        return 'Honk'


if __name__ == "__main__":
    print('___Adding animals:___')
    my_animals = [('Lion', 'Aaaa', '1'), ('Parrot', 'Bbbbb', '2'),('Goose', 'Cccccc', '3'),('Bioson', 'Ddddd', '4'), ('Wolf', 'Eeeeeee', '5')]
    my_zoo = Zoo()
    animal_classes = {'Lion': Lion, 'Parrot': Parrot, 'Goose': Goose, 'Bioson': Bioson, 'Wolf': Wolf}
    for animal_kind, animal_nick, animal_id in my_animals:
        animal_class = animal_classes.get(animal_kind)
        if animal_class:
            animal = animal_class(animal_kind, animal_nick, animal_id)
            my_zoo.add_animal(animal)
            print(animal_kind, animal_nick, animal_id)

    print('___What does the Fox say? :)___')
    for x in my_zoo.animals:
        print(f'{x} {x.name} with the "{x.id}" id says "{x.play_sound()}"')
