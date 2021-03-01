#!/usr/bin/python3

import numpy as np
import os

table_to_play = np.full(9, '.').reshape((3, 3))
table = np.full(9, 0).reshape((3, 3))
counting = 0
players = []
signs = ['X', 'O']
X = 1
O = 2


def print_table(table_to_play):
    for i in table_to_play:
        for j in i:
            print(f'{j:<8}', end='')
        print()


def presenting_board(table_to_play):
    print(f'\n\033[1;4m*Table to play:\033[0m{"":>10}')
    print_table(table_to_play)


def register_players():
    print(f'\n*We need only two players names for this game of Tic-Tac-Toe.')
    names = ['First', 'Second']
    j = 0
    while j < 2:
        print(f'\t{j + 1}.', end=' ')
        players.append(input(f"{names[j]} player name to register into the game: -> "))
        j += 1
    print(f'\n*Markings:\n-{players[0]}: {signs[0]}\n-{players[1]}: {signs[1]}')

    return players


def checking_list(list_check):
    if list_check.count(1) == 3:
        presenting_board(table_to_play)
        print(f'\nDiag with same values, {players[0]} is the winner.')
        exit()
    elif list_check.count(2) == 3:
        presenting_board(table_to_play)
        print(f'\nDiag with same values, {players[1]} is the winner.')
        exit()


def check_diags(table):
    list_check = []

    for i in range(len(table)):
        for j in range(len(table[i])):
            if j == i:
                list_check.append(table[i][j])
        checking_list(list_check)

    list_check.clear()

    for i in range(len(table) - 1, -1, -1):
        for j in range(len(table[i])):
            if j == (len(table) - 1 - i):
                list_check.append(table[i][j])

        checking_list(list_check)


def check_winner(table):
    for i in range(len(table)):
        if np.product(table[:, i]) == 1:
            presenting_board(table_to_play)
            print(f'\nColumn number {i} -> {table_to_play[:, i]}, {players[0]} is the winner.')
            exit()
        elif np.product(table[:, i]) == 8:
            presenting_board(table_to_play)
            print(f'\nColumn number {i} -> {table_to_play[:, i]}, {players[1]} is the winner.')
            exit()
        elif np.product(table[i, :]) == 1:
            presenting_board(table_to_play)
            print(f'\nRow number {i} -> {table_to_play[i, :]}, {players[0]} is the winner.')
            exit()
        elif np.product(table[i, :]) == 8:
            presenting_board(table_to_play)
            print(f'\nRow number {i} -> {table_to_play[i, :]}, {players[1]} is the winner.')
            exit()
        else:
            check_diags(table)


def player1_input(p1, repetitions):
    print(f"\n{players[0]} - > enter location, row and column, to put {signs[0]}.")
    player0_row = int(input("\t-Row: "))
    player0_col = int(input("\t-Column: "))

    if np.any(table_to_play[player0_row, player0_col] == 'O' or table_to_play[player0_row, player0_col] == 'X'):
        print(f'\n*ERROR - Square is not empty, try enter another value.')
    else:
        table_to_play[player0_row, player0_col] = signs[0]
        table[player0_row, player0_col] = 1
        repetitions += 1
        check_winner(table)
        p1 += 1

    return p1, repetitions


def player2_input(p2, repetitions):
    print(f"\n{players[1]} - > enter location, row and column, to put {signs[1]}.")
    player1_row = int(input("\t-Row: "))
    player1_col = int(input("\t-Column: "))

    if np.any(table_to_play[player1_row, player1_col] == 'O' or table_to_play[player1_row, player1_col] == 'X'):
        print(f'*ERROR - Square is not empty, try enter another value.')
    else:
        table_to_play[player1_row, player1_col] = signs[1]
        table[player1_row, player1_col] = 2
        repetitions += 1
        check_winner(table)
        p2 += 1

    return p2, repetitions


def put_values(repetitions):
    p1 = 0
    p2 = 0

    while True:
        os.system('clear')
        presenting_board(table_to_play)
        if p1 == 0 and repetitions <= 8:
            p1, repetitions = player1_input(p1, repetitions)
        elif p2 == 0 and repetitions <= 8:
            p2, repetitions = player2_input(p2, repetitions)
        else:
            break

    return repetitions


def main():
    j = 0
    presenting_board(table_to_play)
    register_players()
    repetitions = 0

    while j < 9:
        repetitions = put_values(repetitions)
        j += 1

    print(f'\n*We have a draw.')


main()
