#!/usr/bin/python

import inspect
import random
import string
from time import perf_counter
import functools
import datetime
import os
import decimal
from fractions import Fraction



def intro_for_scopes():
    _print = lambda i: f'hello {i}'
    s = _print('world')

    print(s)
    print('nebunie', s)


def first_func():
    var = 10

    def second_funct():
        nonlocal var
        var = 'Bo$$'

    second_funct()
    print(var)


def outer():
    variable = 'we go to work work work'        # in other words this is the default value

    def inner():
        words = (sorted(list(j), key=lambda i: random.random()) for j in variable.split())
        ax = list(''.join(i) for i in words)
        printing = ' '.join((i.capitalize() for i in ax))

        print(printing)

    return inner


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


def another_outer():
    count = 0

    def inc_1():
        nonlocal count
        count += 1
        return count

    def inc_2():
        nonlocal count
        count += 1
        return count

    return inc_1, inc_2


def adder(n):
    def inner(x):
        return x + n

    return inner


def incrementer(step):
    def to_begin(start):
        result = start

        def add():
            nonlocal result
            result += step
            return result
        return add
    return to_begin


def adding_words(final_result: str):
    def to_do_the_adding(*args):
        nonlocal final_result
        final_result = ' '.join(args)
        return final_result
    return to_do_the_adding


def power(base):
    def exec_power(exponent):
        return base ** exponent
    return exec_power


def creat_closure():
    list_with_closures = []

    for i in range(2, 5):
        #list_with_closures.append(lambda j: j ** i)
        list_with_closures.append(lambda j, k=i: j ** k)       # to fix this, y here is a local variable, we do not have a closure

    # it is a bug with closures and shared  free variable

    return list_with_closures


class Averager:
    def __init__(self):
        self._count: int = 0
        self._given_numbers: list = []

    @property
    def given_numbers(self):
        return self._given_numbers

    @property
    def count(self):
        return len(self.given_numbers)

    def add_numbers(self, args):
        if isinstance(args, str) or isinstance(args, int) or isinstance(args, float):
            self._given_numbers.append(float(args))
            self._count += 1
        else:
            for i in args:
                self._given_numbers.append(float(i))
                self._count += 1

    def calc_average_with_lambdas(self):
        return functools.reduce(lambda i, j: i + j, self.given_numbers)/self.count

    def calc_average_with_sum(self):
        return (sum(self.given_numbers))/self.count

    def __str__(self):
        return f'count: {self.count}\n' \
               f'numbers: {self.given_numbers}'


def averager():
    numbers = []

    def calc_average(args):
        nonlocal numbers
        if isinstance(args, int) or isinstance(args, str) or isinstance(args, float):
            numbers.append(float(args))
        else:
            for i in args:
                numbers.append(float(i))
        return sum(numbers)/len(numbers)

    return calc_average


def averager_v2():
    total = 0
    count = 0

    def calc_average(args):
        nonlocal total, count

        if isinstance(args, int) or isinstance(args, str) or isinstance(args, float):
            total += float(args)
            count += 1
        else:
            for i in args:
                total += float(i)
                count += 1

        return total/count

    return calc_average


class Timer:
    def __init__(self):
        self._start = perf_counter
        self._end = perf_counter

    @property
    def start(self):
        return self._start

    @property
    def end(self):
        return self._end

    def start_time(self):
        return self._start()

    def end_time(self):
        return self._end()

    def time_on_action(self, given_fn):
        if callable(given_fn):
            ax = self.start_time()
            numbers = given_fn()
        else:
            ax = self.start_time()
            numbers = given_fn

        ay = self.end_time()

        return ay - ax, numbers


def timer():
    start_time = perf_counter()

    def run_timer():
        return perf_counter() - start_time

    return run_timer


def countering(start_value: int = 0):
    value = start_value

    def run_counter(args, step=1):
        nonlocal value

        if isinstance(args, list) or isinstance(args, dict) or isinstance(args, set) \
                or isinstance(args, frozenset) or isinstance(args, tuple):
            for i in args:
                value += step
        else:
            value += step

        return value
    return run_counter


