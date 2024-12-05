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
        end_time = time.time()
        print(f'Execution time is{end_time - start_time: .2f}')
        return f

    return wrapper


def random_amount_sleep():
    duration_sleep = choice(range(1, 10))
    print(f"The sleep duration is {duration_sleep}")
    time.sleep(duration_sleep)
    return duration_sleep


@execution_time
def parallel_sleep():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(random_amount_sleep) for _ in range(20)]
    return [f.result() for f in as_completed(futures)]


if __name__ == '__main__':
    execution_time(random_amount_sleep)()
    results = parallel_sleep()
    print(f"The total workload time is {sum(results)}")
    print(f"The max workload time is {max(results)}")
