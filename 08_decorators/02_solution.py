def debug(func):
    def wrapper(*args,**kwargs):
        arg_value = ', '.join([str(a) for a in args])
        kwargs_value = ', '.join([f"{k}={v}" for k,v in kwargs.items()])       
        print(f"calling {func.__name__} with args {arg_value} and kwargs {kwargs_value}")
        return func(*args,**kwargs)
    return wrapper


@debug
def greeting(name,greeting="Hello"):
    return f"{greeting} {name}"



greeting("Himanshu",greeting="Hi")