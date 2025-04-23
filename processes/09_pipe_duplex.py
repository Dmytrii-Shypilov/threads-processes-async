from multiprocessing import Process, Pipe
from time import sleep
import sys

# like echo server always waiting forthe vent and sends back the result
def worker(receiver): 
    while True:
        try:
            instance = receiver.recv() # receives from wk
            receiver.send(f"Ok for: {instance}") # sends to wk
            print(f"Received: {instance}")
        except EOFError: # when pipe is closed (receiver) - breaks the loop; should return something
            return None
        

def wk(sender, store):
    for el in store:
        sender.send(el) # sends to worker
        recieved_back = sender.recv() # receives back from worker
        print(recieved_back)


def main():
    start_pipe, end_pipe = Pipe(duplex=True)

    store = [12, 'Hello', {'name': "Dima"}, 22, None, 0]

    my_worker = Process(target=worker, args=(end_pipe,))
    my_wk = Process(target=wk, args=(start_pipe, store))
    my_worker.start()
    my_wk.start()

    my_wk.join() #  wait for wk to complete 
    start_pipe.close()
    end_pipe.close()

if __name__ == '__main__':
    main()