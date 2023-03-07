#!/usr/bin/python

import asyncio
import time


async def runnning_async():
    i: int = 0

    while i < 100:
        print(f"{'* Lux si opulenta'}")
        await asyncio.sleep(1)
        i += 1


async def za_shit():
    j: int = 0
    while j < 100:
        print(f"{'Viata buna!'}")
        time.sleep(1)
        j += 1


async def main():
    await runnning_async()
    await za_shit()


if __name__ == '__main__':
    asyncio.run(main())
