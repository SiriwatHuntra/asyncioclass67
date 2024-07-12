# example of waiting for the first task to fails

from random import random
import asyncio

#coroutine to exe in new task
async def task_coro(arg):
    #gen rand value 0-1
    value = random()

    #block for a moment 
    await asyncio.sleep(value)

    #report value
    print(f"> Task {arg} done with {value}")

    if value < 0.5:
        raise Exception(f"Something bad happend with {arg}")


async def main():
    #create tasks
    task = [asyncio.create_task(task_coro(i)) for i in range(10)]

    #wait for all task complete
    done, pending = await asyncio.wait(task, return_when=asyncio.FIRST_EXCEPTION)

    print("All done")

    #get 1st task done
    first = done.pop()
    print(f"The first task is: {first}")

#Start Main\
asyncio.run(main())