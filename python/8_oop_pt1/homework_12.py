#Create a Python file with the next classes:
#1) Create the class "Zoo" with a protected list named "animals"
#2) Add methods for adding and removing elements from the list.
#3) Create classes for Wolf, Lion, Bioson, Parrtot, and Goose
#a) Each class should have fields: name(str), id(int) and constructor.
#b) Each class should have the method "play_sound()" which returns the string
# with the sound of the animal
# (Use "Roar" for wolf and lion, "Moo" for bison, and "honk" for goose and parrot).
#c) Create method which represents the current class object as a string
# e.g. output in print command should be like "class Lion name Alex id 2".


class Zoo:
    def __init__(self):
        self._animals = []

    def add_animal(self, animal):
        self._animals.append(animal)

    def remove_animal(self, animal):
        self._animals.remove(animal)


class Wolf:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Lion:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        return "Roar"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Bison:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        return "Moo"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Parrot:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


class Goose:
    def __init__(self, name, _id):
        self.name = name
        self.id = _id

    def play_sound(self):
        return "Honk"

    def __str__(self):
        return f"class {self.__class__.__name__} name {self.name} id {self.id}"


# Example:
if __name__ == "__main__":
    zoo = Zoo()
    wolf = Wolf("Grey Bully", 1)
    lion = Lion("King Leo", 2)
    bison = Bison("Fat Tony", 3)
    parrot = Parrot("Funny Sally", 4)
    goose = Goose("Drunkard Gary", 5)

    zoo.add_animal(wolf)
    zoo.add_animal(lion)
    zoo.add_animal(bison)
    zoo.add_animal(parrot)
    zoo.add_animal(goose)

    for animal in zoo._animals:
        print(animal, f"says:{animal.play_sound()}!")