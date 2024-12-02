# Multiprocessing, CPU-bound work
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
import time

duration = 0


def exec_timer(function):
    def wrapper(*args):
        start_time = time.time()
        fun_exec = function(*args)
        global duration
        duration = time.time() - start_time
        return fun_exec

    return wrapper


@exec_timer
def calculate_sum(start: int, end: int):
    return reduce(lambda a, b: a + b, range(start, end + 1))


# takes values from range() as parameters and executes 'calculate_sum' function with them as arguments
def mapper_range_values(range_val):
    return calculate_sum(range_val.start, range_val.stop)


@exec_timer
def calculate_sum_parallel(start: int, end: int):
    given_range = range(start, end)
    processes = multiprocessing.cpu_count()
    chunk_size = (len(given_range) + 1) // processes + 1
    chunks = [given_range[i - 1: i - 2 + chunk_size] for i in range(start, end + 1, chunk_size)]

    with ProcessPoolExecutor() as executor:
        result = list(executor.map(mapper_range_values, chunks))

    return sum(result)


if __name__ == '__main__':
    print('Sum of all integers from 1 to 2**30 will be calculated. It will take a while.')

    synch_ver = calculate_sum(1, 2 ** 30)
    print(f'Result of Synchronous Version: {synch_ver}. Calculation took {duration} sec')

    multi_proc_ver = calculate_sum_parallel(1, 2 ** 30)
    print(f'Result of Multi-Processed Version: {multi_proc_ver}. Calculation took {duration} sec')
