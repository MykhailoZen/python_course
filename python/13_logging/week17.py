import multiprocessing
import concurrent.futures
import time
import logging

range_start = 1
range_end = 2**5
num_parts = multiprocessing.cpu_count()

def calculate_range_sum(range_start, range_end):

    res_1 = sum(range(range_start, range_end + 1))
    return res_1

def split_range_into_n_parts(range_start, range_end, num_parts):

    part_size = (range_end - range_start) // num_parts
    remainder = (range_end - range_start) % num_parts
    start = range_start
    end = range_start
    ranges_split = []

    for _ in range(num_parts):
        end += part_size + (1 if remainder > 0 else 0)
        ranges_split.append(range(start, end))
        start = end
        remainder -= 1
    return ranges_split

def process_data(item):

    return sum(item)

def main_task(data_x):
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_parts) as executor:
        futures = [executor.submit(process_data, item) for item in data_x]
        results = [future.result() for future in concurrent.futures.as_completed(futures)]
    return sum(results)

if __name__ == "__main__":
    logger = logging.getLogger("logger")
    logging.basicConfig(level=logging.DEBUG, filename='app.log', filemode='w',
                        format='%(asctime)s - %(levelname)s - %(message)s')
    logging.debug("starting 1 phase")
    start_time = time.time()
    range_sum = calculate_range_sum(range_start, range_end)
    logging.debug("finishing 1 phase")

    logging.debug("starting 2 phase")
    straight_calc_total = round(time.time() - start_time, 2)
    logging.info('straight calc took %s seconds', straight_calc_total)
    logging.info('straight calc result: %s', range_sum)
    logging.debug("finishing 2 phase")

    logging.debug("starting 3 phase")
    start_time = time.time()
    ranges_split = split_range_into_n_parts(range_start, range_end +1, num_parts)
    split_list_total = round(time.time() - start_time, 2)
    logging.info('split list took %s seconds', split_list_total)
    logging.debug("finishing 3 phase")

    logging.debug("starting 4 phase")
    start_time = time.time()
    result = main_task(ranges_split)
    split_calc_total = round(time.time() - start_time, 2)
    logging.info('split calc took %s seconds', split_calc_total)
    logging.info('split calc result: %s', result)
    logging.debug("finishing 4 phase")


