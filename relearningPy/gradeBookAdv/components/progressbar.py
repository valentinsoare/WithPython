# progressbar.py

from time import sleep
from typing import Union
from itertools import cycle
from threading import Thread
from shutil import get_terminal_size


class ProgressBar:
    def __init__(self, description: str = "Loading...", end: str = "Done!", timeout: Union[int, float] = 0.1):

        self.description = description
        self.end = end
        self.timeout = timeout
        self.flag_for_end: bool = False

        self._thread = Thread(target=self._exec_animate)
        self.animated_characters: list = [['\\', '|', '/', '-'],
                                          ["⢿", "⣻", "⣽", "⣾", "⣷", "⣯", "⣟", "⡿"]]

    def start(self):
        self._thread.start()
        return self

    def _exec_animate(self) -> None:
        for i in cycle(self.animated_characters[1]):
            if self.flag_for_end:
                break
            print(f"\r{' ' * 7}{self.description}... {i} ", flush=True, end="")
            sleep(self.timeout)

    def __enter__(self) -> None:
        self.start()

    def stop(self) -> None:
        self.flag_for_end = True
        columns = get_terminal_size((80, 20)).columns
        print("\r" + " " * columns, end="", flush=True)
        print(f"\r{' ' * 7}{self.description}...{self.end}", flush=True)
        sleep(1)

    def __exit__(self, exc_type, exc_value, tb) -> None:
        self.stop()
