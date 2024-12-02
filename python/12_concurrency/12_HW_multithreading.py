# Multithreading, IO-bound work
import concurrent.futures
import time
import random
from concurrent.futures import ThreadPoolExecutor
from functools import reduce

# input parameters
number_of_executions = 20
number_of_threads = 5

multithreading_each_duration_list = []


def sleepy():
    start_time = time.time()
    time.sleep(random.randint(0, 10))
    one_sleep_duration = time.time() - start_time
    return one_sleep_duration


def sleep_n_times():
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        futures = [executor.submit(sleepy) for i in range(number_of_executions)]
        for f in concurrent.futures.as_completed(futures):
            multithreading_each_duration_list.append(f.result())

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)


def main():
    start_time = time.time()
    sleep_n_times()
    multithreading_total_duration = time.time() - start_time
    print('List of each execution duration in parallel threads: ', multithreading_each_duration_list)
    print(
        f'Multithreading max workload (longest call): {reduce(lambda x, y: x if x >= y else y, multithreading_each_duration_list)} sec')
    print(
        f'Multithreading total workload (sum of outputs from all calls): {sum(multithreading_each_duration_list)} sec')
    print(f'Multithreading total execution (elapsed) time: {multithreading_total_duration} sec')


if __name__ == '__main__':
    sleepy_duration = sleepy()
    print(f'One-time function executed took {sleepy_duration} sec')

    print(
        f'Function will be executed {number_of_executions} times within {number_of_threads} threads. It will take a while. Please be patient.')
    main()
