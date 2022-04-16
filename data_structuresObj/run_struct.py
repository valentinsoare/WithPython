#!/usr/bin/python
import operator

import dynArray
import fixedArray
import stackArray


def main():
    main_array_fixed = fixedArray.FixedArray(['math', 'physics', 'chemistry', 'computer science', 'english'])
    ab = main_array_fixed.fixed_to_dict(given_keys=[1, 2, 3, 4, 5])

    for i, j in sorted(ab.items(), key=operator.itemgetter(0), reverse=True):
        print(f'{i}. {j}')


if __name__ == '__main__':
    main()
