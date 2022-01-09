#!/usr/bin/python

import operator
import random
import collections


def rolling_dice():
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)

    return dice_1, dice_2


def increment_dict(detect, wins, losses, rolls):
    if detect == 'lost':
        if rolls in losses:
            losses[rolls] += 1
        else:
            losses[rolls] = 1

        return losses

    elif detect == 'win':
        if rolls in wins:
            wins[rolls] += 1
        else:
            wins[rolls] = 1

        return wins


def checking_dices_determine_point(dice_1, dice_2, roll, wins, losses):
    point = 0
    calc_sum = dice_1 + dice_2
    var_for_scoring = 0

    if (calc_sum == 7 or calc_sum == 11) and roll == 1:
        wins = increment_dict('win', wins, losses, roll)
        var_for_scoring = 2
    elif calc_sum in [2, 3, 12] and roll == 1:
        losses = increment_dict('lost', wins, losses, roll)
        var_for_scoring = 1
    elif calc_sum in [4, 5, 6, 8, 9, 10]:
        point = calc_sum

    return point, var_for_scoring, wins, losses


def generate_statistics(wins, losses, number_of_games):
    games_won = sum(wins.values())
    games_lost = sum(losses.values())
    rolls_wins_losses = dict(sorted(dict(collections.Counter(wins) + collections.Counter(losses)).items(),
                                    key=operator.itemgetter(0)))

    print(f"\n\033[1mPercentage of wins: {((games_won * 100)/number_of_games):.2f}%\033[0m")
    print(f"\033[1mPercentage of losses: {((games_lost * 100)/number_of_games):.2f}%\033[0m")

    cumulative_percentage = 0

    print(f'\n\033[1m{"% Resolved":>25}{"Cumulative %":>22}\n{"Rolls"}{"on this roll":>22}{"of games resolved":>25}\033[0m')

    for roll, game in rolls_wins_losses.items():

        if roll == 1:
            calc_percentage = (game * 100) / number_of_games
            cumulative_percentage = calc_percentage
        else:
            calc_percentage = (game * 100) / number_of_games
            cumulative_percentage += calc_percentage

        print(f"{roll:>5}{calc_percentage:>21}%{cumulative_percentage:>24.2f}%")

    print()


def printing_output(wins, losses):
    wins_sorted_by_rolls = dict(sorted(wins.items(), key=operator.itemgetter(0)))
    losses_sorted_by_rolls = dict(sorted(losses.items(), key=operator.itemgetter(0)))

    print(f'\n\033[1m{"ROLLS":<10}GAMES WON\033[0m')
    for roll, games in wins_sorted_by_rolls.items():
        print(f"{roll:>5}{games:>14}")

    print(f'\n\033[1m{"ROLLS":<10}GAMES LOST\033[0m')

    for roll, games in losses_sorted_by_rolls.items():
        print(f"{roll:>5}{games:>15}")

    print()


def main():
    games = 0
    wins = {}
    losses = {}

    while games < 10_000:
        rolls = 1
        d_1, d_2 = rolling_dice()
        point, to_quit, wins, losses = checking_dices_determine_point(d_1, d_2, rolls, wins, losses)

        if to_quit == 1 or to_quit == 2:
            games += 1
            continue

        while to_quit == 0:
            d_1, d_2 = rolling_dice()
            if d_1 + d_2 == 7:
                losses = increment_dict('lost', wins, losses, rolls)
                to_quit = 1
            elif d_1 + d_2 == point:
                wins = increment_dict('win', wins, losses, rolls)
                to_quit = 2
            else:
                rolls += 1

        games += 1

    generate_statistics(wins, losses, games)
    #printing_output(wins, losses)


main()
