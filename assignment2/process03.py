# Multiprocessing 2 kitkens, 2 cooker, 2 dishes
# 2 process
import multiprocessing
from multiprocessing import Value
import os
from time import sleep, ctime, time 

#basket of sharing
class Basket:
    def __init__(self, eggs):
        self.eggs = Value('i', eggs)

    def use_eggs(self, index):
        print(f'{ctime()} Kitchen-{index} : Chef-{index()} has lock with eggs remaining {self.eggs}')
        self.eggs -= 1
        print(f'{ctime()} Kitchen-{index} : Chef-{index} has release lock with eggs remaining {self.eggs}')

#Chef cooking
def cooking(index, basket):
    cooking_time = time()
    print(f'{ctime()} Kitchen-{index} : begin cooking PID {os.getpid()}')
    sleep(2)
    duration = time() - cooking_time
    with basket.eggs.get_lock():
        basket.eggs.value = basket.eggs.value - 1
        print(f'{ctime()} Kitchen-{index} : Used eggs')
    print(f'{ctime()} Kitchen-{index} : cooking done in {duration:0.2f} seconds')


#Kitchen cooking
def kitchen(index, basket):
    cooking(index, basket)
    
if __name__ == "__main__" :
    #begin main thread 
    print(f'{ctime()} Main  : begin cooking')
    start_time = time()

    basket = Basket(50)
    
    print(f'{ctime()} Main : ID of main process: {os.getpid()}')

    #Multi process
    kitchens  = []
    for index in range(50):
        p = multiprocessing.Process(target=kitchen, args=(index, basket))
        kitchens.append(p)
        # starting processes
        p.start()

    for p in kitchens:
        #wait until processes are finished
        p.join()

    print(f'{ctime()} Main : basket eggs remaining {basket.eggs}')
    duration = time() - start_time
    print(f"{ctime()} Main   : Finished Cooking duration in {duration:0.2f} seconds")