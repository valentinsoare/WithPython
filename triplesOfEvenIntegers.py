#!/usr/bin/python

def determine_sum_triple_even_integers(list_of_integers):
    ### calculate with filter and map - lazy style
    even_integers = list(filter(lambda i: i % 2 == 0, list_of_integers))
    triples_even_integers = list(map(lambda j: j ** 3, even_integers))
    sum_of_integers = sum(triples_even_integers)

    return sum_of_integers


def determine_sum_triple_list_comprehension(list_of_integers):
    ### calculate with list comprehension - greedy style - not good
    triple_integers = [i ** 3 for i in list_of_integers if i % 2 == 0]
    sum_of_integers = sum(triple_integers)
    return sum_of_integers


def main():
    given_list = [i for i in range(1, 11)]

    ### With filter and map
    sum_of_triple_even_integers = determine_sum_triple_even_integers(given_list)

    ### With list comprehension
    sum_of_triple_even_integers = determine_sum_triple_list_comprehension(given_list)
    print(f"\n\033[1m - > Sum of triple even integers from 1 to 10: {sum_of_triple_even_integers}\033[0m", end="\n")


main()