counters: dict = {}


def cool_counter(fn):
    @functools.wraps(fn)                          # to keep metadata of the original function that is decorated, original function is fn.
    def run_counter(*args, step=1, **kwargs):
        global counters

        if fn.__name__ not in counters:
            counters[fn.__name__] = 1
        else:
            counters[fn.__name__] += step

        return fn(*args, **kwargs)
    #run_counter = functools.wraps(fn)(run_counter) or up version
    return run_counter


def _add(a, b):
    return a + b


def _div(a, b):
    return a / b


def cool_print():
    message: str = ''
    def run_print(*values, sep: str = '_', end: str = '|'):
        nonlocal message
        if sep:
            if not isinstance(values, int) and not isinstance(values, float):
                for i in values:
                    message += str(i) + sep
            else:
                message += str(values) + sep
        else:
            if not isinstance(values, int) or not isinstance(values, float):
                for i in values:
                    message += str(i) + ' '
            else:
                message += str(values) + ' '

        if end:
            message += end

        print(message)
    return run_print


def create_timer(fn):
    start_time: decimal.Decimal = decimal.Decimal('0.00')

    @functools.wraps(fn)
    def run_timer(*args, **kwargs):
        nonlocal start_time
        start_time = decimal.Decimal(str(perf_counter()))

        return fn(*args, **kwargs), decimal.Decimal(str(perf_counter())) - start_time
    return run_timer


def scrambled(fn):
    printing: str = ''

    @functools.wraps(fn)
    def run_scrambled_print(*args):
        nonlocal printing
        words: list = []

        for i in args:
            if isinstance(i, str):
                words.extend(list(sorted(k, key=lambda n: random.random()) for k in i.split()))
            elif isinstance(i, int) or isinstance(i, float) or isinstance(i, decimal.Decimal):
                words.append(str(i))
            else:
                for z in i:
                    if isinstance(z, int) or isinstance(z, float) or isinstance(z, decimal.Decimal):
                        z: str = str(z)
                    if z.split() != 1:
                        z: list = z.split()
                    words.extend(list(sorted(p, key=lambda n: random.random()) for p in z))

        intermediary: list = list(''.join(i) for i in words)
        printing = ' '.join((i.capitalize() for i in intermediary))

        return fn(printing)
    return run_scrambled_print


def timer_app(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def run_function_in_timer(*args, **kwargs):
        start_time: float = perf_counter()
        implement_function = fn(*args, **kwargs)
        end_time: float = perf_counter()
        time_to_completion = end_time - start_time

        args_as_strings = list(str(i) for i in args)
        kwargs_as_strings = list(f"{k}={l}" for k, l in kwargs.items())
        args_ = args_as_strings + kwargs_as_strings
        str_with_args = ', '.join(args_)

        print(f"Output: {implement_function}\nTime_to_completion: {time_to_completion:.6f}\n"
              f"Arguments given: {str_with_args}")

        return implement_function, time_to_completion
    return run_function_in_timer


def calc_fib_recursive(n):
    if n <= 2:
        return 1
    else:
        return calc_fib_recursive(n - 2) + calc_fib_recursive(n - 1)


@timer_app
def fib_recursive(n):
    return calc_fib_recursive(n)


@timer_app
def calc_fib_loop(n):
    nr_1 = 1
    nr_2 = 1
    for i in range(3, n+1):
        #Classic way
        #temp = nr_2
        #nr_2 = nr_1 + nr_2
        #nr_1 = temp

        # Pythonic way
        nr_1, nr_2 = nr_2, nr_1 + nr_2

    return nr_2


def logged(fn):
    from os import getlogin
    from functools import wraps
    from datetime import datetime, timezone

    @wraps(fn)
    def run_function_inner(*args, **kwargs):
        current_user: str = getlogin()
        current_time = datetime.now(timezone.utc)
        result_to_return = fn(*args, **kwargs)

        with open(file='file_to_logg.txt', mode='a', encoding='utf-8') as file_to_write_to:
            print(f"{current_time}; {current_user}; {fn.__name__} - {result_to_return}", file=file_to_write_to)

        return result_to_return
    return run_function_inner


@logged
def create_banner(*, message: str):
    to_print: list = [f"*# {message.split()[0]}", f"{message.split()[-1]} #*"]
    full_message: str = ' '.join(to_print)

    length_to_use: int = len(full_message)

    print(f"\n{' ' * 40}{' ' * (length_to_use // 2)}{full_message}")
    print(f"{' ' * 40}{'-' * (length_to_use * 2)}")

    print(f"\n{' ' * 10}Yoyyy.....we are seeing how to log!")

    return f'Banner message generated with message {full_message}'

def calc_fib_wth_memoization(n):
    if n <= 2:
        return 1
    else:
        return calc_fib_wth_memoization(n - 2) + calc_fib_wth_memoization(n - 1)


class Fib:
    def __init__(self):
        self._cache: dict = {1: 1, 2: 1}

    @property
    def cache(self):
        return self._cache

    def fib(self, n):
        if n not in self.cache:
            self._cache[n] = self.fib(n - 2) + self.fib(n - 1)

        return self.cache[n]


def calc_fib():
    cache: dict = {1: 1, 2: 1}

    def run_fib_calc(n):
        nonlocal cache

        if n not in cache:
            cache[n] = run_fib_calc(n - 2) + run_fib_calc(n - 1)

        return cache[n]
    return run_fib_calc


def memoization(fn):
    cache: dict = {}

    @functools.wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]

    return inner


