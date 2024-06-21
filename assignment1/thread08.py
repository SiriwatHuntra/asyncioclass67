# Race Conditions
import concurrent.futures
import logging 
import time

class FakeDatabase:
    def __init__(self):
        self.value = 0

    # thread 1 and 2 read 0 at same time 
    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1) 
        self.value = local_copy
        #thread 1 and 2 update thier self (1) into memory so we will get 1
        logging.info("Thread %s: finish update", name)

if __name__ == "__main__" :
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level= logging .INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d", database.value)
    # 2 thread at same time 
    with concurrent.futures.ThreadPoolExecutor(max_workers= 2 ) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d", database.value)