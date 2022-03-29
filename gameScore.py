#!/usr/bin/python
import operator

from dynamicArray import DynamicArray


class ScoreEntry:
    def __init__(self, name, score, number_of_tries):
        self._first_name, self._surname = name.split()
        self._score = score
        self._number_of_tries = number_of_tries

    @property
    def get_name(self):
        return self._first_name, self._surname

    @property
    def first_name(self):
        return self._first_name

    @property
    def surname(self):
        return self._surname

    @property
    def score(self):
        return self._score

    @property
    def number_tries(self):
        return self._number_of_tries

    def __str__(self):
        return f'Name: {self.first_name}, {self.surname}\nScore: {self.score}\nNumber of tries: {self.number_tries}'


def first_implementation():
    bogdan = ScoreEntry('Bogdan X', 127, 5)
    valentin = ScoreEntry('Valentin Soare', 140, 2)
    andreea = ScoreEntry('Andreea Petrescu', 98, 10)
    madalina = ScoreEntry('Madalina V', 156, 1)
    bobita = ScoreEntry('Bobita Bossu', 199, 1)

    new_array = DynamicArray()
    new_array.extend([bogdan, valentin, andreea, madalina, bobita])

    array_with_entries_scoring = DynamicArray()
    array_with_entries_scoring.extend([(new_array[i].get_name, new_array[i].score) for i in range(new_array.count)])

    sort_list_score = sorted(array_with_entries_scoring, key=operator.itemgetter(1), reverse=True)

    count = 1
    for name, score in sort_list_score:
        print(f'{count}. Name: {name[0]}, {name[1]}; score: {score}')
        count += 1


def main():
    first_implementation()


if __name__ == '__main__':
    main()
