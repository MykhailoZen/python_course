# CPU-bound task
# Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers
# in the given range including both ends.
import time
import random
import concurrent.futures
from concurrent.futures.process import ProcessPoolExecutor

def calculate_sum(start: int, end: int) -> int:
    res = 0
    for i in range(start, end +1):
        res += i
    return res

# Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner
# (using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks,
# obtain the result for each range chunk, and return the total sum.
# The returning result should be the same as for the first function.
# Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
# Print the times it takes for each approach.


def calculate_sum_parallel(start: int, end: int) -> int:

    chunk_size = (end - start)//4
    print(chunk_size)

    with ProcessPoolExecutor() as executor:
        chunks = []

        for i in range(start, end + 1, chunk_size):
            chunk_start = i
            chunk_end = min(i + chunk_size - 1, end)
            print(chunk_start, chunk_end)
            chunks.append(executor.submit(calculate_sum, chunk_start, chunk_end))
        return sum(result.result() for result in chunks)

if __name__ == '__main__':

    start = time.time()
    print("Results for calculate_sum():", calculate_sum(1, 2**30))
    print(f"Time spent: {time.time() - start:.2f}")

    start = time.time()
    print("Result of calculate_sum_parallel():", calculate_sum_parallel(1, 2**30))
    print(f"Time spent: {time.time() - start:.2f}")


# Results for calculate_sum(): 576460752840294400
# Time spent: 33.10
# Result of calculate_sum_parallel(): 576460752840294400
# Time spent: 8.31



# IO-bound task:

# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
# def sleep_time():
#     duration = random.random() * 10
#     time.sleep(duration)
#     print(f"Sleeping for {duration:.2f} seconds.")
#     return duration

# start = time.time()
# for _ in range(20):
#     sleep_time()
# print(f"Total workload: {time.time() - start:.2f}")

# Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the elapsed time. It should be several times smaller than the "workload" time.
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).

# def new_sleep_time():
#     start = time.time()
#     with concurrent.futures.ThreadPoolExecutor() as pool:
#         for _ in range(20):
#             pool.submit(sleep_time)
#     print("\n")
#     print(f"The elapsed time is: {time.time() - start:.2f}")



# new_sleep_time()

