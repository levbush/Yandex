from PIL import Image
import math
import random


def image_filter(pixels, i, j):
    """Окунает картинку в кисель."""
    if 'blur_map' not in globals():
        globals()['blur_map'] = {(i, j): random.random() < 0.1 for i in range(x) for j in range(y)}
    if blur_map[i, j]:  # type: ignore
        shift_x, shift_y = random.randint(-5, 5), random.randint(-5, 5)
        i = min(x - 1, max(0, i + shift_x))
        j = min(y - 1, max(0, j + shift_y))
    
    if random.random() < 0.6:
        freq_x, freq_y = random.randint(5, 15), random.randint(5, 15)
        amp_x, amp_y = random.randint(2, 10), random.randint(2, 10)
        i = min(x - 1, max(0, i + int(amp_x * math.sin(2 * math.pi * j / freq_x))))
        j = min(y - 1, max(0, j + int(amp_y * math.cos(2 * math.pi * i / freq_y))))

    r, g, b = pixels[i, j]
    r = int(0.8 * r + 0.2 * b)
    g = int(0.1 * r + 0.7 * g + 0.2 * b)
    b = int(0.9 * b + 0.1 * r)
    r, g, b = min(255, r + 50), min(255, int(g * 0.8)), min(255, b + 30)

    if random.random() < 0.01:  
        r = min(255, r + random.randint(-40, 40))
        g = min(255, g + random.randint(-40, 40))
        b = min(255, b + random.randint(-40, 40))

    return r, g, b


img = Image.open("image.jpg")
pixels = img.load()
x, y = img.size

for i in range(x):
    for j in range(y):
        pixels[i, j] = image_filter(pixels, i, j)

img.save('res.jpg')
