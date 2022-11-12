#!/usr/bin/python

import os
import random


def header(message_to_print):
    chars_to_replace = {'u': '|_|', 's': '5', 'a': '@', 'o': '0', 'e': '3'}
    processed_message = ' *#* '
    list_with_keys_for_message = chars_to_replace.keys()

    for i in message_to_print:
        if i in list_with_keys_for_message:
            processed_message += ' ' + chars_to_replace[i]
        else:
            processed_message += ' ' + i

    processed_message += ' *#* '
    length_of_message = len(processed_message)

    print(f"\n{' ' * int(length_of_message * 0.5)}{'-' * int(length_of_message + 2)}")
    print(f"{' ' * int(length_of_message * 0.5)}|{processed_message}|")
    print(f"{' ' * int(length_of_message * 0.5)}{'-' * int(length_of_message + 2)}")


def ask_how_many_times_to_play():
    error = 0
    processed_answer = ''

    while not isinstance(processed_answer, int):
        header('Game Of Craps Analysis')

        print(f"\n{' ' * 12} * Please give us how many games you want to analyse (q to quit):", end=" ")
        answer = input()

        try:
            processed_answer = int(answer)
        except ValueError:
            error = 1

        if error == 1 or processed_answer < 0:
            print(f"\n{' ' * 15} ERROR please use only integers greater than zero.")
            os.system('sleep 1')
            error = 0

    return processed_answer


def roll_the_dice():
    d_1 = random.randrange(1, 7)
    d_2 = random.randrange(1, 7)
    return d_1, d_2


def check_dices(dice_1, dice_2, number_of_roll, your_point):
    value_to_return = ''
    sum_of_dice = sum((dice_1, dice_2))

    if number_of_roll == 1:
        if sum_of_dice in [7, 11]:
            value_to_return = 'w'
        elif sum_of_dice in [2, 3, 12]:
            value_to_return = 'l'
        elif 4 <= sum_of_dice <= 6 or 8 <= sum_of_dice <= 10:
            value_to_return = sum_of_dice
    elif number_of_roll != 1:
        if sum_of_dice == your_point:
            value_to_return = 'w'
        elif sum_of_dice == 7:
            value_to_return = 'l'

    return value_to_return


def populate_dict(value_after_checking_dices, win_dict, losses_dict, roll):
    if value_after_checking_dices == 'w':
        if roll in win_dict.keys():
            win_dict[roll] += 1
        else:
            win_dict[roll] = 1
    elif value_after_checking_dices == 'l':
        if roll in losses_dict.keys():
            losses_dict[roll] += 1
        else:
            losses_dict[roll] = 1

    return win_dict, losses_dict


def calculate_statistics(wins, losses, number_of_games):
    games_resolved = {}
    resolved_games_rolls = {*wins.items(), *losses.items()}
    total_games_played_won = (sum(wins.values())/number_of_games) * 100
    total_games_played_lost = (sum(losses.values())/number_of_games) * 100

    for i, j in resolved_games_rolls:
        if i in wins.keys() and i in losses.keys():
            games_resolved[i] = wins[i] + losses[i]
        elif i in wins.keys():
            games_resolved[i] = wins[i]
        elif i in losses.keys():
            games_resolved[i] = losses[i]

    print(f"\n{' ' * 13}{'- Total of games played: '}{number_of_games:.0f}")
    print(f"{' ' * 13}{'- Games Won: '}{sum(wins.values())}, percentage: {total_games_played_won:.2f}%")
    print(f"{' ' * 13}{'- Games Lost: '}{sum(losses.values())}, percentage: {total_games_played_lost:.2f}%")
    print(f"\n{' ' * 13}{'- Percentage of wins/losses based on total number of rolls:'}")

    print(f"\n{' ' * 26}{'% Resolved':<30}{'Cumulative %'}")
    print(f"{' ' * 13}{'Rolls':<11}{'on this roll':<27}{'of games resolved'}")

    past = 0
    for i, j in sorted(games_resolved.items(), key=lambda k: k[0], reverse=False):
        print(f"{' ' * 13}{i:>5}{(j/number_of_games) * 100:>17.2f}%{past + ((j/number_of_games) * 100):>31.2f}%")
        past = past + (j/number_of_games) * 100


def main():
    count = 0
    point = ''
    wins = {}
    losses = {}

    number_of_plays = ask_how_many_times_to_play()

    while count < number_of_plays:
        roll = 1
        value_after_checking_dices = ''
        while value_after_checking_dices not in ['w', 'l']:
            dice1, dice2 = roll_the_dice()
            value_after_checking_dices = check_dices(dice1, dice2, roll, point)

            wins, losses = populate_dict(value_after_checking_dices, wins, losses, roll)

            if isinstance(value_after_checking_dices, int) and value_after_checking_dices > 0:
                point = value_after_checking_dices

            roll += 1
        count += 1

    calculate_statistics(wins, losses, number_of_plays)


if __name__ == '__main__':
    main()
