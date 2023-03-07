#!/usr/bin/python


import time
import threading


def calc_sum_squares(given_number: int):
    calc_sum = 0

    for i in range(given_number):
        calc_sum += i ** 2

    print(calc_sum)


def sleep_a_little(time_to_sleep: int):
    time.sleep(time_to_sleep)


def main():
    start_time = time.time()
    current_threads: list = []

    # here we need multiprocessing...this is a heavy computation task
    for i in range(1, 12):
        value_to_be_calculated: int = (i ** 3) * 10000
        t = threading.Thread(target=calc_sum_squares, args=(value_to_be_calculated, ))
        t.start()
        current_threads.append(t)

    for j in range(len(current_threads)):
        current_threads[j].join()

    end_time = time.time()
    print(f"{'How much time it took for calculations:'} {end_time - start_time}")

    present_threads: list = []
    start_time = time.time()
    for i in range(1, 6):
        t = threading.Thread(target=sleep_a_little, args=(i, ))
        t.start()
        present_threads.append(t)

    for k in range(len(present_threads)):
        present_threads[k].join()

    end_time = time.time()
    print(f"{'How much time for sleep:'} {end_time - start_time}")


if __name__ == '__main__':
    main()
