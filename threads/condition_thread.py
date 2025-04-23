from threading import Thread, Condition, current_thread
from time import sleep
import logging


def master(con: Condition):
    logging.info('Master is working hard')
    sleep(1)
    with con:
        logging.info('It is time to start working')
        con.notify_all()
  


def worker(con: Condition):
    logging.info(f"{current_thread().name} is waiting")
    # waiting until master allow us to perform task (event.set())
    with con:
        con.wait()
        logging.info(f"{current_thread().name} started working")

# Event is used for the threads execution management

# SET - to indicate that the event has occured
# WAIT -  we are waiting for the event to occur


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")
    con = Condition()

    m = Thread(target=master, args=(con,))
    w1 = Thread(target=worker, args=(con,))
    w2 = Thread(target=worker, args=(con,))
   

    w1.start()
    w2.start()
    m.start()