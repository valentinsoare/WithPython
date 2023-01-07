#!/usr/bin/python
import random


def multi_line_statements():
    a = 10
    b = 5
    c = 2

    if a > 2 and \
            b > 3 and \
            c == 2:
        print(f"lux si opulebta")

    ax = """lux si 
        opulenta boss"""

    print(ax)


def playing_with_lambdas():
    f_1 = lambda x: x ** 2
    f_2 = lambda y: y ** 3

    print(f_1(2))
    print(f_2(3))


def emulate_do_while():
    j: int = 0
    message: str = "LUX si OPULENTA"
    as_list_of_chars: list = list(list(i) for i in message.split())

    while True:
        final_message: str = ''

        for i in as_list_of_chars:
            random.shuffle(i)
            final_message += ''.join(i) + ' '

        print(f"{final_message}")
        j += 1

        if j >= 5:
            break


def replacing_if_when_looping_with_length():
    given_list = ['boss', 'lux', 'nebunie', 'aiurea']

    for index, element in enumerate(given_list):
        print(element)
        if index == 2:
            break


def main():
    # multi_line_statements()
    #playing_with_lambdas()
    #emulate_do_while()
    replacing_if_when_looping_with_length()

if __name__ == '__main__':
    main()
