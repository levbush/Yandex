from PIL import Image


def makeanagliph(filename, delta):
    img = Image.open(filename)
    pixels = img.load()
    x, y = img.size
    anagliph = Image.new('RGB', img.size)
    anagliph_pixels = anagliph.load()
    for i in range(x):
        for j in range(y):
            anagliph_pixels[i, j] = (pixels[i - delta, j][0] if i >= delta else 0, *pixels[i, j][1:])
    anagliph.save('res.jpg')