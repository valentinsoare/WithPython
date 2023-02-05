#!/usr/bin/python

import collections.abc
from numbers import Integral
from functools import singledispatch


def singledispatch_(fn):
    registry_2: dict = {object: fn}

    def decorated(arg, descending=False, sorting_dict_by='keys'):
        return registry_2.get(type(arg), registry_2[object])(arg, descending, sorting_dict_by)

    def register(type_of_input):
        def inner(fn):
            registry_2[type_of_input] = fn
            return fn
        return inner

    def dispatch(type_argument):
        return registry_2.get(type_argument, registry_2[object])

    decorated.register = register
    decorated.dispatch = dispatch

    return decorated


@singledispatch
def sorting(given_seq, descending: bool = False, sorting_dict_by: str = 'values'):
    return given_seq


@sorting.register(collections.abc.Mapping)
def _sorting_mapping(arg, descending: bool, sorting_dict_by: str, *args):
    if sorting_dict_by == 'values':
        return type(arg)(sorted(arg.items(), key=lambda i: i[1], reverse=descending))
    else:
        return type(arg)(sorted(arg.items(), key=lambda i: i[0], reverse=descending))


@sorting.register(str)
def _sorting_string(arg, descending: bool, *args):
    return ''.join(sorted(list(arg), reverse=descending))


@sorting.register(collections.abc.Sequence)
def _sorting_sequence(arg, descending: bool, *args):
    return type(arg)(sorted(arg, reverse=descending, key=lambda i: float(i)))


@sorting.register(collections.abc.Set)
def _sorting_set(arg, descending: bool, *args):
    return sorted(arg, reverse=descending, key=lambda i: float(i))


def main():
    # here with singledispatch decorator made by me
    #print(sorting_way_cool([4, 10, 2, 3, 10], descending=True))

    #print(sorting_way_cool.dispatch(list))

    #-------------------------------
    # with singledispatch decorator from functools module

    print(sorting.registry)

    print(sorting.dispatch(list))

    print(sorting([4, 10, 2, 3, 101, 99], descending=False))

    print(sorting({'1': 'nebunie', '4': 'lux', '0': 'opulenta'}, descending=True, sorting_dict_by='keys'))

    print(sorting({'1', '22', '4', '3', '0', '11'}, descending=True))

    print(sorting('opulenta', descending=True))




if __name__ == '__main__':
    main()

