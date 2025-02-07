def print_without_duplicates(message, cache=set()):
    if message not in cache:
        print(message)
        cache.add(message)
    else:
        cache.clear()
        cache.add(message)