@memoization
def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


@memoization
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n - 1)


@functools.lru_cache(maxsize=512)
def another_fib_cool(n):
    return 1 if n <= 2 else another_fib_cool(n - 2) + another_fib_cool(n - 1)


def time_with_params(how_many_runs):
    def timed(fn):
        from time import perf_counter

        @functools.wraps(fn)
        def run_time(*args, **kwargs):
            total_time_passed: float = 0.0

            for i in range(how_many_runs):
                start_time = perf_counter()
                our_result = fn(*args, **kwargs)
                total_time_passed += (perf_counter() - start_time)

            print(f" * Average time: {total_time_passed/how_many_runs}")
            return our_result
        return run_time
    return timed



#def printing(*, height=0, width=0):
#    print(f" * Custom pretty print with height: {height} and width: {width}")

#    def running_decorator(fn):

#        @functools.wraps(fn)
#        def inner(message):
#            for i in range(height): print()
#            print(f"{' ' * width}{message}")

#        return inner
#    return running_decorator

#@printing(height=1, width=0)
#def display(given_message):
#    print(given_message)


class Printing:
    def __init__(self, height: int = 0.0, width: int = 0.0):
        self.height = height
        self.width = width
        #print(f" * Custom pretty print with height: {height} and width: {width}")

    def __call__(self, fn):
        @functools.wraps(fn)
        def inner(message):
            for i in range(self.height): print()
            print(f"{' ' * self.width}{message}")

        return inner


@Printing(height=4, width=10)
def display(given_message):
    print(given_message)


@functools.lru_cache(maxsize=256)
def timing_fib(n):
    return 1 if n <= 2 else another_fib_cool(n - 2) + another_fib_cool(n - 1)


def check_values_fraction(numerator, denominator):
    return True if numerator % denominator == 0 else False


def dec_builtin_class(cls):
    cls.speak = lambda self: check_values_fraction(self.numerator, self.denominator)
    return cls


Fraction = dec_builtin_class(Fraction)


#----------------

def sorting_list(arg, descending, *args):
    return list(sorted(arg, reverse=descending))


def sorting_set(arg, descending, *args):
    return set(sorted(arg, reverse=descending))


def sorting_dict(arg, descending: bool, sorting_dict_by: str, *args):
    if sorting_dict_by == 'values':
        return dict(sorted(arg.items(), key=lambda i: i[1], reverse=descending))
    else:
        return dict(sorted(arg.items(), key=lambda i: i[0], reverse=descending))


def sorting_string(arg, descending: bool, *args):
    return ''.join(sorted(list(arg), reverse=descending))


