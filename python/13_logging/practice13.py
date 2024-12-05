import logging
import time
from random import choice
from concurrent.futures import ThreadPoolExecutor, as_completed


def execution_time(func):
    def wrapper():
        start_time = time.time()
        f = func()
        end_time = time.time()
        log.info(f'Execution time is{end_time - start_time: .2f}')
        return f

    return wrapper


def random_amount_sleep():
    duration_sleep = choice(range(1, 10))
    log.debug(f"The sleep duration is {duration_sleep}")
    time.sleep(duration_sleep)
    return duration_sleep


@execution_time
def parallel_sleep():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(random_amount_sleep) for _ in range(20)]
    return [f.result() for f in as_completed(futures)]


if __name__ == '__main__':
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    log_stream = logging.StreamHandler()
    log_stream.setLevel(logging.DEBUG)
    log.addHandler(log_stream)

    log_file = logging.FileHandler("log.txt", mode="w")
    log_file.setLevel(logging.INFO)
    log_file_formatter = logging.Formatter(
        fmt="[%(asctime)s] [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    log_file.setFormatter(log_file_formatter)
    log.addHandler(log_file)
    execution_time(random_amount_sleep)()
    results = parallel_sleep()
    log.debug(f"The total workload time is {sum(results)}")
    log.debug(f"The max workload time is {max(results)}")
