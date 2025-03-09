from PIL import Image


def transparency(file1, file2):
    img1, img2 = Image.open(file1), Image.open(file2)
    Image.blend(img1, img2, 0.5).save('res.jpg')