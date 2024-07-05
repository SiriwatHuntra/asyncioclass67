# example of gather for many coroutines in a list
import asyncio 

#coroutine used for task
async def task_coro(values):
    #report msg
    print(f'task {values} is running')
    await asyncio.sleep(1)

async def main():
    #rp msg
    print("main started")
    #start task
    coros = [task_coro(i) for i in range (10)]
    #run task
    await asyncio.gather(*coros)
    #report a mesaage
    print('main done')
    
#start program
asyncio.run(main())