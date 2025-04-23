import logging
from threading import Thread, RLock
from random import randint
from time import sleep

# RLock key unique for each specific thread; Lock - key, one for all

counter = 0
lock = RLock()

# lock.acquire()
# some resource manipulation (without context, primitive)
# lock.release()

# !!!! ALWAYS USE LOCK IF THE THREADS ARE WORKING WITH A COMMON RESOURCE !!!

def worker():
    global counter
    while True:
        # reserve resource for usage by a particular worker at a time (works slowly)
        with lock:
            counter += 1
            # imitating process
            sleep(randint(1, 3))
            with open('results.txt', 'a') as fd:
                fd.write(f"{counter}\n")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")

logging.info('Start program')

for i in range(6):
    thread = Thread(name=f"Thread #{i}", target=worker)
    thread.start()

logging.info('End program')
