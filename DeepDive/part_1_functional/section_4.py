#!/usr/bin/python


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

    digits = []

    while number > 0:
        module = number % base
        number = number // base
        digits.insert(0, module)

    print(digits)


def main():
    #integers_and_ordereddict()
    #another_function()
    converting_integers_base(232, 5)


if __name__ == '__main__':
    main()
