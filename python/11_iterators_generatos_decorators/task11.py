from time import sleep
from datetime import datetime


def time_tracker(func):
    def wrapper():
        start = datetime.now().second
        func()
        end = datetime.now().second
        print(f"Sleeping time: {end - start} seconds")
    return wrapper

@time_tracker
def sleeper():
    sleep(5)
    print("I woke up!")

def fibonachi_func(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    sleeper()
    print(list(fibonachi_func(10)))

