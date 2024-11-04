#Create a Python file with the next classes:
#1) Create the class "Zoo" with a protected list named "animals"
class Zoo:
    def __init__(self):
        self._animals = []

    # 2) Add methods for adding and removing elements from the list.
    def an_add(self, new_animal):
        self._animals.append(new_animal)

    def an_remove(self, animal):
        self._animals.remove(animal)

    def __repr__(self):
        return str(self._animals)

class Animal:
    def __init__(self, name, an_id):
        self._name = name
        self._an_id = an_id
    def __repr__(self):
        return f"Class {self.__class__.__name__} name {self._name} id {self._an_id}"


#3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
#Each class should have fields: name(str), id(int) and constructor.
#Each class should have the method "play_sound()" which returns the string with the sound of the animal (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
#Create method which represents the current class object as a string e.g. output in print command should be like "class Lion name Alex id 2".'''

class Wolf(Animal):
    def play_sound(self):
        return "Roar"

class Lion(Animal):
    def play_sound(self):
        return "Roar"

class Bioson(Animal):
    def play_sound(self):
        return "Moo"

class Goose(Animal):
    def play_sound(self):
        return "honk"

my_zoo = Zoo()
leo = Lion("Leo", 2)
goose = Goose("Geegee", 3)
wolfy = Wolf("Wolfy", 4)
my_zoo.an_add(leo)
my_zoo.an_add(goose)
my_zoo.an_add(wolfy)
print (my_zoo._animals)
my_zoo.an_remove(leo)
print (my_zoo._animals)

print(leo.play_sound())
print(goose)

