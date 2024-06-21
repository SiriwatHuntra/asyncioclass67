# Starting a Thread
import logging
import threading
import time

#create func
def thread_function(name):
    #start msg
    logging.info('thread %s: starting', name)
    #blocking 
    time.sleep(2)
    #finish msg
    logging.info("thread %s: finishing", name)

if __name__ == '__main__': 
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info('Main  : before creating thread')
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info('Main  : before running thread')
    x.start()
    logging.info('Main  :wait for thread finnish')
    #x.join() #if this uncomment it will wait to join all thread before do the next one
    logging.info('Mian  : all done')