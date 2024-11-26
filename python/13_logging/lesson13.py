'''Add logging to the code implemented in the "Concurrency" module.
There should be at least two logging levels: debug and info.
All print statements should be replaced with logging.
Configure logging to print all log messages to the console, and write INFO+ messages to a log file.
Configure and run black, isort & flake8 on the files created in the "Concurrency" module.
Add ".flake8" & "pyproject.toml" files with appropriate settings.
Make sure the configurations are compatible with each other.
(optional) Create a working pre-commit configuration with black, isort & flake8 (i.e. .pre-commit-config.yaml).'''


import time
from multiprocessing import Pool
from os import cpu_count
from functools import wraps
from concurrent.futures import ThreadPoolExecutor
import random
import asyncio
import logging


# Logger
# Configure logging to print all log messages to the console, and write INFO+ messages to a log file.
def setup_logging():
    logger = logging.getLogger('parallel_processing')
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Console handler (DEBUG and above)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # File handler (INFO and above)
    file_handler = logging.FileHandler('parallel_processing.log', mode="a", encoding="utf-8")
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

logger = setup_logging()
logger.info("Logger is configured.")

def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration_time = end_time - start_time
        logger.info(f"Function '{func.__name__}' took {duration_time:} seconds to execute.")
        return result
    return wrapper

#Multiprocessing, CPU-bound work (30 points):
#Create a function (e.g. "calculate_sum(start: int, end: int) -> int") which returns the sum of numbers in the given range including both ends.
@time_logger
def calculate_sum(start: int, end: int) -> int:
    return sum(range(start, end + 1))

#Create another function (e.g. "calculate_sum_parallel") that calls "calculate_sum" in a parallel manner (using "multiprocessing.Pool" or "concurrent.futures.ProcessPoolExecutor"). Split the given range into chunks, obtain the result for each range chunk, and return the total sum. The returning result should be the same as for the first function.
@time_logger
def calculate_sum_parallel(start: int, end: int) -> int:
    chunk_num = cpu_count()
    logger.debug(f"Number of CPU cores: {chunk_num}")
    chunk_size = (end + 1 - start)/chunk_num
    chunks = [(int(start + i*chunk_size), int(min(start+(i+1)*chunk_size-1, end))) for i in range(chunk_num)]
    logger.debug(f"Chunks: {chunks}")
    with Pool(chunk_num) as pool:
        chunk_result = pool.starmap(calculate_sum, chunks) #starmap works with multy args (tuples), map with 1
    return sum(chunk_result)

@time_logger
def calculate_sum_parallel_thread(start: int, end: int) -> int:
    chunk_size = (end + 1 - start)/cpu_count()
    chunks = [(int(start + i * chunk_size), int(min(start + (i + 1) * chunk_size - 1, end))) for i in range(cpu_count())]
    logger.debug(f"Chunks: {chunks}")
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        chunk_result = executor.map(lambda args: calculate_sum(*args), chunks) #lambda to unpack tuple into 2 args for calc_sum
    return sum(chunk_result)


#Run both functions for the range [1, 2**30], verify the result is 576460752840294400.
#Print the times it takes for each approach.

#Multithreading, IO-bound work (30 points):

#Create a function that sleeps for a random amount of time (<10 seconds), prints and returns the sleep duration.
#@time_logger
def sleep_time():
    sleep_time = random.randrange(10)
    time.sleep(sleep_time)
    logger.debug(f"Sleep time is {sleep_time:} seconds.")
    return sleep_time
#Create another function that calls the previous one 20 times using multiple threads in parallel (e.g. use "concurrent.futures.ThreadPoolExecutor" class).
@time_logger
def call_sleep():
    with ThreadPoolExecutor(max_workers=cpu_count()) as executor:
        results = list(executor.map(lambda _: sleep_time(), range(20)))
    return results

#(optional) asyncio practice: Implement the multithreading task above using the asyncio approach.
async def sleep_time_async():
    sleep_time = random.randrange(10)
    logger.debug(f"Sleep time is {sleep_time:} seconds.")
    await asyncio.sleep(sleep_time)
    return sleep_time

@time_logger
async def call_sleep_async():
    sleep_times = [sleep_time_async() for _ in range(20)]
    results = await asyncio.gather(*sleep_times)
    return results



if __name__ == '__main__':
    logger.info("Start of parallel calculation program.")

    start = time.perf_counter()
    result = calculate_sum(1, 2**30)
    duration = time.perf_counter() - start
    logger.info(f"Result of single: {result}")
    logger.info(f"Execution time of single: {duration:.2f}")

    start = time.perf_counter()
    result = calculate_sum_parallel(1, 2**30)
    duration = time.perf_counter() - start
    logger.info(f"Result of parallel: {result}")
    logger.info(f"Execution time of parallel: {duration:.2f}")

    start = time.perf_counter()
    result = calculate_sum_parallel_thread(1, 2**30)
    duration = time.perf_counter() - start
    logger.info(f"Result of parallel thread: {result}")
    logger.info(f"Execution time of parallel thread: {duration:.2f}")


# Thread task for sleep time
    # Print the "total workload" time (the sum of outputs from all calls) and the "max workload" time (the longest task).
    # Print the elapsed time. It should be several times smaller than the "workload" time.
    logger.info("Start of sleep time program.")
    start_time = time.perf_counter()
    workload = call_sleep()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Elapsed time for thread: {elapsed_time:.4f} seconds")

    total = sum(workload)
    max_wl = max(workload)
    logger.info(f"Total workload time is  {total:} seconds.")
    logger.info(f"Max workload time is  {max_wl:} seconds.")
    logger.info(f"Workload: {workload}")
    logger.info(f"Length of workload: {len(workload)}")

#async task for sleep time
    logger.info("Start of async sleep time program.")
    start_time = time.perf_counter()
    as_result = asyncio.run(call_sleep_async())
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    logger.info(f"Elapsed time for async: {elapsed_time:.4f} seconds")
    logger.info(f"Result of async: {as_result}")
    logger.info(f"Length of async: {len(as_result)}")

    total_as = sum(as_result)
    max_as = max(as_result)
    logger.info(f"Total workload time is  {total_as:} seconds.")
    logger.info(f"Max workload time is  {max_as:} seconds.")

# this line here to test pre-commit one more rime
   logger.info("End of parallel calculation program.")
