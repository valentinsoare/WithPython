#!/usr/bin/python

import asyncio
import multiprocessing


class MultiprocessingAsync(multiprocessing.Process):
    def __init__(self, duration):
        super(MultiprocessingAsync, self).__init__()
        self._duration = duration

    @staticmethod
    async def async_sleep(duration):
        await asyncio.sleep(duration)

    async def consecutive_sleeps(self):
        pending = set()
        for duration in self._duration:
            pending.add(asyncio.create_task(self.async_sleep(duration)))

        while len(pending) > 0:
            done, pending = await asyncio.wait(pending, timeout=1)
            for i in done:
                print(await i)

    def run(self):
        asyncio.run(self.consecutive_sleeps())


if __name__ == '__main__':
    durations = []

    for i in range(1, 11):
        durations.append(i)

    processes = []
    for i in range(2):
        processes.append(MultiprocessingAsync(durations[i*5:(i+1)*5]))

    for p in processes:
        p.start()

    for p in processes:
        p.join()
