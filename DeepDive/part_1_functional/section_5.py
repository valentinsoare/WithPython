#!/usr/bin/python
import random
import time
from re import split
from functools import partial
import operator
import keyword
from datetime import datetime
from os import getlogin

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

    ax = {'10', '20'}
    ay = {'30', '50'}
    print(f"Executing: {ax.union(ay)}")

def amount(exec_operator, number_2):
    given_list: set = {100, 402, 101, 78, 88, 99, 62}
    to_return: set = set()

    for i in given_list:
        if exec_operator(i, number_2):
            to_return.add(i)

    return to_return

#-----------------------------------------------

def compare(what_to_execute=None):
    dict_to_work_with: dict = {}
    operators = {'>': operator.gt,
                 '<': operator.lt,
                 '>=': operator.ge,
                 '<=': operator.le,
                 '==': operator.eq}
    credits_bank = {100, 402, 101, 78, 88, 99, 62}
    period_of_credits = {12, 48, 32, 82, 42, 92, 62}
    first_map = {'amount': credits_bank, 'period': period_of_credits}
    order_of_operands: list = []

    given_list_with_arguments: list = what_to_execute.split()
    command_to_execute: str = ''
    count: int = 0
    counting: int = 0

    for i in given_list_with_arguments:
        if i not in ['and', 'or']:
            command_to_execute += i + ' '
            counting += 1
        else:
            order_of_operands.append(i)

        if counting == 3:
            what_to_search, operator_value, value_to_compare = command_to_execute.split()

            if not (what_to_search and operator_value and value_to_compare) or what_to_search not in first_map \
                    or operator_value not in operators:
                raise ValueError('You need to use a variable instance for comparison, a valid operator and an integer!')

            try:
                value_to_compare = float(value_to_compare)
            except ValueError:
                raise ValueError(f'Value to compare should be an integer or float!')

            dict_to_work_with[count] = set()
            for j in first_map[what_to_search]:
                if operators[operator_value](j, value_to_compare):
                    dict_to_work_with[count].add(j)

            command_to_execute: str = ''
            counting = 0
            count += 1

        if count == 1:
            if i == 'and' and not len(dict_to_work_with[count - 1]):
                return None
            elif i == 'or' and len(dict_to_work_with[count - 1]):
                return dict_to_work_with[count - 1]
        elif count == 2:
            if not (len(dict_to_work_with[0]) and len(dict_to_work_with[1])):
                return None

    return dict_to_work_with


def extended_unpacking():
    given_list = ['10', '20', 'lux si opulenta']
    mancare = {12: 'cartofi', 22: 'maine_prajita'}
    given_list = dict((i, j) for i, j in enumerate(given_list))

    combined_them = {**given_list, **mancare}
    print(combined_them)


def calling_function(*args, variable):
    print(f"{list(args)} and {variable}")


def printing_variables(*, first_name, last_name):
    print(f'{first_name} and {last_name}')


def exec_function(*args, **kwargs):
    for i in range(len(args)):
        if (i + 1) % 2 == 0:
            kwargs.update({args[i - 1]: args[i]})

    print(kwargs)


def time_it(fn, *args, how_many_times=1, **kwargs):

    i = 0
    start = time.perf_counter()

    while i < how_many_times:
        fn(*args, **kwargs)
        i += 1
    end = time.perf_counter()

    return (end - start) / how_many_times


def log_to_file(message, date_time=None):
    date_time = date_time or datetime.utcnow()

    with open('to_write_to', mode='a', encoding='utf-8') as file_to_write_to:
        print(f"{date_time} - {getlogin()}: {message}", file=file_to_write_to)


def printing_a_message():
    message_to_be_printed = 'lux si opulenta boss, sa fi bine sa nu fie rau!!'
    j = 0
    count = 5

    while j < count:
        for i in message_to_be_printed.split(sep=', '):
            words = i.split()
            random.shuffle(words)
            log_to_file((' '.join(words)))
        j += 1


def main():
    #funct_with_false(first_param='lux', second_param='nebunie', third_param='opulenta')

    #exec_rotate(a=10, b=20, c=30)

    #unpacking_star()

    #combined_list_with_unpacking()

    #with_sets_dict()

    #for_testing(partial(operator.le, 300)))
    #word = '<= 100'
    #a, b = word.split()

    #ax = amount(operator.le, int(b))
    #print(ax)

    #az: dict = compare(what_to_execute='amount > 100 and period > 20 and amount > 20')
    #print(az)

    #extended_unpacking()

    #calling_function(1, 2, 3, 4, 5, variable=100)
    #calling_function_v2(variable=101)

    #printing_variables(first_name='valentin', last_name='soare')

    #exec_function(4, 'lux', a='opulenta', b='ce facem ?')

    #ax = time_it(print, 'Lux', 'Si Opulenta',  end=' # ', flush=True, how_many_times=5)
    #print(f"\n{ax}")

    printing_a_message()


if __name__ == '__main__':
    main()
