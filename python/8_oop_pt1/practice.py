from abc import ABC, abstractmethod


class Fruits(ABC):
    def __init__(self, color: str, form: str):
        self.color = color
        self.form = form

    def __str__(self):
        return f'I am object of class {self.__class__.__name__} and I have {self.color} color and {self.form} form!'

    @abstractmethod
    def lay_on_table(self):
        pass


class Citrus(Fruits):
    def lay_on_table(self):
        print(f"I'm {self.__class__.__name__} and I'm lying on the table and smelling good")


class NotCitrus(Fruits):
    def lay_on_table(self):
        print(f"I'm {self.__class__.__name__} and I'm lying on the table")


class Apple(NotCitrus):
    def lay_on_table(self):
        super().lay_on_table()
        print(f'I am fresh red apple!')


class Orange(Citrus):
    pass


class Lemon(Citrus):
    pass


class Banana(NotCitrus):
    pass


class BoxFruits:
    def __init__(self):
        self._fruits_list = []

    @abstractmethod
    def fruits_adding(self, fruit_for_adding: Fruits):
        self._fruits_list.append(fruit_for_adding)
        return self

    def fruits_deleting(self, fruits_for_deleting: Fruits):
        self._fruits_list.append(fruits_for_deleting)
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

    print(isinstance(apple, Apple))
    print(isinstance(apple, NotCitrus))
    print(isinstance(apple, Fruits))

    apple.lay_on_table()
