#!/usr/bin/python

import re
import math


def remainder_one():
    print(f' *Integers:', end=" ")
    for i in range(100, 999):
        to_count = 0
        for j in [2, 3, 4, 5, 6, 7]:
            if i % j == 1:
                to_count += 1
                if to_count == 6:
                    print(f'{i}', end=" ")


def finding_integer():
    final = ''
    to_begin = int(math.sqrt(31415))

    while not re.search(r'^31415', final):
        to_begin += 1
        final = str(to_begin ** 2)

    print(f'\n **Found number: {to_begin} - Reached pattern: {final}')


def main():
    remainder_one()
    finding_integer()


if __name__ == '__main__':
    main()
