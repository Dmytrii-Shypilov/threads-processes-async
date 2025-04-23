from threading import Thread, Barrier, RLock, current_thread
from time import sleep, ctime
from random import randint
import logging

# Barrier set a threshold (# of threads) that should be surpassed in order for threads to start working
# Barier is 4 so 4 threads should be launched to further continue working after barrier.wait()
# Total # of threads launched should be multiple of # indicated in Barrier(num) since the barrier won't be surpassed
# and it will be waiting infinitely


def worker(bar: Barrier):
    name = current_thread().name
    logging.info(f"Start thread {name}: {ctime()}")
    num = bar.wait()
    sleep(randint(1, 3))
    logging.info(f"Barrier is surpassed {name}#{num}: {ctime()}")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")

    br = Barrier(4)

    logging.info('Start program')
    for i in range(12): # 12 is multiple of 4
        w = Thread(target=worker, args=(br,))
        w.start()

    logging.info('End Program')
