import time

# Create a decorator that logs the time taken by a function to execute.
def time_decorator(function):
    def wrapper(*args):
        start = time.time()
        result = function(*args)
        end = time.time()
        print(end - start)
        return result
    return wrapper


# Write a generator function that generates Fibonacci numbers up to a specified limit
@time_decorator
def gen(limit):
    num1, num2 = 0, 1
    while num1 < limit:
        yield num1
        num1, num2 = num2, num1 + num2


for i in gen(10):
    print(i)