from threading import Thread, Event, current_thread
from time import sleep
import logging


def master(event: Event):
    logging.info('Master is working')
    sleep(1)
    logging.info('Master set an Event')
    # allowing workers to perform
    event.set()


def worker(event: Event):
    logging.info(f"{current_thread().name} is waiting")
    # waiting until master allow us to perform task (event.set())
    event.wait()
    logging.info(f"{current_thread().name} is working")

# Event is used for the threads execution management

# SET - to indicate that the event has occured
# WAIT -  we are waiting for the event to occur


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    event = Event()

    m = Thread(target=master, args=(event,))
    w1 = Thread(target=worker, args=(event,))
    w2 = Thread(target=worker, args=(event,))
    w3 = Thread(target=worker, args=(event,))

    w1.start()
    w2.start()
    w3.start()
    m.start()