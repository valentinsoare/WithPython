#!/usr/bin/python

import gc
import sys
import ctypes
import timeit


def find_reference_count(input_variable, type_of_return: int):

    if type_of_return == 0:
        return sys.getrefcount(input_variable)
    else:
        return ctypes.c_long.from_address(input_variable).value


def find_objects_in_gc(object_id):
    for i in gc.get_objects():
        print(id(i))


def about_mutability_immutability():
    a = [1, 2, 3]
    b = [4, 5, 6]
    t = (a, b)

    a.append(4)
    b.append(7)

    print(t)


def check_quality():
    a = 10
    b = a

    if a == b:
        print(f'All Good!')

    if a == b:
        print(f'same')

    x = [1, 2, 3, 4]
    y = x
    x.append(5)
    print(x)

    if y is x:
        print(f"OK!")


def everything_is_an_object():
    ax = int(2002)
    ay = str(101)

    #print(type(ay))

    az = int(str(10011110), base=2)    # from binary to decimal
    print(az)


def square(given_value):
    return given_value ** 2


def cube(given_value):
    return given_value ** 3


def select_function(given_id):
    if given_id == 1:
        return square
    else:
        return cube


def exec_function(fn, value):
    return fn(value)


def for_speed():
    x = 1

    if x in {1, 2, 3}:
        print(f"All OK!")


def main():
    #lux = 'nebunie'
    #print(find_reference_count(id(lux), 1))
    #gc.collect()

    #find_objects_in_gc(id(lux))

    #about_mutability_immutability()

    #check_quality()

    #everything_is_an_object()

    #az = square(2)
    #print(az)
    #print(square)

    #print(select_function(2)(4))

    #print(exec_function(cube, 44))

    for_speed()
    print(for_speed.__code__.co_consts)


if __name__ == '__main__':
    main()
