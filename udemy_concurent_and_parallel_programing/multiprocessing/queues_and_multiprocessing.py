#!/usr/bin/python

from time import time
from multiprocessing import Process, Queue


def check_value_in_list(given_values, i, number_of_processes, queue):
    max_number_to_check = 10 ** 8

    lower = int(i * max_number_to_check / number_of_processes)
    upper = int((i + 1) * max_number_to_check / number_of_processes)

    number_of_hits = 0
    for i in range(lower, upper):
        if i in given_values:
            number_of_hits += 1

    queue.put((lower, upper, number_of_hits))


max_processes = 4
start_time = time()
processes = []
comparison_list = [1, 25059458, 85072815, 5508147]
queue = Queue()

for i in range(max_processes):
    t = Process(target=check_value_in_list, args=(comparison_list, i, max_processes, queue))
    processes.append(t)

for t in processes:
    t.start()

for t in processes:
    t.join()

queue.put('DONE')


while True:
    v = queue.get()
    if v == 'DONE':
        break

    lower, upper, number_of_hits = v
    print(f"* In the Range of {lower} - {upper} - > number_of_hits: {number_of_hits}")

print(f"Execution_time: {round(time() - start_time, 1)}")
