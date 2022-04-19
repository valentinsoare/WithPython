#!/usr/bin/python

import string
import dynArray
import fixedArray
import stackArray


def main():
    classes = fixedArray.FixedArray(['math', 'physics', 'chemistry', 'computer science', 'english'])
    classes_dict = classes.fixed_to_dict(given_keys=list(string.ascii_uppercase), to_return=1)
    sorted_array_classes = classes.sort_array(reverse=False, to_return=True)
    to_fixed = fixedArray.to_stack(sorted_array_classes)

    print(to_fixed)


if __name__ == '__main__':
    main()
