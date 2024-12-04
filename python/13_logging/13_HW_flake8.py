# Multithreading, IO-bound work
import concurrent.futures
import logging
import time
import random
from asyncio import FIRST_EXCEPTION
from concurrent.futures import ThreadPoolExecutor
from functools import reduce

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s.%(msecs)03d: %(levelname)s: %(name)s: %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S")

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

file_handler = logging.FileHandler(
    'concurrency_13_HW.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# input parameters
number_of_executions = 20
number_of_threads = 5

multithread_runs = []


def sleepy():
    start_time = time.time()
    sleep_val = random.randint(0, 10)
    logger.debug(
        f'Function "{sleepy.__name__}" will sleep for '
        f'{sleep_val} sec during execution')
    time.sleep(sleep_val)
    one_sleep_duration = time.time() - start_time
    return one_sleep_duration


def sleep_n_times():
    counter = 0
    with ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        futures = [
            executor.submit(sleepy) for i in range(number_of_executions)]
        for f in concurrent.futures.as_completed(futures):
            multithread_runs.append(f.result())
            counter += 1
            logger.debug(
                f'Function "{sleepy.__name__}" execution  '
                f'#{counter} took {f.result()} sec')

        # Wait for all tasks to complete
        done, not_done = concurrent.futures.wait(
            futures, return_when=FIRST_EXCEPTION)

        for future in done:
            if future.exception():
                logger.error(f"Exception occurred: {future.exception()}")


def main():
    start_time = time.time()
    sleep_n_times()
    multithreading_total_duration = time.time() - start_time
    logger.info(
        f'Durations of each of {number_of_executions} '
        f'executions in parallel threads: {multithread_runs}')
    logger.info(
        f'Multithreading max workload (longest call): '
        f'{reduce(lambda x, y: x if x >= y else y, multithread_runs):.3f} sec')
    logger.info(
        f'Multithreading total workload (sum of outputs from '
        f'{number_of_executions} calls): '
        f'{sum(multithread_runs):.3f} sec')
    logger.info(
        f'Multithreading total execution (elapsed) time: '
        f'{multithreading_total_duration:.3f} sec')


if __name__ == '__main__':
    sleepy_duration = sleepy()
    logger.info(f'One-time execution of function '
                f'"{sleepy.__name__}" took {sleepy_duration:.3f} sec')
    logger.debug(
        f'\nFunction "{sleepy.__name__}" will be executed '
        f'{number_of_executions} times within {number_of_threads} threads')
    main()
