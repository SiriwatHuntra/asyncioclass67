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
    start = time()
    await make_coffee()
    await fry_eggs()
    print(f'breakfast is already in {time()-start} min.')

#Every def is coroutine, it dosen't have any task

asyncio.run(main()) #run top_Level func concurrently