# check the type of a coroutine
import asyncio
# define a corourite
async def custom_coro():
    #await another corutine
    await asyncio.sleep(1)

#create the coroutine
coro = custom_coro()
#check type of the coroutine 
print(type(coro))