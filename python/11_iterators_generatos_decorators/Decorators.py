# Practice
# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.

from time import sleep
from datetime import datetime

def decorator(func):
    def wrapper():
        start_time = datetime.now().time().second
        func()
        end_time = datetime.now().time().second
        print(f'The difference between {start_time} and {end_time} is {end_time - start_time}')
    return wrapper

@decorator
def sleeping_function():
    sleep(5)
    print('I am very fresh after sleep!')

def fibonacci_numbers(n: int):
    a = 0
    b = 1
    for _ in range(n):
        yield a
        a = b
        b = a + b


if __name__ == "__main__":
    sleeping_function()
    print(f'Fibonacci sequence is {list(fibonacci_numbers(7))}')









