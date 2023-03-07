#!/usr/bin/python

import time
import asyncio
import aiohttp
import requests


async def get_url_response(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    # non async
    given_urls = ['https://google.ro',
                  'https://ansible.com',
                  'https://python.org']

    start_time = time.time()
    sync_text_response = []
    for url in given_urls:
        sync_text_response.append(requests.get(url).text)

    print(f"Request time: {time.time() - start_time}")

    #---------------------------------
    # async
    start = time.time()
    tasks = []

    for url in given_urls:
        tasks.append(asyncio.create_task(get_url_response(url)))

    async_text_response = await asyncio.gather(*tasks)

    print(f"Request time: {time.time() - start}")

if __name__ == '__main__':
    asyncio.run(main())
