# Asynchronous, I need breakfast
import asyncio
from random import random

async def task_coro(arg):
    value = random() +1
    print(f"Microwave: ({arg}): Cooking {value} sec.")
    await asyncio.sleep(value)
    print(f"Microwave: ({arg}): Finish!")
    return f"{arg} done in {value} sec."

async def main():    
    tasks = ["Fried_Rice", "Noodle", "Curry"] #task list
    tasks = [asyncio.create_task(task_coro(i)) for i in tasks]

    done, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
    print(f"Completed {len(done)} task")        
    for task in done:
        print(task.result())
    print(f"Uncomplete: {len(pending)} tasks")

asyncio.run(main())