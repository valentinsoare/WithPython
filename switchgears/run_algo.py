#!/usr/bin/python

import string
import numpy as np
from operator import itemgetter
from collections import OrderedDict


def calculate_recursive(n):
    if n > 0:
        calculate_recursive(n - 1)    # head recursion
        k = n ** 2
        print(f'{k}', end=" ")
        calculate_recursive(n - 1)   # tail recursion

        # if both of them are on, then we have tree recursion


def sum_of_numbers(n):
    if n == 0:
        return 0
    else:
        return n + sum_of_numbers(n - 1)


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)


def multiplication(a, b):
    if b == 1:
        return a
    else:
        return a + multiplication(a, b - 1)


def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x - 1) + fib(x - 2)


def is_palindrome(given_input):
    if len(given_input) <= 1:
        return True
    #elif given_input[0] != given_input[-1]:
    #    return False
    else:
        return given_input[0] == given_input[-1] and is_palindrome(given_input[1:-1])


def linear_search(given_array, length_of_the_array, desired_value):
    index = 0
    to_check = ''

    while index < length_of_the_array:
        if isinstance(given_array[index], str):
            to_check = given_array[index].lower()

        if given_array[index] == desired_value or to_check == desired_value:
            return index

        index += 1

    return -1


def binary_search_iterative(given_array, desired_value):
    left = 0
    right = len(given_array) - 1

    while left <= right:
        index = (left + right) // 2

        if given_array[index] == desired_value:
            return index
        elif desired_value < given_array[index]:
            right = index - 1
        elif desired_value > given_array[index]:
            left = index + 1

    return -1


def binary_search_recursive(given_array, desired_value, left, right):
    index = (left + right) // 2

    if left > right:
        return -1
    else:
        if given_array[index] == desired_value:
            return index
        elif desired_value < given_array[index]:
            return binary_search_recursive(given_array, desired_value, left, index - 1)
        elif desired_value > given_array[index]:
            return binary_search_recursive(given_array, desired_value, index + 1, right)


def selection_sort(given_array):
    n = len(given_array)

    for i in range(n - 1):
        position = i

        for j in range(i+1, n):
            if given_array[j] < given_array[position]:
                position = j

        given_array[i], given_array[position] = given_array[position], given_array[i]


def insertion_sort(given_array):
    length_of_array = len(given_array)

    for i in range(1, length_of_array):
        needed_value = given_array[i]
        position = i

        while position > 0 and given_array[position - 1] > needed_value:
            given_array[position] = given_array[position - 1]
            position -= 1

        given_array[position] = needed_value


def main():
    #calculate_recursive(3)

    #ax = sum_of_numbers(4)
    #print(ax)

    #ay = factorial(5)
    #print(ay)

    #az = multiplication(2, 3)
    #print(az)

    #print(is_palindrome("aiurea"))

    #x = [fib(n) for n in range(15)]
    #print(x)

    #----------------------------------

    #Linear search
    #given_list = ['nebunie', 'lux', 'oracle', 'ce nu trebuie', 150, 'Blacklist', 'BMW', 'Honda', 4, 10]
    #print(linear_search(given_list, len(given_list), 100))

    #Binary Search - log(n) growth
    #given_array = [4, 10, 11, 15, 18, 19, 23, 27, 31, 37, 42, 45, 47, 50, 58, 62, 69, 72, 76, 79]
    #print(binary_search_iterative(given_array, 31))
    #print(binary_search_recursive(given_array, 79, 0, len(given_array) - 1))

    #---------------------------------

    given_array = [4, 10, 2, 3, 38, 20, 17, 21, 14, 18, 34]
    #selection_sort(given_array)
    insertion_sort(given_array)
    print(given_array)

    #-------------------------------
    #second_array = [(4, 10), (2, 7), (6, 3), (9, 2)]

    #sorted_array = sorted(second_array, key=itemgetter(0))
    #print(sorted_array, end="\n\n")

    #for i, j in sorted_array:
    #    k = 0
    #    while k < i // 2:
    #        print(f' |')
    #        k += 1
    #    print(f' | {"#" * j}')

    #print(f' |', end=" ")
    #print(f'{"-" * sorted_array[len(sorted_array) - 1][0]}')
    #------------------------------










if __name__ == '__main__':
    main()
