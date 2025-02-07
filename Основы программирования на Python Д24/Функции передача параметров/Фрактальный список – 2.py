def defractalize(fractal):
    i = 0
    while i < len(fractal):
        if fractal[i] is fractal:
            fractal.pop(i)
        else:
            i += 1