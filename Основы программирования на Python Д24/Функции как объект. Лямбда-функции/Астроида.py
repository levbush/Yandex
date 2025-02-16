from math import pi, sin, cos
print(min([((cos(t)**3 - 0.75)**2 + (sin(t)**3)**2)**0.5 for t in range(100000, int(2 * pi * 100000) + 1)]))