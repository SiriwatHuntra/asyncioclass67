# example of using an asyncio queue
from random import random
import asyncio
import time

#coroutine generate work
async def producer(queue):
    print('Producer: Running')
    produce_time = time.perf_counter()
    #generate work'
    for i in range(10):
        #generate a value
        value = i
        #block to simulate work
        sleeptime = 0.99 #random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
    #send an all done signal
    await queue.put(None)
    end_produce_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous Produce 10 tasks. Time taken: {end_produce_time-produce_time:.2f} seconds")
    print('Producer: Done')

#coroutine to cunsume work
async def consumer(queue):
    consume_start = time.perf_counter()
    print('Consumer: Running')
    #consume work
    while True:
        #get a unit of work without blocking
        item = await queue.get()
        #check for stop
        if item is None:
            break
        #report
        print(f'\t> Consumer got {item}')
    end_consume = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous Produce 10 tasks. Time taken: {end_consume-consume_start:.2f} seconds")
    print('Consumer: Done')

#entry point coroutine
async def main():
    start_time = time.perf_counter()
    #create the shared queue
    queue = asyncio.Queue()
    #run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get 10 tasks. Time taken: {end_time-start_time:.2f} seconds")


#start the asyncio program
asyncio.run(main())
    