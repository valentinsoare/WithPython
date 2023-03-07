#!/usr/bin/python

import inspect
import random
import decimal
import fractions
from re import match
import numpy as np
import functools
import operator

def first_one(first_argument: str, second_argument: float) -> str:
    """this is the shit documentation for this function
    boss. What the fuc man ?"""
    return 'a_boss_the_boss'


def executing(*, first_name: str = 'Valentin', last_name: str = 'Soare',
              **kwargs: 'rest of the positional parameters') -> None:
    """printing first name and last name"""

    #print(f'{first_name} & {last_name}, age: {kwargs.get("age")}')

    ax = match(r'(\d{4}-){3}(\d{4})', '4256-0311-0752-2490')
    #print(ax.group())


def sexy_things():
    given_dict = {'first': 'lux', 'second': 'opulenta', 'third': 'nebunie'}

    #parsing = lambda i: i, given_dict
    #reversing_value = list(str(i)[::-1] for i in (lambda word: word, list(given_dict.values())))

    #print(len(reversing_value))

    parsing_v2 = lambda j: j.capitalize()
    #print(parsing_v2('boss'))


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

    executing(first_name='Tudorina', last_name='Soare', age='56')

    sexy_things()

    decimal.getcontext().prec = 4
    result = apply_function('10', lambda i: i ** decimal.Decimal('0.5'))
    #print(result)

    #print(f"Average: {calc_average(10, 40, 22, 30, 18, 19):.2f}")

    #az = sort_a_dict({'lux': 10, 'nebunie': 25, 'opulenta': 4}, by_element='key')
    #print(az)

    t = another_version_of_sort_a_dict({'lux': 10, 'nebunie': 25, 'opulenta': 4}, by_element='value')
    #print(at)

    at = randomized_an_iterable_with_sorted([1, 4, 10, 77, 9, 7, 56, 101])
    #print(at)

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

    ax = inspect.signature(another_version_of_sort_a_dict)
    #print(ax.parameters)
    #------------------------------------

    #print(another_version_of_sort_a_dict.__defaults__)
    #print(another_version_of_sort_a_dict.__kwdefaults__)
    #print(another_version_of_sort_a_dict.__code__)
    #print(another_version_of_sort_a_dict.__code__.co_varnames)
    #print(another_version_of_sort_a_dict.__code__.co_argcount)

    #------------------------------------

    #print(inspect.getsource(another_version_of_sort_a_dict))

    az = inspect.signature(another_version_of_sort_a_dict)
    #print(az.parameters)
    #------------------------------------

    #print(callable(iter))

    #-------------------------------------

    def sqrt(given_number):
        return given_number**1/2

    processed_numbers = list(map(sqrt, np.random.randint(12, 244, 12)))
    #print(processed_numbers)

    def combined_values(value_1, value_2):
        return value_1[0], [value_1[1].capitalize(), value_2.upper()]

    dict_1 = {'RO': 'Romania', 'UK': 'United Kingdom', 'FR': 'France', 'DE': 'Germany'}
    list_1 = ['lei', 'pounds', 'euros', 'euros']

    given_values = dict(map(combined_values, tuple(dict_1.items()), list_1))
    #print(given_values)

    combined_them = list((*dict_1.values(), *list_1))
    #print(combined_them)

    #--------------------------------------------

    def is_even(given_number):
        return given_number % 2 == 0

    even_numbers = filter(is_even, np.random.randint(1, 999, 20))
    #print(list(even_numbers))

    #-------------------------------------------

    l1 = 'python'
    l2 = range(101)

    find_indexes = zip(l2, l1)
    #print(list(find_indexes))

    #-------------------------------

    aax = [i**2 for i in range(10) if i**2 < 25]
    #print(aax)

    #--------------------------------

    #for index, value in zip(range(100), np.random.randint(1, 99, 20)):     # same thing like enumerate
    #    print(f'{index}: {value}')

    #--------------------------------
    ax = list((i**2 for i in np.random.randint(1, 10, 5) if i % 2 != 0))

    ay = [i**2 for i in np.random.randint(1, 10, 5) if i % 2 != 0]

    #print(ax)
    #=--------------------------------
    def maximum(nr_1, nr_2):
        to_return = nr_1
        if to_return < nr_2:
            return nr_2

        return to_return

    def find_max(zz):
        max_value = zz[0]

        for i in range(1, len(zz)):
            max_value = maximum(max_value, zz[i])

        return max_value

    #print(find_max([4, 10, 2, 22, 34, 12, 10]))

    #--------------------------------------------------

    given_list = [4, 10, 22, 101, 98, 67, 23, 56, 142]
    add = lambda x, y: x + y

    sum_of_elements = given_list[0]

    for i in range(1, len(given_list)):
        sum_of_elements = add(sum_of_elements, given_list[i])

    #print(f"Classic: {sum(given_list)} and Alternative: {sum_of_elements}")

    #---------------------------------------------------

    final_result = functools.reduce(lambda x, y: x if x < y else y, given_list)
    #print(final_result)

    #print(any(given_list))

    #----------------------------------------

    our_list = [0, 4, None, None]

    our_result = functools.reduce(lambda i, j: bool(i) or bool(j), our_list)
    #print(our_result)    # simulating any

    #----------------------------------

    given_list = np.random.randint(1, 10, 10)

    calc_product = functools.reduce(lambda i, j: i * j, given_list)
    #print(calc_product)

    fact_new_way = functools.reduce(lambda k, l: k * l, range(1, 6))
    #print(fact_new_way)

    #------------------------------------

    given_list = [4, 10, 2, 4, 12, 44, 23, 10, 101]

    def simulate_reduce(fn, given_iterable, initializer=None):
        it = iter(given_iterable)

        if initializer:
            final_value = initializer
        else:
            final_value = next(it)

        for i in it:
            final_value = fn(final_value, i)

        return final_value

    #print(f'\nAlternative way: {simulate_reduce(lambda i, j: i + j, given_list)}\nClassic way: {sum(given_list)}')

    factorial_calc = functools.reduce(lambda i, j: i * j, range(1, 6))
    #print(f"Factorial of 5 is {factorial_calc}")

    def fact(n):
        return 1 if n < 2 else n * fact(n - 1)

    #print(f'Classic way of factorial: {fact(5)}')

    #--------------------------------------------------


