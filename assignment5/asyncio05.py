# Asynchronous, I need breakfast
import asyncio
from random import random

async def task_coro(arg):
    value = random() +1
    await asyncio.sleep(value)
    print(f"Microwave: ({arg}): Cooking {value} sec.")

async def main():    
    tasks = ["Fried_Rice", "Noodle", "Curry"] #task list
    tasks = [asyncio.create_task(task_coro(i)) for i in tasks]
    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)
    print("All done")
    first = done.pop()
    first_task = first
    print(f"The first task is: {first_task}")
asyncio.run(main())