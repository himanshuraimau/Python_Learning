import time

def timer(func):   # timer is a decorator function
    def wrapper(*args,**kwargs):  # wrapper is a closure function
        start = time.time()   # start time
        result = func(*args,**kwargs)  # calling the function
        end = time.time()   # end time
        print(f"Time taken by {func.__name__} is {end-start}") # printing the time taken
        return result  # returning the result
    return wrapper  # returning the closure function


@timer  # decorator
def example_function(n):
    time.sleep(n)   # sleep for n seconds


example_function(2)

