# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.

from datetime import datetime
from time import sleep


def decorator_function(func):
    def wrapper():
        start_time = datetime.now().time().second
        func()
        end_time = datetime.now().time().second
        print(f'The time of execution is {end_time - start_time} seconds')

    return wrapper


@decorator_function
def sleep_func():
    sleep(5)
    print("I'm wake up")

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    sleep_func()
    for x in fibonacci(10):
        print(x)
