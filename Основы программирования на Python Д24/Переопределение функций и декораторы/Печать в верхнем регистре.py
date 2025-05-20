def uppercase(func):
    def new_func(*args, **kwargs):
        return func(*[el.upper() for el in args], **kwargs)
    return new_func

    
print = uppercase(print)