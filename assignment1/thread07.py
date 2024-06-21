# Using a ThreadPoolExecutor
import concurrent.futures
import logging 
import time 

def thread_function(name):
    logging.info("Thread %s; starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ = "__main__"
