from multiprocessing import Process, Pipe
from time import sleep
import sys

# Pipe is used to interconnect different processes

def worker(conn, name):
    print(f"{name} started!")
    value = conn.recv() # waits here for the data to be received. Doesn't wait second time - process is closed
    print(f"{name}: {value**2}") # process the received data
    sys.exit(0)


if __name__ == "__main__":
    rcv1, snd1 = Pipe(duplex=False) # False means it has separate receiver and sender. Othrewise it works in both directions
    rcv2, snd2 = Pipe(duplex=False)

    # rcv - listener, snd - sender
    # listener is send to the worker to listen and receive the necessary data
    # sender sends the data when neccessary. May work (send) only once since process will end after the worker complete the job


    pr1 = Process(target=worker,  args=(rcv1, 'first'))
    pr2 = Process(target=worker,  args=(rcv2, 'second'))

    pr1.start()
    pr2.start()

    snd1.send(10)
    # snd1.send(15) - won't work since the pr1 has been completed 
    sleep(2)
    snd2.send(20)