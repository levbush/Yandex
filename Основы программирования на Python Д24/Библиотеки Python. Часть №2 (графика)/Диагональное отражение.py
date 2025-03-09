from PIL import Image


def mirror():
    img = Image.open('image.jpg')
    img = img.transpose(Image.Transpose.FLIP_TOP_BOTTOM)
    img = img.transpose(Image.Transpose.ROTATE_90)
    img.save('res.jpg')