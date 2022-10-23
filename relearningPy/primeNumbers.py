#!/usr/bin/python

import math


def determine_if_prime(given_number):
    if given_number <= 1:
        return False
    elif given_number <= 3:
        return True
    elif given_number % 2 == 0 or given_number % 3 == 0:
        return False

    for i in range(2, int(math.sqrt(given_number))):
        if given_number % i == 0:
            return False

    return True


def check_how_many_numbers(qty):
    list_with_prime_numbers = list(filter(determine_if_prime, range(1, qty)))
    return list_with_prime_numbers


def main():
    list_with_primes = check_how_many_numbers(23)
    print(list_with_primes)


if __name__ == '__main__':
    main()
