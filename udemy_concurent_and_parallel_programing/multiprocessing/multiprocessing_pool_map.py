#!/usr/bin/python

from time import time
from multiprocessing import Pool, cpu_count


def square(number):
    return number ** 2


max_processes = 4
comparison_list = list(range(123))
start_time = time()

number_of_cpu_available = cpu_count()
number_of_cpus_to_use = max(1, number_of_cpu_available - 1)

print(f"Number of CPUs available: {number_of_cpu_available}")

with Pool(number_of_cpus_to_use) as mp_pool:
    result = mp_pool.map(square, comparison_list)

print(result)

print(f"Execution_time: {round(time() - start_time, 1)}")
