#!/usr/bin/python

import random


def print_header(given_message):
    message_length = len(given_message)
    print(f"\n{' ' * 12}{' ' * (message_length // 2)}{given_message}")
    print(f"{' ' * 12}{'-' * (message_length * 2)}")


def roll_the_dice(number_of_times):
    count = 0
    #random.seed(32) - > with seed we can have the same values on random generator.

    while count < number_of_times:
        face_to_return = random.randrange(1, 7, 1)
        count += 1

        yield face_to_return


def count_faces(faces_number):
    list_with_counters = []

    for i in range(1, 7):
        if i in faces_number:
            list_with_counters.append((i, faces_number.count(i)))
        else:
            list_with_counters.append((i, 0))

    return list_with_counters


def print_counters(list_counters):
    print(f"\n{' ' * 14}{'Face'}{' ' * 14}{'Freq'}")
    for i in list_counters:
        face, count = i[0], i[1]
        print(f"{' ' * 14}{face}{' ' * 17}{count}")


def main():
    print_header('Roll the Dice 6 million times')

    given_list = list(roll_the_dice(6_000_000))
    list_with_counters = count_faces(given_list)

    print_counters(list_with_counters)


if __name__ == "__main__":
    main()

