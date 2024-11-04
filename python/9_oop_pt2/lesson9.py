class Zoo:
    def __init__(self):
        self._animals = []

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

class Bird(Animal):
    def play_sound(self):
        return "honk"

class Predator(Animal):
    def play_sound(self):
        return "Roar"

class Prey(Animal):
    def play_sound(self):
        return "Moo"

class Wolf(Predator):
    pass

class Lion(Predator):
    pass

class Bioson(Prey):
    pass

class Goose(Bird):
    pass

my_zoo = Zoo()
leo = Lion("Leo", 2)
goose = Goose("Geegee", 3)
wolfy = Wolf("Wolfy", 4)
my_zoo.an_add(leo)
my_zoo.an_add(goose)
duck = Goose("Duckly", 7)
my_zoo.an_add(duck)
my_zoo.an_add(wolfy)
print (my_zoo._animals)
my_zoo.an_remove(leo)
print (my_zoo._animals)

print(leo.play_sound())
print(goose)
print(my_zoo)

