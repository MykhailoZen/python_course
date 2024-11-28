# Multithreading, IO-bound work (30 points):
# Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
# Create another function that calls the previous one 20 times using multiple threads in parallel
# (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
# Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
# Print the elapsed time. It should be several times smaller than the "workload" time.
import time
from random import choice
from concurrent.futures import ThreadPoolExecutor, as_completed


def execution_time(func):
    def wrapper():
        start_time = time.time()
        f = func()
        print(f'Execution time is{time.time() - start_time: .2f} seconds')
        return f
    return wrapper


def sleep_random_amount():
    sleep_duration = choice(range(1, 10))
    print(f"Sleep duration is {sleep_duration} seconds")
    time.sleep(sleep_duration)
    return sleep_duration


@execution_time
def sleep_parallel():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(sleep_random_amount) for _ in range(20)]
    results = [f.result() for f in as_completed(futures)]
    print(f"Total workload = {sum(results)} seconds")
    print(f"Max workload = {max(results)} seconds")


if __name__ == '__main__':
    execution_time(sleep_random_amount)()
    sleep_parallel()
