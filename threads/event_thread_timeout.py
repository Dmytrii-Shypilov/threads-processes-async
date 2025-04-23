from threading import Thread, Event, current_thread
from time import sleep
import logging

# Master with timeout
def master(event: Event):
    logging.info('Master is working')
    sleep(1)
    logging.info('Master set an Event')
    # allowing workers to perform
    event.set()


def worker_stupid(event: Event):
    logging.info(f"{current_thread().name} is waiting")
    # waiting until master allow us to perform task (event.set())
    event.wait()
    logging.info(f"{current_thread().name} is working")

def worker_smart(event: Event, time: float):
    # Do some work while master is not allowing to procede (don't stand still just waiting)
    while not event.is_set():
        logging.info("Waiting for event to be set as complete")
        # After indicated time we check whether the event is set as complete
        e_wait = event.wait(time) # True or False
        if e_wait:
            logging.info("Performing the work as ordered by master")
        else:
            logging.info("Can still play around")

# Event is used for the threads execution management

# SET - to indicate that the event has occured
# WAIT -  we are waiting for the event to occur


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    logging.info('Start program')

    event = Event()

    w1 = Thread(target=worker_stupid, args=(event,))
    w1.start()

    w2 = Thread(target=worker_smart, args=(event,1))
    w2.start()

    sleep(3)
    event.set()

    logging.info('End program')

    # m = Thread(target=master, args=(event,))
    # m.start()