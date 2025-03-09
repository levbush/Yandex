from PIL import Image
from math import ceil


def mirror():
    img = Image.open('image.jpg')
    pixels = img.load()
    x, y = img.size
    for i in range(ceil(x / 2)):
        for j in range(y):
            pixels[i, j], pixels[~i, j] = pixels[~i, j], pixels[i, j]
    img.save('res.jpg')