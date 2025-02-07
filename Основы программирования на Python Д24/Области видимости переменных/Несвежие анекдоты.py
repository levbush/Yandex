def print_only_new(message, cache=set()):
    if message not in cache:
        print(message)
        cache.add(message)
    else:
        cache.add(message)