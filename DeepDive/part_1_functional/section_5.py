#!/usr/bin/python

from functools import partial
import operator

def funct_with_false(first_param=None, second_param=None, third_param=None, if_print=0):
    given_set_with_parameters: set = {first_param, second_param, third_param}
    processed_by_size: set = set(i for i in given_set_with_parameters if i)

    if not processed_by_size:
        raise ValueError('No valid arguments were given')

    if if_print:
        for j, k in enumerate(processed_by_size):
            print(f"{j + 1}. {k}")


def rotate_values(x, y, z):
    a, b, c = x, y, z
    print(f'{a} {b} {c}')
    return c, a, b


def exec_rotate(a=None, b=None, c=None):
    i = 0
    funct_with_false(first_param=a, second_param=b, third_param=b)

    while i < 6:
        a, b, c = rotate_values(a, b, c)
        i += 1

def unpacking_star():
    given_list = [4, 20, 40, 10, 22, 101, 99]

    # a pop alternative from index 0......is the first element
    a, *b = given_list
    print(f"{a} and {b}")

    c, *d = b
    print(f"{c} and {d}")

    e, *f = d
    print(f"{e} and {f}")


def combined_list_with_unpacking():
    l_1 = [4, 10, 22]
    l_2 = [3, 101, 7]

    l_3 = [*l_1, *l_2]
    print(l_3)


def with_sets_dict():
    s = {4, 10, 2, 'a', 'lux'}
    a, b, *c, d = s

    d_1 = {'1': 'nebunie', '2': 'lux', '3': 'altceva', '4': 'eu_stiu'}
    d_2 = {'t': 4, 'a': 2, 'c': 2}
    d_3 = {'p': 9, '2': 'aiurea', 'y': 101}

    our_list = [*d_1, *d_2, *d_3]
    #print(our_list)

    our_set = {*d_1, *d_2, *d_3}
    #print(our_set)

    d = {**d_1, **d_2, **d_3}
    print(d)


def amount(exec_operator, number_2):
    given_list = [100, 402, 101, 78, 88, 99, 62]

    for i in given_list:
        if exec_operator(i, number_2):
            yield i

def main():
    #funct_with_false(first_param='lux', second_param='nebunie', third_param='opulenta')

    #exec_rotate(a=10, b=20, c=30)

    #unpacking_star()

    #combined_list_with_unpacking()

    #with_sets_dict()

    #for_testing(partial(operator.le, 300)))
    word = '<= 100'
    a, b = word.split()

    for i in amount(operator.le, 100):
        print(i)

if __name__ == '__main__':
    main()
