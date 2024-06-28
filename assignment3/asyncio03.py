# example of creating an event loop
import asyncio

#create and accesss a new asychonous event loop
loop = asyncio.new_event_loop()

#report defualts of the loop
print(loop)

### 03.1 ###
#import asyncio
async def some_async_task():
    print("sleep for 1 sec")
    await asyncio.sleep(1) 
    print('done')

loop = asyncio.get_event_loop()

#Run until corotine completed
loop.run_until_complete(some_async_task())