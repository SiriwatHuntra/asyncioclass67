# extending the Thread class
from time import sleep, ctime
from threading import Thread

#custom threaf class
class CustomThread(Thread):
    #override the run func
    def run(self):
        #block
        sleep(1)
        #message
        print(f'{ctime()} this comming from an another thread')

#create thread
thread = CustomThread()
#run the thread 
thread.start()
#wait for finish 
print(f'{ctime()} Waiting for thread finish')

thread.join()
