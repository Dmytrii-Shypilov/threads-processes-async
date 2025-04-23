from threading import Thread
from random import randint
from time import sleep
import logging


def worker(arg):
    print(f"My thread {arg} is working!")

# redefining the thread


class MyThread(Thread):
    def __init__(self, group=None, target=None, name=None,
                 args=(), kwargs=None, *, daemon=None):
        super().__init__(group=group, target=target, name=name,
                         args=args, kwargs=kwargs, daemon=daemon)

    # redefining method
    def run(self):
        # return super().run()
        ttl = randint(1, 3)
        sleep(ttl)
        logging.info(f"In my thread {self.name} i have a lag of {ttl} seconds")


# Process (main thread) and multiple threads within this process
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG,
                        format="%(threadName)s %(message)s")

    threads = []
    for i in range(6):
        thread = MyThread(name=f"Thread #{i}")
        thread.start()
        threads.append(thread)
    # join() to wait for the completion of specific thread
    [th.join() for th in threads]
    # Program ends but process iteslf is still being executed (if threads are not joined)
    logging.info('End program')

# If we state daemon=True the process will kill all the uncompleted runing threads when program finishes (Main Threads ends)