#!/usr/bin/python3

import random
import operator


def initialize_deck(given_option):

    type_of_cards = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
    suit_of_cards = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    combined = [(i, j) for i in type_of_cards for j in suit_of_cards]
    deck = []

    if given_option == 1:
        random.shuffle(combined)
        length_combined = len(combined)
        for i in range(length_combined):
            deck.append(combined[i])
        return deck

    elif given_option == 0:
        return type_of_cards


def print_or_hand(given_option, deck):

    if given_option == 1:
        length_deck = len(deck)
        for i in range(0, length_deck):
            print(f'{deck[i][0]} of {deck[i][1]}', end='  ')
            if (i+1) % 4 == 0:
                print()

    elif given_option == 2:
        five_cards = []
        count = 0
        numbers_list = []

        while True:
            nr = random.randrange(len(deck))
            if nr not in numbers_list:
                numbers_list.append(nr)
                hand = (deck[nr][0], deck[nr][1])
                five_cards.append(hand)
                count += 1

            if count == 5:
                break

        return five_cards


def is_a_one_pair_v2(given_hand):
    given_hand = sorted(given_hand, key=operator.itemgetter(0))
    processed_list = [i[0] for i in given_hand]
    same_cards = []
    rtrn = False
    length_pocessed_list = len(processed_list)
    for i in range(length_pocessed_list):
        value = processed_list.count(processed_list[i])
        if value == 2:
            same_cards.append((given_hand[i][0], given_hand[i][1]))
            rtrn = True

    return rtrn


def is_a_two_pair_v2(given_hand):
    given_hand = sorted(given_hand, key=operator.itemgetter(0))
    processed_list = [i[0] for i in given_hand]
    same_cards = []
    rtrn = False
    count = 0

    length_pocessed_list = len(processed_list)
    for i in range(length_pocessed_list):
        value = processed_list.count(processed_list[i])
        if value == 2:
            same_cards.append((given_hand[i][0], given_hand[i][1]))
            count += 1

    if count == 4:
        rtrn = True

    return rtrn


def is_a_three_of_a_kind_v2(given_hand):
    given_hand = sorted(given_hand, key=operator.itemgetter(0))
    processed_list = [i[0] for i in given_hand]
    count = 0
    same_cards = []
    rtrn = False

    length_processed_list = len(processed_list)
    for i in range(length_processed_list):
        value = processed_list.count(processed_list[i])
        if value == 3:
            same_cards.append((given_hand[i][0], given_hand[i][1]))
            count += 1

    if count == 3:
        rtrn = True

    return rtrn


def is_a_flush(given_hand):
    given_hand = sorted(given_hand, key=operator.itemgetter(0))
    rtrn = False

    working_list = [j for i in given_hand for j in i]
    length_given_hand = len(given_hand)
    for i in range(length_given_hand):
        value = working_list.count(given_hand[i][1])
        if value == 5:
            rtrn = True
            break

    return rtrn


def is_a_straight(given_hand):
    type_of_cards = list(initialize_deck(0))
    ranks = list(range(1, 14))
    length_given_hand = len(given_hand)
    given_list = [given_hand[i][0] for i in range(length_given_hand)]
    cards_combined = list(map(lambda x, y: (x, y), ranks, type_of_cards))
    values_we_have = []
    rtrn = False
    count = 0

    length_cards_combined = len(cards_combined)
    length_given_list = len(given_list)
    for i in range(length_cards_combined):
        for j in range(length_given_list):
            if cards_combined[i][1] == given_list[j]:
                values_we_have.append(cards_combined[i][0])

    values_sorted = sorted(values_we_have)

    end = 0
    length_values_sorted = len(values_sorted)
    for i in range(length_values_sorted - 1):
        if values_sorted[i] == 1:
            end = 14
        elif values_sorted[i] + 2 == end:
            count += 1

        if values_sorted[i] + 1 == values_sorted[i+1]:
            count += 1

    if count == 4:
        rtrn = True

    return rtrn


def is_a_full_house(given_hand):
    rtrn = False

    if is_a_three_of_a_kind_v2(given_hand) and is_a_one_pair_v2(given_hand):
        rtrn = True

    return rtrn


def is_a_four_of_a_kind(given_hand):
    length_given_hand = len(given_hand)
    given_list = [given_hand[i][0] for i in range(length_given_hand)]
    rtrn = False

    length_given_list = len(given_list)
    for i in range(length_given_list):
        value = given_list.count(given_list[i])
        if value == 4:
            rtrn = True
            break

    return rtrn


def is_a_straight_flush(given_hand):
    length_given_hand = len(given_hand)
    given_list = [given_hand[i][1] for i in range(length_given_hand)]
    rtrn = False

    value = given_list.count(given_list[0])

    if value == 5:
        rtrn = True

    return rtrn


def playing(cards):
    first_hand, second_hand = cards
    winning_hands = [('is_a_straight_flush(hand)', '- > straight flush'), ('is_a_full_house(hand)', '- > full house'),
                     ('is_a_four_of_a_kind(hand)', '- > four of a kind'),
                     ('is_a_flush(hand)', '- > flush'), ('is_a_straight(hand)', '- > straight'),
                     ('is_a_three_of_a_kind_v2(hand)', '- > three of a kind'),
                     ('is_a_two_pair_v2(hand)', '- > two pair'), ('is_a_one_pair_v2(hand)', '- > one pair')]

    print(f'\nFirst hand: {first_hand} \nSecond hand: {second_hand}', end='\n\n')

    length_cards = len(cards)
    for i in range(length_cards):
        hand = cards[i]
        for value, message in winning_hands:
            if eval(value):
                print(f'{hand} {message}')
                break


def main():
    first = print_or_hand(2, initialize_deck(1))
    second = print_or_hand(2, initialize_deck(1))
    cards = [first, second]
    playing(cards)


main()
