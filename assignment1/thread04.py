# extending the Thread class and return values
from time import sleep, ctime
from threading import Thread 

#custom thread class
class CustomeThread(Thread):
    #override func 
    def run(self):
        #block
        sleep(1)
        #message
        print(f'{ctime()} This come from another thread')
        #store return val
        self.value = 99

#create    
thread = CustomeThread()
#start
thread.start()
#wait for finish
print(f'{ctime()} Waiting for thread finish')
thread.join()
#get val
value = thread.value
print(f'{ctime()} Got: {value}')