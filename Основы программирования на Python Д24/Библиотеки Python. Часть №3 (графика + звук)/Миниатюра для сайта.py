from PIL import Image


def make_preview(size, n):
    Image.open('image.jpg').resize(size).quantize(n).save('res.bmp', 'BMP')