from abc import ABC, abstractmethod


class Fruits(ABC):
    def __init__(self, color: str, form: str):
        self.color = color
        self.form = form

    def __str__(self):
        return f'I am an object of class {self.__class__.__name__} and I have {self.color} color and {self.form} shape.'

    def __eq__(self, other):
        if isinstance(other, Fruits):
            return self.form == other.form
        return False

    @abstractmethod
    def laying_on_table(self):
        pass


class Citrus(Fruits):
    def laying_on_table(self):
        print(f"I'm {self.__class__.__name__} I'm laying on the table and smell good")


class NotCitrus(Fruits):
    def laying_on_table(self):
        print(f"I'm {self.__class__.__name__} I'm laying on the table")


class Apple(NotCitrus):
    pass


class Orange(Citrus):
    pass


class Lemon(Citrus):
    pass


class Banana(NotCitrus):
    pass


class BoxFruits:
    def __init__(self):
        self._fruits_list = []

    def fruits_adding(self, fruit_for_adding: Fruits):
        self._fruits_list.append(fruit_for_adding)
        return self

    def fruits_deleting(self, fruit_for_deleting: Fruits):
        self._fruits_list.remove(fruit_for_deleting)
        return self

    def fruits_erasing(self):
        self._fruits_list.clear()
        return self

    @property
    def fruits_list(self):
        return self._fruits_list


if __name__ == "__main__":
    apple = Apple("red", "oval")
    orange = Orange("orange", "round")
    lemon = Lemon("yellow", "round")
    banana = Banana("green", "long")

    boxFruits = BoxFruits()
    boxFruits.fruits_adding(apple).fruits_adding(orange).fruits_adding(lemon).fruits_adding(banana)

    for fruit_from_box in boxFruits.fruits_list:
        print(fruit_from_box)

    print(lemon == orange)
    print(banana != orange)
    print(isinstance(lemon, Lemon))
    print(isinstance(lemon, Citrus))
    print(isinstance(lemon, Fruits))
