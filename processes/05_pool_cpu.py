from multiprocessing import Pool, Process, current_process, cpu_count
from random import randint
from time import sleep, ctime

# Callback - high order function passed as the parameter. Any delayed task requires  a callback. Process is a delayed task

def worker():
    name = current_process().name
    print(f"Start process {name}: {ctime()}")
    r = randint(1,3)
    sleep(r)
    print(f"End work process {name}: {ctime()}")
    return f"Process {name} run time is {r} sec."


def callback(result):
    print(result.upper())


if __name__ == '__main__':
    print(f"CPU number is {cpu_count()}")
    cpu_num = cpu_count()
    with Pool(cpu_num) as pool:
        for i in range(cpu_num):
            pool.apply_async(worker, callback=callback) # callback will process the result of each worker
        pool.close() # Stop allocating processes into the pool
        # pool.terminate() # kill all processes
        pool.join() # wait for all porcesses to complete
    
    print(f"End {current_process().name}") 
    # End MainProcess (this script) that engendered other processes
   