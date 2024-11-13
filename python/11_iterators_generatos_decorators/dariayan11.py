from datetime import datetime
from time import sleep


def time_decorator(func):
    print(datetime.now().strftime("%H:%M:%S"))
    return func

@time_decorator
def my_func():
    print('My function called!')

my_func()

print('a) Create a decorator that logs the time taken by a function to execute.')
def count_func_execution_time(func):
    start_time = datetime.now().time().second
    func()
    end_time = datetime.now().time().second
    dif  = end_time - start_time
    print(f'Execution time is {dif}')
    return func

@count_func_execution_time
def test_function():
    sleep(5)
    print('Test function inside.')

print('b) Write a generator function that generates Fibonacci numbers up to a specified limit.')
def fibonacci_generator(stop=10):
    current_fib, next_fib = 0, 1
    for _ in range(0, stop):
        fib_number = current_fib
        current_fib, next_fib = (next_fib, current_fib + next_fib)
        yield fib_number

print(list(fibonacci_generator()))





