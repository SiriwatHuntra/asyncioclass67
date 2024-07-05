# example of starting many tasks and getting access to all tasks
import asyncio

#coroutine for task
async def task_coroutine(values):
    #report msg
    print(f'task {values} is running')
    await asyncio.sleep(1)

async def main():
    #rp msg
    print("main coroutine started")
    #start task
    started_task = [asyncio.create_task(task_coroutine(1)) for i in range(10)]
    #allow some of the task time to start
    await asyncio.sleep(0.1)
    #get all task
    tasks = asyncio.all_tasks()

    #report all tasks
    for task in tasks:
        print(f">{task.get_name()}, {task.get_coro()}")
    #wait for all task to complete
    for task in started_task:
        await task

#start program
asyncio.run(main())