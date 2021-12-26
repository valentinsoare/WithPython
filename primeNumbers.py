#!/usr/bin/python

given_list = [i for i in range(2, 1001)]


def check_if_prime(given_number):
    if given_number <= 1:
        return False
    elif given_number <= 3:
        return True
    elif given_number % 2 == 0 or given_number % 3 == 0:
        return False

    for i in range(5, (int(given_number ** 0.5) + 1)):
        if i % given_number == 0:
            return False

    return given_number


def extract_prime_numbers_from_list(given_list):
    prime_numbers = list(filter(check_if_prime, given_list))
    print(f"\n - > Prime numbers from the given list: {prime_numbers}")


def main():
    extract_prime_numbers_from_list(given_list)


main()
