class Zoo:
    def __init__(self):
        self._animals = []

    def add(self, element: str):
        self._animals.append(element)

    def remove(self, element: str):
        self._animals.remove(element)

    @property
    def animals(self):
        return self._animals


class Wolf:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        sound = "Roar"
        return sound


class Lion:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        sound = "Roar"
        return sound


class Bison:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        sound = "Moo"
        return sound


class Parrot:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        sound = "Honk"
        return sound


class Goose:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def play_sound(self):
        sound = "Honk"
        return sound


if __name__ == '__main__':
    wolf = Wolf("Alex", 1)
    print(f"class {wolf.__class__.__name__} name {wolf.name} id {wolf.id}")
    lion = Lion("Tom", 2)
    print(f"class {lion.__class__.__name__} name {lion.name} id {lion.id}")
    bison = Bison("Sarah", 3)
    print(f"class {bison.__class__.__name__} name {bison.name} id {bison.id}")
    parrot = Parrot("Patric", 4)
    print(f"class {parrot.__class__.__name__} name {parrot.name} id {parrot.id}")
    goose = Goose("Chloe", 5)
    print(f"class {goose.__class__.__name__} name {goose.name} id {goose.id}")
    zoo = Zoo()
    zoo.add(wolf.name)
    zoo.add(lion.name)
    zoo.add(bison.name)
    zoo.add(parrot.name)
    zoo.add(goose.name)
    for x in zoo.animals:
        print(x)
