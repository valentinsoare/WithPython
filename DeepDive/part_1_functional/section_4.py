#!/usr/bin/python

import math
import string
import decimal
from time import time
from fractions import Fraction
from itertools import repeat

# a = b * (a // b) + (a % b) - formula


def integers_and_ordereddict():
    my_list = ['lux', 'opulenta', 'nebunie', 'home']
    names = ['andrei', 'vali', 'gabriela', 'adriana']

    my_dict = dict(zip(names, my_list))
    print(my_dict)


def another_function():
    a = int(10.9)
    print(a)

    b = int(True)
    print(b)

    c = int('10')
    print(c)

    d = int('dde', base=16)
    print(d)

    e = int('100101', base=2)
    print(e)

    f = int('osamaducacasasavadcenaibafac', base=36)
    print(f)

    print(f"{bin(1987).lstrip('0b')}")


def converting_integers_base(number, base):
    # n = number
    # b = base
    #formula = n = b * (n // b) + (n % b) - > n = (n // b) * b + (n % b)

    # from 232 base 10 to 232 in base 5
    # n = 232, b = 5

    if number < 0 or base < 2:
        raise ValueError('For now please use only base greater or equal to 2 and number should be a positive one!')
    elif number == 0:
        return [0]

    digits: list = []

    while number > 0:
        #module = number % base
        #number = number // base
        number, module = divmod(number, base)
        digits.insert(0, module)

    return digits


def encoding(number, base):
    mapping_schema = list(string.digits + string.ascii_uppercase)[0: base]

    number_after_translating = ''.join(mapping_schema[i] for i in number)
    return number_after_translating


def fractions_my():
    x = Fraction(22, 8)
    print(x.denominator)

    y = Fraction(math.pi)

    print(y.limit_denominator(100))
    print(y.limit_denominator(10))

    x = Fraction(7, 11)
    y = Fraction(2, 4)

    ay = decimal.Decimal(float(x))
    print(ay)


def floats_my():
    #ax = random.randint(1000000, 9999999, 1)
    print(bin(11))


def numbers_are_equal_with_only_absolute_tolerance(first_number, second_number, range):
    if range > 0:
        return math.fabs((first_number - second_number)) < range
    else:
        raise ValueError('Range value should be greater than zero!')


def numbers_are_equal_relative_tolerance(first_number, second_number, relative_tolerance, absolute_tolerance):
    if relative_tolerance > 0 and absolute_tolerance > 0:
        tolerance = max((max(math.fabs(first_number), math.fabs(second_number)) * relative_tolerance), absolute_tolerance)
        return math.fabs(first_number - second_number) < tolerance
    else:
        raise ValueError('Relative tolerance value should be greater than zero!')


def compare_numbers():
    #ax = numbers_are_equal_with_only_absolute_tolerance(0.1 + 0.1 + 0.1, 0.3, 0.000000000000023)
    #print(ax)

    ay = numbers_are_equal_relative_tolerance(0.3 + 0.3 + 0.3, 0.9, 0.0000000000001, 0.000000000000123)
    print(ay)


def rounding():
    given_number = 10.723

    #ax = math.floor(given_number)
    ##ay = math.ceil(given_number)
    #az = math.trunc(given_number)
    #at = round(given_number, 1)
    #print(at)
    x = math.copysign(10, -2)
    print(x)


def always_rounding_up_ties(given_number):
    # x = sign(x) * int(abs(x)  0.5)
    #sign = 1
    #if given_number * -1 > 0:
    #    sign = -1

    value_after_rounding = math.copysign(1, given_number) * int(math.fabs(given_number) + 0.5)
    print(value_after_rounding)


def decimal_context():
    ax = decimal.getcontext()
    print(ax.rounding)
    print(ax.prec)
    print(decimal.getcontext())
    with decimal.localcontext() as ctx:
        ctx.prec = 6
        ctx.rounding = decimal.ROUND_HALF_UP
        print(decimal.getcontext())


def creating_decimals():
    given_number = decimal.Decimal((1, (3, 1, 4, 5), -2))
    print(given_number)

    if (decimal.Decimal('0.1') + decimal.Decimal('0.1') + decimal.Decimal('0.1')) == decimal.Decimal('0.3'):
        print(f'AAaaaaaaaa')

    if decimal.Decimal('0.1') != decimal.Decimal(0.1):
        print(f'too good to be true!!')


def play_with_booleans():
    if issubclass(bool, int):
        print(f'True')

    print(1 + True)


def check_values():
    ax = 'a'
    ay = 'y'

    if not (ax and ay):
        print(f'Lux si opulenta')


    my_name = 'Valentin'
    # here we checked if my_name is True (is not None or empty string '')
    if my_name and my_name[0] in string.ascii_uppercase:
        print(f'Good To Go!')

    x = ''
    y = 2

    if x or y:
        print(f'Este nebunie')

    a = 'abc'
    b = ''
    c = None
    d = 'no char'

    a = a[0] or d
    b = b or d
    c = c or d

    given_dict = {'first': 'lux', 'second': 'nebunie', 'third': 'opulenta'}

    ax = dict((i, j) for i, j in given_dict.items() if j == 'nebunie')
    print(ax)


def main():
    #integers_and_ordereddict()
    #another_function()

    #------------------------
    #digits_after_conversion = converting_integers_base(1987, 32)
    #converted_number = encoding(digits_after_conversion, 32)

    #print(f"200 in base 32 = {converted_number}")
    #-------------------------e

    #fractions_my()

    #floats_my()

    #-------------------------

    #compare_numbers()
    #ax = {'ceva', 'lux', 'opulenta'}

    #-----------------------------

    #rounding()
    #always_rounding_up_ties(-1.52)

    #------------------------------

    #decimal_context()
    #creating_decimals()

    #---------------------------------

    #play_with_booleans()
    check_values()


if __name__ == '__main__':
    main()
