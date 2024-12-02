# Create a decorator that logs the time taken by a function to execute.
# Write a generator function that generates Fibonacci numbers up to a specified limit.
from datetime import datetime
from time import sleep


def execution_time(func):
    def wrapper():
        start_time = datetime.now().time().second
        func()
        print(f"Execution time is {datetime.now().time().second - start_time} seconds")

    return wrapper


@execution_time
def test_function():
    sleep(5)
    print("Test function inside.")


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


if __name__ == "__main__":
    test_function()
    print(list(fibonacci(10)))
