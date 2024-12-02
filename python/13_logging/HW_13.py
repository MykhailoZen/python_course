# 1) Add logging to the code implemented in the "Concurrency" module.
# There should be at least two logging levels: debug and info.
# All print statements should be replaced with logging.
# 2) Configure logging to print all log messages to the console, and write INFO+ messages to a log file.
# Configure and run black, isort & flake8 on the files created in the "Concurrency" module.
# Add ".flake8" & "pyproject.toml" files with appropriate settings.
# Make sure the configurations are compatible with each other.
# (optional) Create a working pre-commit configuration with black, isort & flake8 (i.e. .pre-commit-config.yaml).
import logging
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from random import choice


def execution_time(func):
    def wrapper():
        start_time = time.time()
        f = func()
        log.info(f"Execution time is{time.time() - start_time: .2f} seconds")
        return f

    return wrapper


def sleep_random_amount():
    sleep_duration = choice(range(1, 10))
    log.debug(f"Sleep duration is {sleep_duration} seconds")
    time.sleep(sleep_duration)
    log.debug("Finished sleeping.")
    return sleep_duration


@execution_time
def sleep_parallel():
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(sleep_random_amount) for _ in range(20)]
    results = [f.result() for f in as_completed(futures)]
    log.debug(f"Total workload = {sum(results)} seconds")
    log.debug(f"Max workload = {max(results)} seconds")


if __name__ == "__main__":
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

    execution_time(sleep_random_amount)()
    sleep_parallel()
