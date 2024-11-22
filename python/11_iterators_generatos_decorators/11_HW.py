# Create a decorator that logs the time taken by a function to execute.
import logging
import timeit

logging.basicConfig(filename='hw_11_logs.txt',
                    format='%(asctime)s %(message)s',
                    filemode='a')


def decorator_logging_execution_time(function):
    def wrapper():
        log_exec_time = timeit.timeit(function, number=1)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.info(f'{function} executes {log_exec_time} sec')

        print(f'Time taken by a function to execute: {log_exec_time} sec')
        return log_exec_time

    return wrapper


@decorator_logging_execution_time
def do_nothing():
    print("I'm doing nothing")


do_nothing()


# Write a generator function that generates Fibonacci numbers up to a specified limit.
def fib_generator(seq_limit):
    current_num = 0
    next_num = 1
    while current_num <= seq_limit:
        if current_num == 0:
            pass
        else:
            yield current_num
        current_num, next_num = next_num, current_num + next_num


limit = input("Enter limit for provided Fibonacci numbers: ")
try:
    if int(limit) > 0:
        fib_sequence = fib_generator(int(limit))
        for num in fib_sequence:
            print(num)
    else:
        print('You have entered value that is less than possible minimum')
except ValueError:
    print('It supposed to be integer')
