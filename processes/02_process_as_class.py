from multiprocessing import Process
from time import sleep
import sys

# Redefining parent class Process (customized Process class)
# Daemon kill incomplete processes when script running is completed
class MyProcess(Process):
    def __init__(self, group = None, target = None, name = None, args = (), kwargs = None, *, daemon = None):
        super().__init__(group, target, name, args, kwargs, daemon=daemon)
        self.args = args
        self.kwargs = kwargs

    def run(self) -> None:
        self.kwargs.get('log')(f"rags: {self.args}") # run the passed log function
        sys.exit(0)

# function to be passed as an argument
def log(msg):
    print(msg)



if __name__ == '__main__':
    for i in range(5):
        pr = MyProcess(args=(f"Count process - #{i}",), kwargs={'log': log})
        pr.start()
  

    # [print(pr.exitcode, end=" ") for pr in processes]
    # print('')

    # [pr.join() for pr in processes] # waiting for all processes to complete
    # [print(pr.exitcode, end=" ") for pr in processes]