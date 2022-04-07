#!/usr/bin/python

import random

import pandas as pd
import dynArray
import fixedArray


def main():
    math = fixedArray.FixedArray(10)
    yy = dynArray.DynamicArray([23, 44, 101, 89, 56, 1, 98, 23])

    for i in range(5):
        number = random.randrange(1, 100)
        math.add_in_ascending_sorter_order(number)

    print(math)
    math.reverse_the_array_lazy()
    print(math)


if __name__ == '__main__':
    main()
