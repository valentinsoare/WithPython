#!/usr/bin/python

import random


def h_printing(our_message):
    length_of_message = len(our_message)
    banner = f"{' ' * 12}|{' ' * (length_of_message // 2)}{our_message}{' ' * (length_of_message // 2)}|"

    print(f"\n{' ' * 12}{'-' * (len(banner) - 12)}")
    print(banner)
    print(f"{' ' * 12}{'-' * (len(banner) - 12)}")


def roll_the_two_dices():
    dice_1 = random.randrange(1, 7)
    dice_2 = random.randrange(1, 7)

    return (dice_1, dice_2)


def check_dices():
    d1, d2 = roll_the_two_dices()
    sum_of_dice = sum((d1, d2))
    nr_rolls = 1

    if sum_of_dice in [7, 11] and nr_rolls == 1:
        print(f"\n{' ' * 15}You have {d1} + {d2} = {sum_of_dice} on the {nr_rolls} roll.")
        print(f"{' ' * 19}Win!!\n")
        exit(0)
    elif sum_of_dice in [2, 3, 12] and nr_rolls == 1:
        print(f"\n{' ' * 15}Not so lucky, {d1} + {d2} = {sum_of_dice} on the {nr_rolls} roll.")
        print(f"{' ' * 19}Lost!!\n")
        exit(0)
    else:
        print(f"\n{' ' * 12}You roll {d1} + {d2} = {sum_of_dice} on {nr_rolls} try. {d1 + d2} bill become your point.")

        return sum_of_dice, nr_rolls


def main():
    for_exit = 0

    h_printing('Game of Chance - Craps')
    point, number_of_rolls = check_dices()

    while for_exit == 0:
        number_of_rolls += 1
        dc1, dc2 = roll_the_two_dices()
        sum_of_dices = sum((dc1, dc2))

        if sum_of_dices == point:
            print(f"{' ' * 15}Let's see {dc1} + {dc2} = {sum_of_dices}. You made your point on {number_of_rolls} roll. Win!!\n")
            for_exit = 1
        elif sum_of_dices == 7:
            print(f"{' ' * 15}Bad luck, {dc1} + {dc2} = {sum_of_dices}. You lost on {number_of_rolls} roll!!\n")
            for_exit = 1
        else:
            print(f"{' ' * 12}[{number_of_rolls}] We have {dc1} + {dc2} = {sum_of_dices}. Let's continue....")


if __name__ == "__main__":
    main()
