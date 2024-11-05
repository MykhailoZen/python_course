#Create a decorator that logs the time taken by a function to execute.
import time
from functools import wraps

def time_loggger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        print(f"Function '{func.__name__}' took {duration_time:} seconds to execute.")
        return result
    return wrapper

#Write a generator function that generates Fibonacci numbers up to a specified limit.
@time_loggger
def fibonacci(limit):
    #fibonacci limited by number of sequence members
    start_sequence = [0, 1]
    index = 0
    while len(start_sequence) < limit:
        start_sequence.append(start_sequence[index] + start_sequence[index + 1])
        index += 1
    yield start_sequence


my_fib = fibonacci(10)
print("Number of members")
print(list(my_fib))

@time_loggger
def fibonacci_w_val_lim():
    #fibonacci limited by member value
    x, y = 0, 1
    while True:
        yield x
        x, y = y, x + y

fib2 = fibonacci_w_val_lim()
limit = 35
fib_list = []
for i in fib2:
    if i < limit:
        fib_list.append(i)
    else:
        break
print("Member value")
print(fib_list)