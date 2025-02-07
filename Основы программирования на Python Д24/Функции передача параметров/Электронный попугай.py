cache = set()


def parrot(phrase):
    if phrase in cache:
        print(phrase)
        return 
    cache.add(phrase)