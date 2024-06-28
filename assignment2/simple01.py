# Synchronous cooking
# 1 kitchen 1 chefs 1 dish
from time import sleep, ctime, time
#cooking synchornous
def cooking(index):
    print(f'{ctime()} kitchen-{index} : begin cooking...')
    sleep(2)
    print(f'{ctime()} Kitchen-{index} : Cooking done!')

if __name__ == "main":
    #Begin of main thread
    print(f"{ctime()} Main  : Start Cooking.")
    start_time = time()
    #Cooking
    cooking(0)

    duration = time() - start_time
    print(f'{ctime()} Main  : Finish Cooking dduration in {duration:0.2f} seconds')