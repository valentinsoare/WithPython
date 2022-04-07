#!/usr/bin/python

import operator
from arrayDynamic import ArrayDynamic


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

    @score.setter
    def score(self, score):
        self._score = score

    @property
    def number_tries(self):
        return self._number_of_tries

    def __str__(self):
        return f'Name: {self.first_name}, {self.surname}\nScore: {self.score}\nNumber of tries: {self.number_tries}'


class Scoreboard:
    def __init__(self, capacity):
        self._count = 0
        self._capacity = capacity
        self._board = [None] * capacity

    def __getitem__(self, item):
        return self._board[item]

    def __str__(self):
        return '\n'.join(f'{self._board[i].first_name:>10}, {self._board[i].surname} | {self._board[i].score}' for i in range(self._count))

    def add(self, entry):
        given_score = entry.score

        if self._count < len(self._board) or given_score > self._board[-1].score:
            if self._count < len(self._board):
                self._count += 1

            last = self._count - 1

            while last > 0 and self._board[last - 1].score < given_score:
                self._board[last] = self._board[last - 1]
                last -= 1

            self._board[last] = entry

    def insertion_sort(self):
        for i in range(1, self._count):
            element_in_outer = self._board[i]
            score_in_outer = self._board[i].score
            j = i

            while j > 0 and self._board[j - 1].score > score_in_outer:
                self._board[j] = self._board[j-1]
                j -= 1

            self._board[j] = element_in_outer


def first_implementation_with_dynamic_array():
    bogdan = ScoreEntry('Bogdan X', 127, 5)
    valentin = ScoreEntry('Valentin Soare', 140, 2)
    andreea = ScoreEntry('Andreea Petrescu', 98, 10)
    madalina = ScoreEntry('Madalina V', 156, 1)
    bobita = ScoreEntry('Bobita Bossu', 199, 1)
    ionut = ScoreEntry('Ionut H', 108, 3)

    new_array = ArrayDynamic()
    new_array.extend([bogdan, valentin, andreea, madalina, bobita, ionut])

    array_with_entries_scoring = ArrayDynamic()
    array_with_entries_scoring.extend([(new_array[i].get_name, new_array[i].score) for i in range(new_array.count)])

    sort_array_score = ArrayDynamic()
    sort_array_score.extend(sorted(array_with_entries_scoring, key=operator.itemgetter(1), reverse=True))

    print(f'\n\033[1;31m{"---SORT BY SCORE---":>27}\033[0m\n')

    count = 1
    for name, score in sort_array_score:
        print(f'{count}. Name: {name[0]}, {name[1]}; score: {score}')
        count += 1

    array_with_tries = ArrayDynamic()
    array_with_tries.extend([(new_array[i].get_name, new_array[i].number_tries) for i in range(new_array.count)])

    print(f'\n\033[1;33m{"---SORT BY NUMBER OF TRIES---":>37}\033[0m\n')

    counting = 1
    for name, number_of_tries in sorted(array_with_tries, key=operator.itemgetter(1), reverse=False):
        print(f'{counting}. Name: {name[0]}, {name[1]}; number of tries: {number_of_tries}')
        counting += 1


def second_implementation_with_score_board():
    valentin = ScoreEntry('Valentin S', 190, 5)
    gabriela = ScoreEntry('Gabriela M', 167, 1)
    andreea = ScoreEntry('Andreea P', 215, 2)
    tudorina = ScoreEntry('Tudorina S', 410, 1)
    stelian = ScoreEntry('Stelian S', 370, 1)

    new_score_card = Scoreboard(10)
    default_array_with_elements = ArrayDynamic()

    default_array_with_elements.extend([valentin, gabriela, andreea, tudorina, stelian])

    for i in range(default_array_with_elements.count):
        new_score_card.add(default_array_with_elements[i])

    #print(new_score_card)

    new_score_card.insertion_sort()
    #print(new_score_card)


def main():
    #first_implementation_with_dynamic_array()
    second_implementation_with_score_board()


if __name__ == '__main__':
    main()
