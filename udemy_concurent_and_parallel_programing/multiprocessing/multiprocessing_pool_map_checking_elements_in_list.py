#!/usr/bin/python

from multiprocessing import Pool, cpu_count


def check_number_of_values_in_range(comp_list, lower, upper):
    number_of_hits = 0
    for i in range(lower, upper):
        if i in comp_list:
            number_of_hits += 1

    return number_of_hits

max_processes = 4
comparison_list = [2, 3, 4]
lower_and_upper_bounds = [(0, 25*10**6), (25*10**6, 50*10**6), (50*10**6, 75*10**6)]


number_of_cpu_available = cpu_count()
number_of_cpus_to_use = max(1, number_of_cpu_available - 1)

print(f"Number of CPUs available: {number_of_cpu_available}")

with Pool(number_of_cpus_to_use) as mp_pool:
    result = mp_pool.starmap(check_number_of_values_in_range, zip(comparison_list, lower_and_upper_bounds)) # [(2, 5), (4, 6), (3, 7)]

print(result)
