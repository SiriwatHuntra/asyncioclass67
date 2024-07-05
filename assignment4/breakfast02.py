# Concurrently breakfast
import asyncio
from time import sleep, time


async def make_coffee():
    print('coffee: prepare ingradients')
    sleep(1)
    print("coffee: waiting...")
    await asyncio.sleep(5) #pause, other task can run
    print('Coffee: Ready')


async def fry_eggs():
    print('eggs: prepare ingradients')
    sleep(1)
    print("eggs: frying...")
    await asyncio.sleep(3) #pause, other task can run
    print('eggs: Ready')


async def main():
    start