def sorting_tuple(arg, descending, *args):
    return tuple(sorted(arg, reverse=descending))


def sorting_default(*args):
    raise ValueError('We need a data structure like a list, set, dict, '
                     'tuple, string in order to be able to sort the elements')


def singledispatch(fn):
    registry_2: dict = {object: fn,
                        dict: sorting_dict,
                        str: sorting_string,
                        tuple: sorting_tuple,
                        list: sorting_list,
                        set: sorting_set}

    def inner(arg, descending: bool = False, sorting_dict_by: str = 'values'):
        return registry_2.get(type(arg), registry_2[object])(arg, descending, sorting_dict_by)

    return inner


@singledispatch
def sorting_way_cool(arg):
    return arg


#def sorting_data_structures(arg, descending: bool = False, sorting_dict_by: str = 'values'):
#    registry = {set: sorting_set,
#                dict: sorting_dict,
#                str: sorting_string,
#                tuple: sorting_tuple,
#                list: sorting_list,
#                'default': sorting_default}

#    fn = registry.get(type(arg), registry['default'])
#    return fn(arg, descending, sorting_dict_by)





def main():
    #intro_for_scopes()
    #first_func()

    ###------ closures

    #exported_as_variable_from_those_two_functions_as_closure = outer()
    #exported_as_variable_from_those_two_functions_as_closure()

    #-----------------------------

    #i = 0
    #ax = counter()

    #while i < 5:
    #    print(ax())
    #    time.sleep(2)
    #    i += 1

    #--------------------------------

    #in_1, in_2 = another_outer()

    #print(f"{in_1()} and {in_2()} and {in_1()} and {in_2()}")

    #---------------------------------

    #return_fn = adder(4)

    #for i in range(5):
    #    print(return_fn(i))

    #--------------------------------

    #fn = incrementer(10)
    #print(fn(400)())

    #--------------------------------

    #to_add_action = adding_words('')
    #word = to_add_action(*['lux', 'opulenta'])

    #word += to_add_action(*['lume', 'buna', 'fotbal', 'baschet'], *['diablo', 'csgo', 'half-life'])
    #print(word)

    #--------------------------------

    #cube = power(3)

    #print(cube(2))

    #------------------------------------

    #given_list_with_pow = []

    #for i in range(2, 6):
    #    given_list_with_pow.append(power(i))

    #print(given_list_with_pow[0](3))
    #print(given_list_with_pow[1](3))
    #print(given_list_with_pow[2](3))

    #------------------------------------
    #list_with_functions = []

    # it is a bug with closures and shared  free variable

    #for i in range(2, 5):
    #    list_with_functions.append((lambda j: j ** i))

    #print(list_with_functions[0](2))
    #print(list_with_functions[1](2))

    #-----------------------------------------

    #closuring = creat_closure()
    #print(closuring[0](2))
    #print(closuring[1](2))

    #-----------------------------------------

    #---------Averager with class
    #init_class = Averager()
    #init_class.add_numbers(4)
    #init_class.add_numbers([10, 100, 404, 10])
    #init_class.add_numbers({'21', '89'})

    #print(init_class.given_numbers)
    #print(init_class.count)

    #print(f'Average_1: {init_class.calc_average_with_lambdas()}')
    #print(f'Average_2: {init_class.calc_average_with_sum()}')

    #--------------Averager with closure
    #fn = averager()
    #fn(101)
    #fn([4, 10, '4', 10, 4, 5, 21, '10', '50'])
    #fn(['2', '4', '5', '10', '55', '23', '1', '4'])
    #print(fn(55))

    #-------------Avrager v2 with closure

    #fn_2 = averager_v2()

    #print(fn_2(5))
    #print(fn_2(10))
    #print(fn_2([4, 10, 2, '10']))

    #--------------------------------------

    #to_use = Timer()
    #result = to_use.time_on_action(numpy.random.randint(0, 1000, 20))

    #print(result)

    #----------------------------------------

    #az = timer()

    #print(az())
    #print(az())
    #print(az())

    #-------------------------------------------

    #to_use_for_counting = countering(start_value=0)
    #azz = to_use_for_counting(args=[4, 10, 22, 3, 12, 44, 23, '101', decimal.Decimal('4.10')], step=1)

    #print(azz)

    #--------------------------------------------
    #counters: dict = dict()

    #add = cool_counter(_add, counters)             # decorators
    #div = cool_counter(_div, counters)             # decorators

    #add(4, 2)
    #add(10, 4)
    #add(11, 4)
    #add(20, 44)

    #div(10, 2)
    #div(44, 10)
    #div(100, 44)

    #print(add(4, 2))
    #print(div(100, 2))

    #-------------------------------------------------
    #add(4, 2)
    #add(10, 2)

    #@cool_counter
    #def add(a, b):
    #    return a + b

    #@cool_counter
    #def div(a, b):
    #    return a / b

    #@cool_counter
    #def mult(a, b):
    #    return a * b

    #add(2, 4)
    #add(10, 2)
    #add(18, 4)
    #add(3, 7)

    #div(10, 8)
    #div(5, 2)
    #div(9, 3)

    #mult(10, 4)

    #print(inspect.signature(mult))

    #-------------------------------------------------

    #cool_print()(*[4, 100, 2, 50, 22, 3, 78, 93])

    #------------------------------------------------

    #@create_timer
    #def populate_list(given_list=[], range_to_use=10_000):
    #    for i in range(range_to_use):
    #        given_list.append(random.randrange(0, 1_000_000))

    #    return given_list

    #print(populate_list([], 15_000))

    #------------------------------------------------

    #@scrambled
    #def _print(values):
    #    """Printing scrambled input values"""
    #    print(values)


    #az = print('lux opulenta', 'este', 44, 23)
    #_print(['el', 'este', 'nebunie', 'facem regee'])

    #-------------------------------------------------

    #print(['eu', 2], [4, 2], [10, 22, 34, 41, 23], 'lux', 'ce putem sa facem ma boss aici')

    #-------------------------------------------------

    #fib_recursive(40)
    #calc_fib_loop(10000)

    #-------------------------------------------------

    #create_banner(message='Calendar App')

    #-------------------------------------------------
    #memoization using class
    #f = Fib()

    #az = f.fib(10)
    #print(az)

    #print(f.cache)

    #--------------------------------------------
    #memoization using closures

    #x = calc_fib()

    #print(x(6))

    #----------------------------------------
    #memoization and decorators

    #print(fib(4))
    #print(fib(10))
    #print(fib(22))
    #print(fib(202))

    #----------------------------------------
    # memoization and factorial

    #print(fact(5))
    #print(fact(6))
    #print(fact(50))
    #print(fact(23))

    #----------------------------------------
    # memoization but this time with builtin functools.lru_cache

    #print(another_fib_cool(6))
    #print(another_fib_cool(19))
    ##print(another_fib_cool(89))
    #print(another_fib_cool(110))
    #print(another_fib_cool(78))
    #-----------------------------------------------

    #timing_fib(892)

    #---------------------------------------------

    #display('Lux si opulenta')

    #---------------------------------------------

    #given_f = Fraction(3, 5)
    #Fraction.speak = lambda self: f'Fraction says {self.numerator * self.denominator}'

    #print(given_f.speak())
    #---------------------------------------------

    #given_f = Fraction(4, 1)
    #Fraction.is_integral = lambda self: self.denominator == 1


    #print(given_f.is_integral)

    #------------------------------------------

    #f = Fraction(10, 2)

    #if f.speak():
    #    print(F"All Good!")

    #---------------------------------------------

    given_dict = {'4': 'lux', '2': 'opulenta', '1': 'nebunie', '3': 'fotbal'}

    #sorted_dict = dict(sorted(given_dict.items(), key=lambda i: i[0]))
    #print(sorted_dict)

    #---------------------------------------------

    #print(sorting_data_structures(4, descending=False, sorting_dict_by='keys'))

    print(sorting_way_cool({'10', '4', '22', '101'}, descending=True))


if __name__ == '__main__':
    main()
