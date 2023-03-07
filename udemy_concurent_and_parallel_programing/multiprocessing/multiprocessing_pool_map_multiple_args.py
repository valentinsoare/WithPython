#!/usr/bin/python


from time import time
from functools import partial
from multiprocessing import Pool, cpu_count


def square(x, y):
    return x ** y


max_processes = 4
comparison_list = [2, 3, 4]
power_list = [4, 5, 6]

number_of_cpu_available = cpu_count()
number_of_cpus_to_use = max(1, number_of_cpu_available - 1)

print(f"Number of CPUs available: {number_of_cpu_available}")

with Pool(number_of_cpus_to_use) as mp_pool:
    result = mp_pool.starmap(square, zip(comparison_list, power_list)) # [(2, 5), (4, 6), (3, 7)]

print(result)
