def trend(*args, **kwargs):
    for name, func in kwargs.items():
        if all(abs(func(x) - y) <= 0.01 for x, y in args):
            return name