#!/usr/bin/python

import numpy as np


def main():
    initial_array = np.array(['#', '*'])
    given_array = np.tile(initial_array, 4)
    given_array_flipped = np.flip(given_array, axis=0)
    x = 0

    print(f'\n\033[1m{"CHECKER":>23}\n{"BOARD":>22}\033[0m\n')

    while x < 4:
        print(f'{" ":>12}', end="")
        for i in given_array:
            print(f"{i}", end=" ")

        print(f'\n{" ":>12}', end="")
        for j in given_array_flipped:
            print(f"{j}", end=" ")

        print()

        x += 1

    print("\n")


main()
