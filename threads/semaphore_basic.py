from threading import Thread, Semaphore, current_thread
from time import sleep
import logging

# used to limit the number of threads operating at a time
# Here 3 threads are allowed to launch and other are waiting in the queue until one or several are completed
# Then they take these vacant positions for executions

def worker(sem: Semaphore, number):
    logging.info(f"Is waiting")
    with sem:
        logging.info(f"Got Semaphore")
        sleep(1)
        logging.info(f"Finished operation")


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")

    pool = Semaphore(3)

    logging.info('Start program')
    for i in range(10):
        w = Thread(target=worker, args=(pool, i))
        w.start()

    logging.info('End Program')
