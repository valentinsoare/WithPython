#!/usr/bin/python

import os
import sys
import time
import numpy as np


def catch_names():
    name_1 = input("\n\033[1m - > Name for the first player: \033[0m")
    name_2 = input("\033[1m - > Name of the second player: \033[0m")

    return name_1, name_2


def draw_board(name_1, name_2, to_generate, *args):

    if to_generate == 1:
        tictactoe_board = np.array(np.full(9, "[   ]").reshape(3, 3))
    else:
        tictactoe_board = np.array(args[0])

    print(f'\n\033[1;32m{"Tic Tac Toe":>24}\n{name_1[0].capitalize():>16} vs {name_2[0].capitalize()}\033[0m', end="\n\n")

    for row in range(len(tictactoe_board)):
        for element in range(len(tictactoe_board[row])):
            if element == 0:
                print(f"\033[1m{tictactoe_board[row][element]:>15}\033[0m", end=" ")
            else:
                print(f"\033[1m{tictactoe_board[row][element]}\033[0m", end=" ")
        print()

    if to_generate == 1:
        return tictactoe_board


def who_goes(name_1, name_2):
    goes_first = 'X'
    goes_second = 'X'
    tictactoe_given_board = ''

    while goes_first.capitalize() not in [name_1.capitalize(), name_2.capitalize()]:
        tictactoe_given_board = draw_board(name_1, name_2, 1)
        print(f"\n\033[1m - > Who goes first, {name_1.capitalize()} or {name_2.capitalize()} "
              f"? (q to quit) - > ", end=" ")
        goes_first = input()

        if goes_first.capitalize() not in [name_1.capitalize(), name_2.capitalize(), "Q"]:
            print(f"\n\033[31m ERROR, you need to try again!!", end="\n")
            time.sleep(1)
            os.system('clear')
        elif goes_first[0].capitalize() == 'Q':
            print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
            sys.exit(1)
        elif goes_first.capitalize() != name_1.capitalize():
            goes_second = name_1.capitalize()
        elif goes_first.capitalize() != name_2.capitalize():
            goes_second = name_2.capitalize()

    return goes_first, goes_second, tictactoe_given_board


def board_digits_populate(to_generate, *args):
    if to_generate == 1:
        digits_board = np.array(np.full(9, 100).reshape(3, 3), dtype=int)
        return digits_board
    else:
        board_start, row, column, player_1, player_2, choose_player = args
        digits_board = np.array(board_start.reshape(3, 3))

    if digits_board[row][column] == 100 and choose_player == 1:
        digits_board[row][column] = 1
    elif digits_board[row][column] == 100 and choose_player == 2:
        digits_board[row][column] = 2

    return digits_board


def board_populate_array_signs(board_with_all_digits, tic_board):
    for row in range(len(board_with_all_digits)):
        for column in range(len(board_with_all_digits[row])):
            if board_with_all_digits[row][column] == 1:
                tic_board[row][column] = '[ X ]'
            elif board_with_all_digits[row][column] == 2:
                tic_board[row][column] = '[ 0 ]'

    return tic_board


def select_row_column(what_to_select):
    if what_to_select == 1:
        print(f"\033[1m - > Row [1-3]: \033[0m", end="")
    else:
        print(f"\033[1m - > Column [1-3]: \033[0m", end="")

    element = input()

    if element in ['1', '2', '3']:
        element = (int(element) - 1)
    else:
        if element[0].capitalize() == "Q":
            print(f"\n\033[31m Quitting.....\033[0m\n\n", end=" ")
            sys.exit(1)

    return element


def ask_for_row_column(name_1, name_2, board_to_print, first_chooser):
    while True:
        draw_board(name_1, name_2, 0, board_to_print)

        if first_chooser == 1:
            print(f'\n\n\033[1m PLAYER: {name_1} will put an "X" (q to quit).\n{"-" * 60:>16}\033[0m')
        else:
            print(f'\n\n\033[1m PLAYER: {name_2} will mark the spot with "0" (q to quit).\n{"-" * 60:>16}\033[0m')

        row = select_row_column(1)
        if row not in [0, 1, 2]:
            print(f"\n\033[31m ERROR please select again! \033[0m\n")
            time.sleep(0.5)
            os.system('clear')
            continue

        column = select_row_column(2)
        if column not in [0, 1, 2]:
            print(f"\n\033[31m ERROR please select again! \033[0m\n")
            time.sleep(0.5)
            os.system('clear')
        else:
            return row, column


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
    os.system('clear')
    name_1, name_2 = catch_names()
    digits_board_start = board_digits_populate(1)
    goes_first, goes_second, tictactoe_board = who_goes(name_1, name_2)
    print(f'\n\033[1m - > {goes_first} will choose first and then {goes_second}. {name_1.capitalize()} is using "X" and {name_2.capitalize()} is with "0" \033[0m')
    os.system('clear')
    row, column = ask_for_row_column(name_1, name_2, tictactoe_board, 2)
    digits_board_start = board_digits_populate(0, digits_board_start, row, column, name_1, name_2, 2)

    tictactoe_board = board_populate_array_signs(digits_board_start, tictactoe_board)
    draw_board(name_1, name_2, 0, tictactoe_board)


main()

