# from functools import cache as cached
def cached(old_func):
    cache = {}
    
    def new_func(*args, **kwargs):
        nonlocal cache
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = old_func(*args, **kwargs)
        return cache[key]
    return new_func