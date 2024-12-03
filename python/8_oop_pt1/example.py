class Worker:

    def __init__(self, id):
        self.id = id

    def print_id(self):
        print(f"id: {self.id}")


worker_a = Worker(1)
print(worker_a.id)
# 1
worker_a.id = 5
print(worker_a.id)
# 5
worker_b = Worker(2)
print(worker_b.id)
# 2


class Factory:

    def __init__(self, *args):
        self.workers = args
        # self.factory_modes = kwargs


factory = Factory(worker_a, worker_a)
# print(factory.workers)
# factory.workers = [worker_b]


# static vars
class Car:
    cars_count = 0

    def __init__(self, plate_id):
        self.plate_id = plate_id
        Car.cars_count += 1
        self.factory_id = Car.cars_count


car_a = Car("GH-01")
car_b = Car("HW-03")
car_a.cars_count = 1000
c
# 2
car_b.cars_count
# 2


# print(car_b.cars_count)


# static method
class DMV:
    car_register = {}

    @staticmethod
    def register_car(car):
        DMV.car_register[car.plate_id] = car.factory_id


DMV.register_car(car_b)

dmv_a = DMV()
dmv_a.register_car()


# encapsulation
class PoliceCar:

    def __init__(self, weapon, plate_id):
        self.__weapon = weapon
        self.plate_id = plate_id

    def is_weapon_inside(self):
        return self.__weapon is not None

    def get_weapon(self):
        if self.__weapon is None:
            self.__weapon = "pistol"
        return self.__weapon

    def set_weapon(self, weapon):
        if isinstance(str, weapon):
            self.__weapon = weapon
        else:
            self.__weapon = "pistol"


police_car = PoliceCar("rifle", "PD-01")
print(police_car.is_weapon_inside())
