from multiprocessing import Process
from time import sleep
import sys

# Processes (programs) use separate memory. Threads arerunning within one process use shared memory
# !!! If there is Global Variable defined above processes won't be able to share it !!!
# Can use Event, Condition, Barrier for managing as well like with threads. Semaphore uses Manager

def example_woker(params):
    sleep(2)
    print(params) # can use in process in thread better use logger
    sys.exit(0) # good practice; 0 means process has complete successfully without error


if __name__ == '__main__':
    processes = []
    for i in range(5):
        pr = Process(target=example_woker, args=(f"Count process - #{i}",))
        pr.start()
        processes.append(pr)

    [print(pr.exitcode, end=" ") for pr in processes]
    print('')

    [pr.join() for pr in processes] # waiting for all processes to complete
    [print(pr.exitcode, end=" ") for pr in processes]

    # Exit code = None means that the process has not completed< 0 - if completed without error