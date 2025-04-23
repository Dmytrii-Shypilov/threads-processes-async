from multiprocessing import Pool


def worker(val):
    return val**2

if __name__ == '__main__':
    with Pool(2) as pool: # Create a pool with 2 worker processes
        r = pool.map(worker, [0,1,2,3,4,5,6,7,8,9])
        print(r)
        # Pool.map() splits the input list and distributes it among the available processes in the pool.
        # Mapping the list and applying callback to each item and distribute that job among multiple proceses
        # Each value in the list is passed to worker, which returns the square of that number.

        iterator = pool.imap(worker, range(10)) # mapping through the iterator
        print(iterator)
        print(iterator.next())
        print(iterator.next())
        print(iterator.next())