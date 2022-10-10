#!/usr/bin/python

import os


def printing_cool_header(size, message):
    if size % 2 == 0:
        print(f"\n{' '*3}\033[1;31m ERROR \033[0mYou need to use only odd numbers as size for header\n")
        os.system('sleep 1')
        exit(1)

    length_message = len(message)

    print()
    for i in range(size):
        print(f"{' ' * 20}", end="")

        for j in range(i+1):
            print(f"*", end="")

        if i == (size // 2):
            print(f"    {message} ", end="")
            print(f"{' ' * (size - i + 1)}", end="")
            print(f"{'*' * (i + 1)}", end="")
        else:
            print(f"{' ' * (size - i + 1)} ", end="")
            print(f"{' ' * length_message}", end="")
            print(f"{' ' * (size - i + 1)}", end="")
            print(f"{'*' * (i+1)}", end="")

        print()


def calc_pythagorean(limit):
    list_with_values_pyth = []

    for i in range(1, limit + 1):
        for j in range(i+1, limit + 1):
            for k in range(j + 1, limit + 1):
                calc = i ** 2 + j ** 2
                hyp = k ** 2

                if calc == hyp:
                    list_with_values_pyth.append((i, j, k))

    return list_with_values_pyth


def set_a_limit():
    for_error = 0
    input_after_processing = ''

    while True:
        printing_cool_header(5, 'Pythagorean Triples')
        print(f"\n ** Please give us a limit of those pythagorean triples before we square them:", end=" ")
        answer = input()

        try:
            input_after_processing = int(answer)
        except ValueError:
            for_error = 1

        if for_error == 1 or input_after_processing < 0:
            print(f"\n{' ' * 3}\033[1;31m ERROR \033[0m You need to use only integers larger than 0.")
            os.system('sleep 1')
            os.system('clear')
        else:
            return input_after_processing


def print_values_pyth(given_list):
    print(f"\n{' ' * 11} Pythagorean triples")
    print(f" {'-' * 40}")

    for i in given_list:
        print(f" {i[0]} + {i[1]} = {i[2]} - > {i[0] ** 2} + {i[1] ** 2} = {i[2] ** 2}")


def main():
    given_limit = set_a_limit()
    values_processed = calc_pythagorean(given_limit)

    print_values_pyth(values_processed)


if __name__ == '__main__':
    main()
