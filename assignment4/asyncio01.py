# example of getting the current task from the main coroutine
import asyncio

#define main coroutine
async def main():
    #report msg
    print("main coroutine started")
    #get current task
    task = asyncio.current_task()
    #report it detail
    print(task)

#start asyc program
asyncio.run(main())