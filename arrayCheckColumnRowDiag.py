#!/usr/bin/python

import numpy as np

def check_diags_winner(given_2d_array, diag_type):
    count_diag = []
    player = ''

    if diag_type == 2:
        given_2d_array = np.flip(given_2d_array, axis=1)

    for row in range(len(given_2d_array)):
        for column in range(len(given_2d_array[row])):
            if column == row:
                count_diag.append(given_2d_array[row][column])

    if count_diag.count(1) == 3:
        player = 'first'
    if count_diag.count(2) == 3:
        player = 'second'

    return player


def check_rows_columns_winner(given_array, for_row):
    winner_row = []
    player = ''

    if for_row == 0:
        given_array = given_array.transpose()

    for row in range(len(given_array)):
        if list(given_array[row]).count(1) == 3:
            winner_row = row
            player = 'first'
        elif list(given_array[row]).count(2) == 3:
            winner_row = row
            player = 'second'

    return winner_row, player


def colorize_rows_column(given_array, element, to_choose):
    for row in range(len(given_array)):
        for column in range(len(given_array[row])):
            if to_choose == 0 and element == column:
                print(f"\033[1;32m{given_array[row][column]}\033[0m", end=" ")
            elif to_choose == 1 and element == row:
                print(f"\033[1;34m{given_array[row][column]}\033[0m", end=" ")
            else:
                print(f"\033[1m{given_array[row][column]}\033[0m", end=" ")
        print()


def colorize_diags(given_array, diag_type):

    if diag_type == 1:

        for row in range(len(given_array)):
            for column in range(len(given_array[row])):
                if row == column:
                    print(f"\033[1;31m{given_array[row][column]}\033[0m", end=" ")
                else:
                    print(f"{given_array[row][column]}", end=" ")
            print()

    elif diag_type == 2:

        for row in range(len(given_array)):
            for column in range(len(given_array)):
                if row == (len(given_array) - column - 1):
                    print(f"\033[1;31m{given_array[row][column]}\033[0m", end=" ")
                else:
                    print(f"\033[1m{given_array[row][column]}\033[0m", end=" ")
            print()


def main():
    given_matrix = np.array([[2, 4, 1], [1, 1, 1], [2, 2, 1]])
    print(f"\n{given_matrix}", end="\n")

    column, player_column = check_rows_columns_winner(given_matrix, 0)

    if column and player_column:
        print(f"\nWinner column {column} by {player_column} player.")
        colorize_rows_column(given_matrix, 2, 0)

    #row, player_row = check_rows_columns_winner(given_matrix, 1)

    #if row and player_row:
    #    print(f"\nWinner row: {row} by {player_row} player.")

    #colorize_rows_column(given_matrix, 2, 0)

    #colorize_diags(given_matrix, 1)

main()