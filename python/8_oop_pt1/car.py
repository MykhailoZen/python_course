class Car:
    # Class attributes
    number_of_doors = 4

    # class constructor + Instance Attributes
    def __init__(self, brand: str, color: str):
        self.brand = brand
        self.color = color

    def print_attr(self):
        print(
            f"My car: \nBrand: {self.brand} \nColor: {self.color} \nNumber of doors: {Car.number_of_doors}\n"
        )

    def go_to_work(self):
        self._engine_start()
        print(f"I arrived! Your {self.brand}\n")

    @staticmethod
    def get_door_numbers():
        print(f"Number of doors: {Car.number_of_doors}")

    def _engine_start(self):
        print(f"Engine started for {self.brand}")

    def __do_name_mangling(self):
        print(f"Papapram for {self.brand}")


if __name__ == "__main__":
    # instantiation
    my_car = Car("Mercedes", "red")

    # Calling attribute
    print(f"My car color is {my_car.color}\n")

    # Calling the public methods
    my_car.print_attr()
    my_car.go_to_work()
    my_car.get_door_numbers()
    Car.get_door_numbers()

    # Calling the protected method
    my_car._engine_start()

    # Calling the private method (name mangling)
    my_car._Car__do_name_mangling()
