#!/usr/bin/python

import os
import numpy as np

one_second = 'sleep 1'


def printing_header(message_for_header, type_of_game):
    processed_message = ' * '
    what_type = ' ** '
    processed_message += ' '.join(i for i in message_for_header)
    what_type += ' '.join(j for j in type_of_game)
    processed_message += ' * '
    what_type += ' ** '

    length_first_message = len(processed_message)
    length_second_message = len(what_type)

    print(f"\n{' ' * length_second_message}{'-' * length_second_message}")
    print(f"{' ' * (length_second_message + (length_second_message - length_first_message) // 2)}{processed_message}")
    print(f"{' ' * length_second_message}{what_type}")
    print(f"{' ' * length_second_message}{'-' * length_second_message}")

    return length_first_message, length_second_message


def initialize_empty_board(rows=3, columns=3):
    empty_board = np.full((rows, columns), ' [   ] ')
    board_to_use_for_analyse = np.full((rows, columns), 100)
    return empty_board, board_to_use_for_analyse


def printing_tictactoe_board(game_board, length_second_message):

    print(f"\n{' ' * (length_second_message + (length_second_message // 4) - 2)}", end="")

    for row in range(len(game_board)):
        for column in range(len(game_board[row])):
            print(f"{game_board[row, column]}", end=" ")
        print(f"\n{' ' * (length_second_message + (length_second_message // 4) - 2)}", end="")


def writing_to_boards(row, column, sign, board_game, board_to_determine):
    if sign == 1:
        board_game[row - 1, column - 1] = ' [ X ] '
        board_to_determine[row - 1, column - 1] = 1
    else:
        board_game[row - 1, column - 1] = ' [ 0 ] '
        board_to_determine[row - 1, column - 1] = 0

    return board_game, board_to_determine


def check_if_quit(answer, second_message_length, message_to_use):
    if answer.isspace() or answer == '':
        print(f"\n{' ' * second_message_length} {message_to_use}")
        os.system(one_second)
        return True
    elif answer.lower()[0] == 'q':
        print(f"\n{' ' * second_message_length} Exiting....")
        os.system(one_second)
        exit(1)


def check_if_int_or_float(processed_answer, second_message_length, message_to_use):
    if isinstance(processed_answer, int) or isinstance(processed_answer, float):
        print(f"\n{' ' * second_message_length} {message_to_use}")
        os.system(one_second)


def names(game_board):
    count = 0
    name_of_players = []
    processed_answer = 'default'
    order = {'1': 'first', '2': 'second'}

    while count < 2:
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)

        print(f"\n{' ' * (second_message_length // 2 + 8)} {list(order.keys())[count]}. Tell me the name of the {list(order.values())[count]} player (q to quit):", end=" ")
        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only strings or strings with integers/floats."):
            continue

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                name_of_players.append(answer.capitalize().strip())
                count += 1

        check_if_int_or_float(processed_answer, second_message_length, "ERROR - please use only strings or strings with integers/floats.")

    return name_of_players


def who_will_start_first(list_of_players, game_board):
    processed_answer = 'default'
    one_second = 'sleep 1'
    order_of_start = []
    count = 0
    list_ways = ['first', 'second']

    while count < 2:
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)

        print(f"\n{' ' * (second_message_length // 2 + 8)} * Please tell me who will start {list_ways[count]}", end=" ")
        print(f"{list_of_players} (q to quit)", end=": ")
        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only one of those two names."):
            continue

        try:
            processed_answer = int(answer)
        except ValueError:
            try:
                processed_answer = float(answer)
            except ValueError:
                answer = answer.capitalize().strip()
                if answer not in list_of_players:
                    print(f"\n{' ' * second_message_length} ERROR - please use only those names from the list.")
                    os.system(one_second)
                else:
                    order_of_start.append(answer)
                    list_of_players.remove(answer)
                    count += 1

        check_if_int_or_float(processed_answer, second_message_length, "ERROR - please use only those names from the list.")

    return order_of_start


def choose_sign(list_with_players_in_order, game_board):
    list_with_sign = ['X', '0']
    players_signs = {}
    count = 0

    while len(players_signs) < 2:
        os.system('clear')
        first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
        printing_tictactoe_board(game_board, second_message_length)
        name_of_player = list_with_players_in_order[0]

        print(f"\n{' ' * (second_message_length // 2 + 8)} * {count + 1}. {name_of_player}, what do you want to play with, {list_with_sign} (q to quit):", end=" ")

        answer = input().upper()

        if check_if_quit(answer, second_message_length, "ERROR - please use only X or 0."):
            continue
        elif answer not in list_with_sign:
            print(f"\n{' ' * second_message_length} ERROR - please use only X or 0.")
            os.system(one_second)
        else:
            count += 1
            list_with_players_in_order.remove(name_of_player)
            players_signs[name_of_player] = answer
            list_with_sign.remove(answer)

    players_values_for_board = {}

    for name, value in players_signs.items():
        if value == 'X':
            players_values_for_board[name] = 1
        else:
            players_values_for_board[name] = 0

    return players_signs, players_values_for_board


def print_board(players_order_signs, game_board, if_starting=0):
    os.system('clear')
    first_message_length, second_message_length = printing_header('2D Tic-Tac-Toe', 'human vs human')
    printing_tictactoe_board(game_board, second_message_length)

    if if_starting == 1:
        print(f"\n{' ' * second_message_length} {'[ 1. ]':>7} {list(players_order_signs.keys())[0]} will move first with {list(players_order_signs.values())[0]}")
        print(f"{' ' * second_message_length} {'[ 2. ]':>7} Then {list(players_order_signs.keys())[1]} with {list(players_order_signs.values())[1]}")

        os.system(one_second)
        print(f"\n{' ' * second_message_length} Let's START the game....")
        os.system(one_second)


def main():
    game_board, board_to_use_to_check_winner = initialize_empty_board(3, 3)
    player_names = names(game_board)
    starting_order = who_will_start_first(player_names, game_board)
    players_with_signs, players_with_values = choose_sign(starting_order, game_board)

    print_board(players_with_signs, game_board, 1)    # before starting players moves


if __name__ == '__main__':
    main()

