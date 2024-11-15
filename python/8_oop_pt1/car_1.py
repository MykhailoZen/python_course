def go_to_work_all(atr):
    print(f"I arrived! Your {atr}\n")


class Cars:
    # Class attributes
    number_of_doors = 4

    # class constructor + Instance Attributes
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color
        self._seats = 5

    # class method
    def go_to_work(self):
        self.__engine_start()
        print(f"I arrived! Your {self.brand} with seats {self._seats}\n")

    def __engine_start(self):
        print(f"Engine started for {self.brand}")

    @staticmethod
    def go_to_work_2():
        print("I arrived! Your car!")


if __name__ == '__main__':
    # instantiation
    my_car = Cars("Mercedes", "red")
    friend_car = Cars("BMW", "white")

    # print(f"Friend's car color is {friend_car.color}")
    # my_car.go_to_work_2()
    my_car.go_to_work()
    friend_car.go_to_work()

    my_car._Cars__engine_start()

    # Cars.go_to_work_2()
    # Cars.number_of_doors = 6
    # print(f"Class - {Cars.number_of_doors}")
    # print(f"Object - {my_car.number_of_doors}")
    #
    # friend_car.brand = "Ferrari"
    # print(friend_car.brand)

