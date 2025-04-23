from multiprocessing import Process, Semaphore, Manager, current_process
from random import randint
from time import sleep
import sys

def worker(sem: Semaphore, r: list): # type: ignore
    name = current_process().name
    print(f"{name} is waiting...")
    with sem:
        print(f"{name} is working")
        delay = randint(1, 100)
        r[name] = delay
        sleep(0.2)
        sys.exit(0)
        


if __name__ == '__main__':
    semaphore = Semaphore(3)

    with Manager() as m:
        result = m.dict() # simple structure key:val ! don't use nested structures won't be able to track changes
        # result = m.list() # [[],[]] - one level; don't use nested stuctures

        processes = []
        for num in range(10):
            pr = Process(target=worker, args=(semaphore, result))
            pr.start()
            processes.append(pr)

        [pr.join() for pr in processes]
        print(result) # should be printed inside the manager context

    print('End program')