# Synchronous cooking
# 2 kitchen 2 chefs 2 dishes
from time import sleep, ctime, time

#cooking sychonous
def cooking(index):
    print(f'{ctime()} kitchen-{index} : begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index}} : Cooking done!')

if __name__ == 'main':
    #begin of main thread
    print(f'{ctime()} Main  : Start cooking')
    start_time = time()

    #Cooking for each dish
    for index in range(2):
        cooking(index)

    duration = time() - start_time
    print(f'{ctime()} Main : Finish cooking duration in {duration:0.2f} second')
