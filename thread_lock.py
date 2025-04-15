import logging
from threading import Thread, RLock
from random import randint
from time import sleep

# RLock key unique for each specific thread; Lock - key, one for all

def worker():
    pass

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    
logging.info('Start program')



logging.info('End program')