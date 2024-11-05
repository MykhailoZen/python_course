import uuid

'''-----------------------ZOO----------------------------'''
class Zoo:
    __animals = []

    def add_animals(self, animal):
        self.__animals.append(animal)

    def remove_animals(self, animal):
        self.__animals.remove(animal)

'''-----------------------WOLF----------------------------'''
class Wolf:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Roar'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

wolf = Wolf('Grey')
print(f'Wolf says {wolf.play_sound()}')
print(wolf)

'''-----------------------BISON----------------------------'''
class Bison:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Moo'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

bison = Bison('Byk')
print(f'Bison says {bison.play_sound()}')
print(bison)

'''-----------------------LION----------------------------'''
class Lion:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Roar'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

lion = Lion('Alex')
print(f'Lion says {lion.play_sound()}')
print(lion)


'''-----------------------PARROT----------------------------'''
class Parrot:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Honk'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

parrot = Parrot('Kesha')
print(f'Parrot says {parrot.play_sound()}')
print(parrot)

'''-----------------------GOOSE----------------------------'''
class Goose:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Honk'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

goose = Goose('Kesha')
print(f'Goose says {goose.play_sound()}')
print(goose)









