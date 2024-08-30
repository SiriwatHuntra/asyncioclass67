import asyncio

async def task1():
    print('hello from coro 1')
    await asyncio.sleep(1)

    
async def task2():
    print('hello from coro 2')
    await asyncio.sleep(0.5)
    raise Exception('Something bad happened')

    
async def task3():
    print('hello from coro 3')
    await asyncio.sleep(1)

async def main():
    try:
        async with asyncio.TaskGroup() as group:
                t1 = group.create_task(task1())
                t2 = group.create_task(task2())
                t3 = group.create_task(task3())
    except:
            pass
    print(f"task1: done={t1.done()}, cancelled={t1.cancelled()}")
    print(f"task2: done={t2.done()}, cancelled={t2.cancelled()}")
    print(f"task3: done={t3.done()}, cancelled={t3.cancelled()}")

asyncio.run(main())