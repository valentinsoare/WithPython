#!/usr/bin/python

def is_sorted(given_sequence):
    given_list = list(map(lambda i: str(i), given_sequence))
    given_list_sorted = sorted(given_list)
    val_to_return = True

    if given_list == given_list_sorted:
        print(f"\n\033[1;32m - > Given sequence is in sorted order.\033[0m", end="\n")
    else:
        print(f"\n\033[1;31m - > Given sequence is not in sorted order.\033[0m", end="\n")
        val_to_return = False

    return val_to_return


def main():
    #given = 'abcd'
    #given = ['a', 'b', 'C', 'd']
    given = ('a', 'b', 'c', 'd')

    is_sorted(given)


main()

