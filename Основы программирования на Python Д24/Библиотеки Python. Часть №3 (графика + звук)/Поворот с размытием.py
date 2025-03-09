from PIL import Image, ImageFilter


def motion_blur(n):
    img = Image.open('image.jpg')
    img = img.transpose(Image.Transpose.ROTATE_270)
    img.filter(ImageFilter.GaussianBlur(radius=n)).save('res.jpg')