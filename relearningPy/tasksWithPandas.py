#!/usr/bin/python

import numpy as np
import pandas as pd


def colorize_rows_column(given_board, type_of_print, number_of_slice):             # column
    for row in range(len(given_board)):
        for column in range(len(given_board[row])):
            if (type_of_print == 0 and row == number_of_slice) or (type_of_print == 1 and column == number_of_slice):
                print(f"\033[1;32m{given_board[row][column]}\033[0m", end=" ")
            else:
                print(f"{given_board[row][column]}", end=" ")
        print()


def colorize_1st_2nd_diag(given_board, number_diag):
    if number_diag == 1:
        for row in range(len(given_board)):
            for column in range(len(given_board[row])):
                if row == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()
    elif number_diag == 2:
        for row in range(len(given_board)):
            for column in range(len(given_board[row])):
                if ((len(given_board[row]) - 1) - row) == column:
                    print(f"\033[1;31m{given_board[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_board[row][column]}", end=" ")
            print()


def main():
    numpy_array = np.array(np.random.randint(1, 9, 9).reshape(3, 3))

    print(f"{numpy_array}\n\n")

    #colorize_rows_column(numpy_array, 1, 1)
    #colorize_1st_2nd_diag(numpy_array, 2)


if __name__ == '__main__':
    main()
