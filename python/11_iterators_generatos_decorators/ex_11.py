# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.
from datetime import datetime
from time import sleep


def execution_time(func):
    def wrapper():
        start_time = datetime.now().time().second
        func()
        end_time = datetime.now().time().second
        difference = end_time - start_time
        print(f'Execution time is {difference} seconds')
    return wrapper


@execution_time
def test_function():
    sleep(5)
    print('Test function inside.')


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    test_function()
    print(list(fibonacci(10)))
