# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.

from datetime import datetime
from time import sleep

def decorator_function(func):
    def wrapper():
        start_time = datetime.now().time().second
        func()
        end_time = datetime.now().time().second
        print(f"duration time is {end_time - start_time} seconds")
    return wrapper

@decorator_function
def wake_up():
    sleep(3)
    print('Wake up!')

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    wake_up()

    for number in fib(9):
        print(number)




