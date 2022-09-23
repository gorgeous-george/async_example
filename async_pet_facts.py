from random import random

import aiohttp
import asyncio
import time


async def get_api_task(url, session):
    response = await session.request(method='GET', url=url)
    return await response.json()


async def dog_facts(url, session):
    result = await get_api_task(url, session)
    return result['facts'][0]


async def cat_facts(url, session):
    result = await get_api_task(url, session)
    return result['data'][0]


async def zoo_facts(url, session):
    result = await get_api_task(url, session)
    return f"{result['name']} eats {result['diet']}"


async def main():
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(*[
            dog_facts("https://dog-api.kinduff.com/api/facts", session),
            cat_facts("https://meowfacts.herokuapp.com/", session),
            zoo_facts("https://zoo-animal-api.herokuapp.com/animals/rand", session)
        ])
        # returning the longest string from the received list
        return max(results, key=len)

start = time.time()
print (asyncio.run(main()))
print (f"program took {time.time() - start} to finish")