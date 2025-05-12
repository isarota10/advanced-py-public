import time 

def timeit(fn:callable):
    def wrapper(*args, **kwargs):
        start = time.time()

        result = fn(*args,**kwargs)


        end = time.time()

        print(f"Elapsed time: {end-start:.4f} for {fn.__name__}")

        return result
    
    return wrapper

def timeit2(unit:str):
    def timeit(fn:callable):
        def wrapper(*args, **kwargs):
            start = time.time()

            result = fn(*args,**kwargs)


            end = time.time()

            if unit == "ms":
                print(f"Elapsed time: {(end-start)*1000.:.4f} ms for {fn.__name__}")
            else:
                print(f"Elapsed time: {(end-start):.4f} sec for {fn.__name__}")

            return result
        
        return wrapper
    
    return timeit

class TimeIt:
    def __init__(self,unit:str):
        self.unit = unit

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            start = time.time()

            result = fn(*args,**kwargs)

            end = time.time()

            if self.unit == "ms":
                print(f"Elapsed time: {(end-start)*1000.:.4f} ms for {fn.__name__}")
            else:
                print(f"Elapsed time: {(end-start):.4f} sec for {fn.__name__}")

            return result
    
        return wrapper
        

#@timeit
#@TimeIt(unit="sec")
@timeit2(unit="sec")
def sleepy2(sec:float):
    print(f"Falling into to sleep for {sec} seconds")
    time.sleep(sec)
    print("I woke up")

@timeit
def sleepy(sec:float):
    print(f"Falling into to sleep for {sec} seconds")
    time.sleep(sec)
    print("I woke up")


if __name__ == "__main__":

    sleepy(3.)

    timer = TimeIt("sec")

    wrapped = timer(sleepy)

    wrapped(3)




