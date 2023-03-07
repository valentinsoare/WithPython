#!/usr/bin/python

import asyncio
import threading
import multiprocessing
import concurrent.futures


async def async_sleep(n):
    print(f"Before Sleep")
    for i in range(n):
        yield i
        await asyncio.sleep(i)

    print(f'After Sleep')


async def print_hello():
    print(f"Hello!!")


async def main():
    async for k in async_sleep(5):
        print(k)

if __name__ == '__main__':
    asyncio.run(main())
