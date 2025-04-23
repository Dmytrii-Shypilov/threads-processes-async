from threading import Thread, Event, current_thread
from time import sleep
import logging

# THE ONLY METHOD HOW TO MANAGE THREAD EXECUTION


def worker(event: Event, event_exit: Event):
    while True:
        if event_exit.is_set():
            break

        sleep(1)
        if event.is_set():
            logging.info('Futile iteration')
            continue
        else:
            logging.info('DDOS srever')


# Event is used for the threads execution management

# SET - to indicate that the event has occured
# WAIT -  we are waiting for the event to occur


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    event = Event()
    event_exit = Event()

   
    w1 = Thread(target=worker, args=(event, event_exit))
    w1.start()

    logging.info('Start Program')
    sleep(2)

    event.set() # stop thread execution
    logging.info('Stop Thread')
    sleep(2)

    event.clear() # Restarting the tread again
    logging.info('Restart Thread')

    sleep(3)
    event_exit.set() # ending whole progarm
    logging.info("End program")