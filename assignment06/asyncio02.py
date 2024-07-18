#example of an async iterator with ascy for loop
import asyncio

#define an asynchonous itrerator 
class AsyncIterator():
    #constuctor, define some state
    def __init__(self):
        self.counter = 0
    
    #create an instance of the iterator
    def __aiter__(self):
        return self
    
    #return next awaitable
    async def __anext__(self):
        #check for on further items
        if self.counter >= 10:
            raise StopAsyncIteration
        #increment the counter
        self.counter += 1
        #simulate work
        await asyncio.sleep(1)
        # return the counter value
        return self.counter

#main coroutine 
async def main():
    #loop over async iterator with async for loop
    async for item in AsyncIterator():
        print(item)

#exe the asyncio programs
asyncio.run(main())
        