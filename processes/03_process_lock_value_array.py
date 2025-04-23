from multiprocessing import Process, current_process, RLock, Value, Array
from ctypes import c_int, c_double, c_char, Structure
from sys import exit

# COMMUNICATION BETWEEN PROCESSES
# OS hates when one program tries to intervene with the other one (may regard as a virus)
# ctypes = type from C language

# to create an array with a certain structure (Point coordinates)
class Point(Structure):
    _fields_ = [("x", c_double), ('y', c_double)] # list of tuples


def worker(val: Value, arr: Array, string: Array): # type: ignore
    print(f"Start process: {current_process().name}")
    with val.get_lock():
        val.value += 1
        print(f"Process: {current_process().name}: {val.value}") 
    with string.get_lock():
        string.value = string.value.upper()
    with arr.get_lock():
        for el in arr:
            el.x += val.value
            el.y += val.value
    


if __name__ == '__main__':
    print('Start program')

    value = Value(c_double, 1.5, lock=RLock()) # in RAM we allocatу a piece of memory for our processes (for this variable)
    # Array contains only similar type of data contrary to the List ( Static -  can't change the length)
    string = Array('c', b'The best of the best progarmmer', lock=RLock())
    arr = Array(Point, [(0,0), (2,0), (2,2)], lock=RLock()) # array of points (triangle)

    processes = []

    for i in range(3):
        pr = Process(target=worker, args=(value, arr, string)) # daemon=True
        pr.start()
        processes.append(pr)

        [pr.join() for pr in processes]
        [print(pr.exitcode) for pr in processes]

        print(value.value)
        print(string.value)
        [print(el.x, el.y) for el in arr]

        print('End program')