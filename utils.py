
from time import time

mem = {}


def time_fn(func):

    def measure_time(*arg, **kwarg):

        func_name = func.__name__

        if func_name not in mem.keys():
            mem[func_name] = {
                "n": 0,
                "time": 0
            }

        start = time()
        func(*arg, **kwarg)

        mem[func_name]["n"] += 1
        mem[func_name]["time"] += time()-start

        if mem[func_name]["n"] == 60:

            print("czas wykonania funkcji "
              + func_name + " - " + str(mem[func_name]["time"]))

            mem[func_name]["n"] = 0
            mem[func_name]["time"] = 0

    return measure_time
