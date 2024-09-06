# example of using an asyncio queue without blocking
from random import random
import asyncio
import time
 
# coroutine to generate work
async def producer(queue):
    print('Producer: Running')
    produce_time = time.perf_counter()

    # generate work
    for i in range(10):
        # generate a value
        value = i
        # block to simulate work
        sleeptime = 0.9 #random()
        print(f"> Producer {value} sleep {sleeptime}")
        await asyncio.sleep(sleeptime)
        # add to the queue
        print(f"> Producer put {value}")
        await queue.put(value)
    # send an all done signal
    await queue.put(None)
    end_produce_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous Produce 10 tasks. Time taken: {end_produce_time-produce_time:.2f} seconds")
    print('Producer: Done')

# coroutine to consume work
async def consumer(queue):
    print('Consumer: Running')
    consume_start = time.perf_counter()

    # consume work
    while True:
        # get a unit of work without blocking
        try:
            item = queue.get_nowait()
        except asyncio.QueueEmpty:
            print('Consumer: got nothing, waiting a while...')
            await asyncio.sleep(0.8)
            continue
        # check for stop
        if item is None:
            break
        # report
        print(f'\t> Consumer got {item}')
    # all done
    end_consume = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous consume 10 tasks. Time taken: {end_consume-consume_start:.2f} seconds")
    print('Consumer: Done')
 
# entry point coroutine
async def main():
    start_time = time.perf_counter()
    #create the shared queue
    queue = asyncio.Queue(3)
    #run the producer and consumers
    await asyncio.gather(producer(queue), consumer(queue))
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get 10 tasks. Time taken: {end_time-start_time:.2f} seconds")

 
# start the asyncio program
asyncio.run(main())