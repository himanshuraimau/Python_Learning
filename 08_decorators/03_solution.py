import time

def cache(func):
    cache = {}
    print(cache)
    def wrapper(*args,**kwargs):
        if(args in cache):
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper



@cache
def long_running_function(a,b):
    time.sleep(2)
    return a+b


print(long_running_function(1,2))
print(long_running_function(1,2))
print(long_running_function(1,3))
