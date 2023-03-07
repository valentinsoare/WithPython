# SleepyWorkers.py

import time
import threading
from typing import Union


class SleepyWorker(threading.Thread):
    def __init__(self, number_of_seconds, **kwargs):
        self.number_of_seconds = number_of_seconds
        super(SleepyWorker, self).__init__(**kwargs)
        self.start()

    @property
    def number_of_seconds(self) -> Union[int, float]:
        return self._number_of_seconds

    @number_of_seconds.setter
    def number_of_seconds(self, number_of_seconds) -> None:
        self._number_of_seconds = number_of_seconds

    def _sleep_a_little(self) -> None:
        time.sleep(self._number_of_seconds)

    def run(self) -> None:
        self._sleep_a_little()
