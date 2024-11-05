import uuid

'''-----------------------ZOO----------------------------'''
class Zoo:
    __animals = []

    def add_animals(self, animal):
        self.__animals.append(animal)

    def remove_animals(self, animal):
        self.__animals.remove(animal)

    def get_animals(self):
        return self.__animals

'''-----------------------ANIMAL----------------------------'''
class Animal:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name

    def play_sound(self):
        return 'Animal sound'

    def __str__(self):
        return f'Class: {self.__class__.__name__}; Name: {self.name}; ID: {self.id}'

print('-----------------------WOLF----------------------------')
class Wolf(Animal):
    def play_sound(self):
        return 'Roar'

wolf = Wolf('Grey')
print(f'Wolf says {wolf.play_sound()}')
print(wolf)

print('-----------------------BISON----------------------------')
class Bison(Animal):
    def play_sound(self):
        return 'Moo'

bison = Bison('Byk')
print(f'Bison says {bison.play_sound()}')
print(bison)

print('-----------------------LION----------------------------')
class Lion(Animal):
    def play_sound(self):
        return 'Roar'

lion = Lion('Alex')
print(f'Lion says {lion.play_sound()}')
print(lion)


print('-----------------------PARROT----------------------------')
class Parrot(Animal):
    def play_sound(self):
        return 'Honk'

parrot = Parrot('Kesha')
print(f'Parrot says {parrot.play_sound()}')
print(parrot)

print('-----------------------GOOSE----------------------------')
class Goose(Animal):
    def play_sound(self):
        return 'Honk'

goose = Goose('Kesha')
print(f'Goose says {goose.play_sound()}')
print(goose)


print('------------------------Manage ZOO------------------------')
zoo = Zoo()
zoo.add_animals(wolf)
zoo.add_animals(lion)
zoo.add_animals(parrot)
zoo.add_animals(goose)
for animal in zoo.get_animals():
    print(animal)







