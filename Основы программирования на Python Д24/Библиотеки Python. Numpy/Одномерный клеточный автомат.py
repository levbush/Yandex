import numpy as np

r30 = {(1, 1, 1): 0, (1, 1, 0): 0, (1, 0, 1): 0, (1, 0, 0): 1, (0, 1, 1): 1, (0, 1, 0): 1, (0, 0, 1): 1, (0, 0, 0): 0}

def generation(line):
    line = np.array(list(line), dtype=np.uint8)
    for _ in range(10):
        nl = np.roll(line, 1)
        nu = line
        nr = np.roll(line, -1)
        line = np.zeros(len(line), dtype=np.uint8)
        for i in range(len(line)):
            line[i] = r30[(nl[i], nu[i], nr[i])]
    return ''.join(map(str, line))