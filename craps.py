#! /usr/bin/python

import sys
import random

your_point = 0
number_of_roles = 1
var = 0


def role_the_dice():
    dice1 = random.randrange(1, 6)
    dice2 = random.randrange(1, 6)
    return dice1, dice2


def determine_win():
    side1, side2 = role_the_dice()

    summing = side1 + side2
    print(f"Player roled {side1} and {side2} = {summing}")

    if summing in (7, 11):
        print(f"You win BOSS! on the {number_of_roles + 1} role.")
        sys.exit(0)
    elif summing in (2, 3, 12):
        print(f"Craps, you lost on {number_of_roles + 1} role!")
        sys.exit(0)
    elif (4 <= summing <= 6) or (8 <= summing <= 10):
        var = 0
        your_point = summing
        print(f"Your point: {your_point}")
        return var, your_point, number_of_roles


def main():
    var, your_point, number_of_roles = determine_win()

    while var == 0:
        side1, side2 = role_the_dice()
        summing = side1 + side2

        print(f"Player roled {side1} and {side2} = {summing}")

        if your_point == summing:
            print(f"You win Chief on {number_of_roles + 1} role!!")
            var = 1
        elif summing == 7:
            print(f"You lost on {number_of_roles + 1} role, you role {summing}!!")
            var = 1

        number_of_roles += 1


main()

