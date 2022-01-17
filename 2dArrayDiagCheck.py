#!/usr/bin/python

import numpy as np


def check_diags_winner(given_2d_array, diag_type):
    count_diag = []
    if diag_type == 2:
        given_2d_array = np.flip(given_2d_array, axis=1)

    for row in range(len(given_2d_array)):
        for column in range(len(given_2d_array[row])):
            if column == row:
                count_diag.append(given_2d_array[row][column])

    if count_diag.count(1) == 3:
        return 'f'
    if count_diag.count(2) == 3:
        return 's'


def main():
    given_matrix = np.array([[2, 100, 1], [100, 1, 100], [1, 100, 2]])
    print(f"\n{given_matrix}", end="\n")

    print(f"\nresult: {check_diags_winner(given_matrix, 2)}")

main()