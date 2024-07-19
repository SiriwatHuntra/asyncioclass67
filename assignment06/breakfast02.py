import time
import asyncio

class Coffee:
    pass

class Egg:
    pass

class bacon:
    pass

class Toast:
    pass

class Juice:
    pass

def PourCoffee():
    print(f'{time.ctime()} - Begin pour coffee...')
    time.sleep(2)
    print(f'{time.ctime()} - Finish pour coffee...')
    return Coffee()

def ApplyButter():
    print(f'{time.ctime()} - Begin apply butter...')
    time.sleep(1)
    print(f'{time.ctime()} - Finish apply butter...')

async def FryEggs(eggs):
    print(f'{time.ctime()} - Begin fry eggs...')
    print(f'{time.ctime()} - Heat pan to fry eggs...')
    await asyncio.sleep(1)
    for egg in range(eggs):
        print(f'{time.ctime()} - Frying ', egg+1,' eggs')
        await asyncio.sleep(1)
    print(f'{time.ctime()} - Finish fry eggs...')
    print(f'{time.ctime()} - >>>>>> Fry eggs are ready\n')
    return Egg()

async def FryBacon():
    print(f'{time.ctime()} - Begin fry bacon...')
    await asyncio.sleep(2)
    print(f'{time.ctime()} - Finish fry bacon...')
    print(f'{time.ctime()} - >>>>> Fry bacon are ready...\n')

async def ToastBread(slices):
    for slice in range(slices):
        print(f'{time.ctime()} - Toasting bread', slice+1)
        await asyncio.sleep(1)
        print(f'{time.ctime()} - Bread ', slice+1, 'toasted')
        ApplyButter()
        print(f'{time.ctime()} - Toasting ', slice+1, ' ready')
    print(f'{time.ctime()} - >>>>>> Toast are ready\n')

def PourJuice():
    print(f'{time.ctime()} - Begin pour juice...')
    time.sleep(1)
    print(f'{time.ctime()} - Finish pour juice...')
    return Juice()

async def main():
    PourCoffee()
    print(f'{time.ctime()} - >>>>>> Coffee is ready\n')

    fryEggs_task = asyncio.create_task(FryEggs(2))
    bacon_tasks = asyncio.create_task(FryBacon())
    toast_tasks = asyncio.create_task(ToastBread(2))
    await bacon_tasks
    await fryEggs_task
    await toast_tasks

    print(f'{time.ctime()} - Nearly finish...')
    PourJuice()

if __name__=="__main__":
    start_cooking = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - start_cooking
    print(f'{time.ctime()} - Breakfast cooked in ', elapsed, "seconds." )
