#!/usr/bin/python

import string
import operator
import dynArray
import itertools
import fixedArray


def main():
    classes = ['Math', 'English', 'Physics', 'History', 'Chemistry', 'Sports']
    grades_dyn = dynArray.DynamicArray([10, 7, 8, 4, 9, 8])

    xx = grades_dyn.dyn_to_dict(classes)
    to_sort_dict = dict(sorted(xx.items(), key=operator.itemgetter(1), reverse=True))

    print(f'\n{"-" * 18}')

    for classes, grade in to_sort_dict.items():
        print(f'{classes:<10} | {grade:<3} |')
        print(f'{"-" * 18}')

    print(f'\033[1m{"Average":<10}\033[0m | \033[1m{sum(to_sort_dict.values())/len(to_sort_dict.values()):<2.1f}\033[0m |')
    print(f'{"-" * 18}')

    #------------------------

    arr_fix = fixedArray.FixedArray([4, 10, 2, 3, 23, 5, 10])
    sorted_arr_fix = arr_fix.sort_array()

    easy_way = dict([i for i in enumerate(sorted_arr_fix)])
    easy_way_revert_mapping = {string.ascii_letters[i].title(): j for i, j in easy_way.items()}

    print("\n")

    for i, j in sorted(easy_way_revert_mapping.items(),
                       key=operator.itemgetter(1), reverse=True):
        print(f'{i}: {j}')


if __name__ == '__main__':
    main()
