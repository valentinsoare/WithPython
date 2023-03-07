# SquaredSumWorkers.py

import threading
from typing import Union


class SquaredSumWorker(threading.Thread):
    def __init__(self, given_number, **kwargs):
        super(SquaredSumWorker, self).__init__(**kwargs)
        self.given_number = given_number
        self.start()

    @property
    def given_number(self) -> Union[int, float]:
        return self._given_number

    @given_number.setter
    def given_number(self, given_number: Union[int, float]) -> None:
        self._given_number = given_number

    def _calc_sum_squares(self) -> None:
        calc_sum: int = 0
        for i in range(self._given_number):
            calc_sum += i ** 2
        print(calc_sum)

    def run(self) -> None:
        self._calc_sum_squares()
