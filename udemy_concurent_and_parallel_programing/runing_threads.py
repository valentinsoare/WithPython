#!/usr/bin/python

import time
from workers.SleepyWorkers import SleepyWorker
from workers.SquaredSumWorkers import SquaredSumWorker


def main():
    start_time = time.time()
    current_workers: list = []

    for i in range(12):
        value_calc: int = (i + 1) * 1000000
        squared_sum_worker = SquaredSumWorker(given_number=value_calc)
        current_workers.append(squared_sum_worker)

    for j in range(len(current_workers)):
        current_workers[j].join()

    stop_time = time.time()
    print(f"{'Calculating sum of square took: '}{stop_time - start_time}")


if __name__ == '__main__':
    main()
