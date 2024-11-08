class Zoo:
    _animals = []

    def __str__(self):
        final = []
        for a in self._animals:
            single_animal = a.__str__()
            final.append(single_animal)
        return str(final)

    def add_animals(self, *animals):
        for animal in animals:
            self._animals.append(animal)

    def remove_animals(self, *animals):
        for animal in animals:
            self._animals.remove(animal)


class Animal:
    a_name = ""
    a_id = 0

    def __init__(self, a_name, a_id):
        self.a_name = a_name
        self.a_id = a_id

    def __str__(self):
        return f"{self.a_name} {self.a_id}"

    def play_sound(self):
        pass


class Wolf(Animal):
    def play_sound(self):
        return "Roar"

    def show_info(self):
        print(f"Class: Wolf; name: {self.a_name}; id: {self.a_id}")


class Lion(Animal):
    def play_sound(self):
        return "Roar"

    def show_info(self):
        print(f"Class: Lion; name: {self.a_name}; id: {self.a_id}")


class Bison(Animal):
    def play_sound(self):
        return "Moo"

    def show_info(self):
        print(f"Class: Bison; name: {self.a_name}; id: {self.a_id}")


class Parrot(Animal):
    def play_sound(self):
        return "Honk"

    def show_info(self):
        print(f"Class: Parrot; name: {self.a_name}; id: {self.a_id}")


class Goose(Animal):
    def play_sound(self):
        return "Honk"

    def show_info(self):
        print(f"Class: Goose; name: {self.a_name}; id: {self.a_id}")



wolf = Wolf("Alex", 1)
lion = Lion("Mary", 2)
bison = Bison("Jack", 3)
parrot = Parrot("Mike", 4)
goose = Goose("Sam", 5)

zoo = Zoo()
zoo.add_animals(wolf, lion, bison, parrot, goose)

print(zoo)
wolf.show_info()
print(wolf.play_sound())

zoo.remove_animals(wolf)
print(zoo)