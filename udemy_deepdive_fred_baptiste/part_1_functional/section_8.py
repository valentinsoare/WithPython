#!/usr/bin/python

from collections import namedtuple


def working_with_simple_tuples():
    cities: list = []

    def romanian_cities(adding_city=None):
        nonlocal cities

        if adding_city:
            cities.append(adding_city)

        return cities

    romanian_cities.add_city = romanian_cities
    romanian_cities.print_population = cities

    return romanian_cities


def main():
    cities = working_with_simple_tuples()
    cities.add_city(adding_city=('Craiova', 'RO', 400_000))
    cities.add_city(adding_city=('Iasi', 'RO', 700_000))
    cities.add_city(adding_city=('New York', 'US', 4_000_000))

    print(cities.print_population)


if __name__ == '__main__':
    main()
