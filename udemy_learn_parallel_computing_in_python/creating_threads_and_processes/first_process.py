#!/usr/bin/python

import random
import multiprocessing


def do_work():
    print(f"Starting Work")
    i: int = 0
    for _ in range(20_000_000):
        i += random.randint(1, 10)
    print(f"{'Finished Work'} {'Adding ='} {i}")


def main():
    p_c: list = []

    for _ in range(7):
        p = multiprocessing.Process(target=do_work, args=())
        p_c.append(p)

    for j in p_c:
        j.start()

    for k in p_c:
        k.join()


if __name__ == '__main__':
    multiprocessing.set_start_method('spawn')
    main()
