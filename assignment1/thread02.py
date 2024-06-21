# running a function with arguments in another thread
from time import sleep, ctime
from threading import Thread

#a custome func that block for a moment
def task(sleep_time, message):
    #block for a moment
    sleep(sleep_time)
    #message
    print(f'{ctime()} {message}')

#create thread
thread = Thread(target=task, args=(1.5, "New message from another thread"))
#run the thread 
thread.start()
#wait for finish 
print(f'{ctime()} Waiting for thread')

thread.join()
