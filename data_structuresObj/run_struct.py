#!/usr/bin/python

import string
import dynArray
import fixedArray
import stackArray


def main():
    classes = fixedArray.FixedArray(['math', 'physics', 'chemistry', 'computer science', 'english'])
    classes_dict = classes.fixed_to_dict(given_keys=list(string.ascii_uppercase[0:5]), to_return=1)
    classes_stack_array = fixedArray.to_stack(classes_dict)


if __name__ == '__main__':
    main()
