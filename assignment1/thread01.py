# running a function in another thread
from time import sleep, ctime
from threading import Thread

#a custome function that block for a moment
def task():
    #block for a moment
    sleep(1)
    #message
    print(f'{ctime()} this is an another thread')

#create thread
thread = Thread(target=task)
#run the thread 
thread.start()
#wait for finish 
print(f'{ctime()} Waiting for thread')

thread.join()
