from multiprocessing import Pool, current_process, cpu_count


def worker(n):
    sum = 0
    for i in range(n):
        sum += i
    print(f"{n} into sum: {sum}")
    return sum


def callback(result):
    print(f"Result in callback: {result}")


if __name__ == '__main__':
     print(f"CPU number is {cpu_count()}")
     cpu_num = cpu_count()
     with Pool(cpu_num) as pool:
        pool.map_async(worker, [12,22,33,57,89,45,122,11,45,79,76,443,65], callback=callback)
        # callback is applied tothe final result when all workers complete the job (whole mapping process)
        pool.close()
        pool.join()
    
     print(f"End {current_process().name}")
