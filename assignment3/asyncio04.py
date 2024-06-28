# Starting task
from time import ctime
import asyncio

async def wash(basket):
    print(f"{ctime} : washing machine ({basket}): Put the coin")
    print(f"{ctime} : washing machine ({basket}): Start washing")
    await asyncio.sleep(5)
    print(f'{ctime()} : Washing machine ({basket}) : finish washing')
    return f'{ctime()} : {basket} is complete'

async def main():
    #create corotine
    coro = wash('basket A')
    print(f'{ctime()} : {coro}')
    print(f'{ctime()} : {type(coro)}')
    #create task
    task = asyncio.create_task(coro)
    print(f'{ctime()} : {task}')
    print(f'{ctime()} : {type(task)}')
    #run task
    result = await task
    print(f'{ctime()} : {result}')

if __name__ == "__main__":
    asyncio.run(main())