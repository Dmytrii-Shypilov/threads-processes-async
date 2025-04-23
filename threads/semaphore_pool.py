from threading import Thread, Semaphore, RLock ,current_thread
from time import sleep
from random import randint
import logging

# used to limit the number of threads operating at a time
# It doesn't mean that there are 3 threads always executed at a time. Can be less but no more than 3.
# Here 3 threads are allowed to launch and other are waiting in the queue until one or several are completed
# Then they take these vacant positions for executions

# for tracking active threads
class Logger:
    def __init__(self):
        self.active = []
        self.lock = RLock()
    def make_active(self, name):
        with self.lock:
            self.active.append(name)
            logging.info(f"Thread {name} started working. There are {self.active} in the pool now")
    def make_inactive(self, name):
        with self.lock:
            self.active.remove(name)
            logging.info(f"Thread {name} stopped working. There are {self.active}in the pool now")


def worker(sem: Semaphore, log: Logger):
    logging.info(f"Is waiting")
    with sem:
        name = current_thread().name
        log.make_active(name)
        logging.info(f"Got Semaphore")
        sleep(randint(1,3))
        log.make_inactive(name)
        logging.info(f"Finished operation")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")

    pool = Semaphore(3)
    logger = Logger()

    logging.info('Start program')
    for i in range(7):
        w = Thread(target=worker, args=(pool, logger))
        w.start()

    logging.info('End Program')
