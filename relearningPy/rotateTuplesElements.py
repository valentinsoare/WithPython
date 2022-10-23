#!/usr/bin/python

import time


def rotate_three_elements_tuple(first, second, third):
    third, second = second, third
    second, first = first, second

    return first, second, third


def printing_example():
    count = 0
    name = 'Valentin'
    surname = 'Soare'
    age = 34

    print(f"\n{' ' * 12}**Rotating Arguments in a tuple**\n")

    while count < 3:
        name, surname, age = rotate_three_elements_tuple(name, surname, age)

        print(f"{' ' * 6}{name}, {surname}, {age}")
        time.sleep(1)
        count += 1


def main():
    printing_example()


if __name__ == '__main__':
    main()
