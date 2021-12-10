#!/usr/bin/python

import random
import sys


def generate_number(starting, stoping):
    rnd_number = random.randrange(starting, stoping)
    return rnd_number


def printing_messages_guess_the_number(x, y):
    print(f"\n **Guess my number between {x} and {y} with the fewest guesses: ", end="")
    number_by_user = float(input())

    return number_by_user


def compare_numbers(random_number_to_guess, strt, stp):
    number_by_user = printing_messages_guess_the_number(strt, stp)

    if number_by_user == random_number_to_guess:
        print(f" - > \033[1;33mZero in BO$$!\033[0m")
        return 1
    elif number_by_user > random_number_to_guess:
        print(f" - > \033[1;31mToo high!\033[0m")
    else:
        print(f" - > \033[1;34mToo low!\033[0m")

    return 0


def main(start, stop):
    start, stop = int(start), int(stop)
    number_of_tries = 0
    value_for_running = 0
    our_number = generate_number(start, stop + 1)

    while value_for_running == 0:
        value_for_running = compare_numbers(our_number, start, stop)
        number_of_tries += 1

    if number_of_tries <= 10:
        print(f"\n**Either you know the secret or you got lucky.")
    else:
        print(f"**You should be able to do better!")


main(sys.argv[1], sys.argv[2])
