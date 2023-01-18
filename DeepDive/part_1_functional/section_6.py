#!/usr/bin/python

import inspect
import random
import decimal
import fractions
from re import match


def first_one(first_argument: str, second_argument: float) -> str:
    """this is the shit documentation for this function
    boss. What the fuc man ?"""
    return 'a_boss_the_boss'


def executing(*, first_name: str = 'Valentin', last_name: str = 'Soare',
              **kwargs: 'rest of the positional parameters') -> None:
    """printing first name and last name"""

    print(f'{first_name} & {last_name}, age: {kwargs.get("age")}')

    #ax = match(r'(\d{4}-){3}(\d{4})', '4256-0311-0752-2490')
    #print(ax.group())


def sexy_things():
    given_dict = {'first': 'lux', 'second': 'opulenta', 'third': 'nebunie'}

    #parsing = lambda i: i, given_dict
    #reversing_value = list(str(i)[::-1] for i in (lambda word: word, list(given_dict.values())))

    #print(len(reversing_value))

    parsing_v2 = lambda j: j.capitalize()
    print(parsing_v2('boss'))


def apply_function(first_argument, fn):
    return fn(decimal.Decimal(str(first_argument)))


def calc_average(*args):
    return (lambda i: sum(i)/len(i))(args)


def sort_a_dict(given_dict, *, by_element='key'):
    sorted_dict: dict = {}
    element = given_dict.keys() if by_element == 'key' else given_dict.values()

    sorted_elements = sorted((lambda k: k)(element))
    if by_element == 'key':
        for i in sorted_elements:
            sorted_dict.update({i: given_dict[i]})
    else:
        swapped_given_dict = {j: i for i, j in given_dict.items()}
        for l in sorted_elements:
            sorted_dict.update({swapped_given_dict[l]: l})

    return sorted_dict


# TODO: sorting dict function to remember
def another_version_of_sort_a_dict(given_dict, *, by_element='key'):
    return dict(sorted(given_dict.items(), key=lambda i: i[0])) if by_element == 'key' \
        else dict(sorted(given_dict.items(), key=lambda i: i[1]))


# TODO: shuffle an iterable with sorted and random.random
def randomized_an_iterable_with_sorted(given_list):
    return sorted(given_list, key=lambda i: random.random())


def main():
    #help(first_one)
    ##ax = first_one()

    #executing(first_name='Tudorina', last_name='Soare', age='56')

    #sexy_things()

    #decimal.getcontext().prec = 4
    #result = apply_function('10', lambda i: i ** decimal.Decimal('0.5'))
    #print(result)

    #print(f"Average: {calc_average(10, 40, 22, 30, 18, 19):.2f}")

    #az = sort_a_dict({'lux': 10, 'nebunie': 25, 'opulenta': 4}, by_element='key')
    #print(az)

    #at = another_version_of_sort_a_dict({'lux': 10, 'nebunie': 25, 'opulenta': 4}, by_element='value')
    #print(at)

    at = randomized_an_iterable_with_sorted([1, 4, 10, 77, 9, 7, 56, 101])
    print(at)

    #---------------------------------
    #print(dir(another_version_of_sort_a_dict))

    #print(another_version_of_sort_a_dict.__code__.co_varnames)
    #print(another_version_of_sort_a_dict.__code__.co_names)
    #print(another_version_of_sort_a_dict.__code__.co_argcount)

    #if inspect.isfunction(another_version_of_sort_a_dict):
    #    print(f'YES')

    #print(inspect.getsource(another_version_of_sort_a_dict))

    #print(inspect.getmodule(another_version_of_sort_a_dict))

    #print(inspect.getcomments(another_version_of_sort_a_dict))

    #ax = inspect.signature(another_version_of_sort_a_dict)
    #print(ax.parameters)
    #------------------------------------


if __name__ == '__main__':
    main()