def employee(first_name, last_name, age):
    print(f"\n * Employee: {first_name}, {last_name}; Age: {age}")


def catch_and_release(first_name, last_name):
    return employee(first_name, last_name, 35)

catch_and_release('Valentin', 'Soare')


f = functools.partial(employee, age=35)
f('Valentin', 'Soare')


x = lambda i: employee(i, last_name='Soare', age=35)
x('Valentin')

y = functools.partial(employee, age=35)
y('Valentin', 'Soare')

#-------------------------------
l1 = [1, 4, 10, 22, 23, 4]

x = lambda i, j: operator.lt(i, j)

print(x(10, 2))

xx = 'lux'
yy = 'opulenta'

result = operator.concat(xx, yy)
print(result)

if operator.contains(l1, 22):
    print(f'Trueeeee')

zz = operator.countOf(l1, 4)
print(zz)

given_dict = {'4': 'lux', '6': 'si', '3': 'opulenta', '1': 'ron', '5': 'romania', '2': 'bucuresti'}

sorting_dict = sorted(given_dict.items(), key=operator.itemgetter(1))
print(sorting_dict)

lista = [4, 10, 22, 101, 89, 1001]
ff = operator.itemgetter(*range(4))

print(ff(lista))


given_str = 'bucuresti'
method_name = 'capitalize'

ax = operator.attrgetter('upper')
print(ax(given_str)())

print(operator.methodcaller(method_name)(given_str))

#----------------------------------------------------
print(f"{'-' * 75}")

ax = operator.add(1, 4)
az = operator.truediv(4, 2)


if operator.ne(1, 4):
    print(f'True')

lista_2 = [4, 10, 22, 101, 89, 1]
result_product = functools.reduce(operator.mul, lista_2)

print(result_product)

print(operator.truth(lista_2))

my_req = operator.getitem(lista_2, 2)
print(my_req)

my_req_adv = operator.itemgetter(*[3, 4, 5])
print(my_req_adv(lista_2))

operator.setitem(lista_2, 0, 0)

print(lista_2)

given_values = [(4, 10, 2), (3, 2, 10), (22, 4, 10), (101, 4, 0)]

print(sorted(given_values, key=operator.itemgetter(0)))

word = 'opulenta'

fx = operator.methodcaller('split', 'l')

print(fx(word))


if __name__ == '__main__':
    main()
