# Multiprocessing, CPU-bound work (30 points):
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given
# range including both ends.
# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks,
# obtain the result for each range chunk, and return the total sum. The returning result should be the same as for
# the first function.
# Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
# Print the times it takes for each approach.
from concurrent.futures import ProcessPoolExecutor
from functools import reduce
import time


def execution_time(func):
    def wrapper(*args):
        start_time = time.time()
        f = func(*args)
        print(f'Execution time is{time.time() - start_time: .2f} seconds')
        return f

    return wrapper


def calculate_sum(start: int, end: int) -> int:
    return reduce(lambda x, y: x + y, range(start, end + 1))


def calculation_wrapper(r: range) -> int:
    return calculate_sum(r.start, r.stop - 1)


@execution_time
def calculate_sum_parallel(start: int, end: int, chunks: int) -> int:
    chunk_length = (end - start) // chunks
    with ProcessPoolExecutor() as executor:
        results = executor.map(calculation_wrapper, [range(start, end + 1)[i:i + chunk_length + 1]
                                                     for i in range(0, end, chunk_length + 1)])
    return sum(list(results))


if __name__ == '__main__':
    print(f"The sum is {execution_time(calculate_sum)(1, 2 ** 30)}")
    print(f"The sum in a parallel is {calculate_sum_parallel(1, 2 ** 30, 20)}")
