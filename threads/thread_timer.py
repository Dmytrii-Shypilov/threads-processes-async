import logging
from threading import Timer
from time import sleep

def worker(arg):
    logging.info(arg)


# Timer is a postponed thread: first arg is time delay
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    
    one = Timer(0.5, worker, args=(f"Worker One",))
    one.name = 'First Thread'
    one.start()

    two = Timer(1.5, worker, args=(f"Worker Two",))
    two.name = 'Second Thread'
    two.start()

    # only second will be cancelled since first one will have enough time for execution
    sleep(1)
    one.cancel()
    two.cancel()

    logging.info('End program')