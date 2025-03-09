from PIL import Image


img = Image.open('image.jpg')
x, y = img.size
R = G = B = 0
pixels = img.load()
for i in range(x):
    for j in range(y):
        r, g, b = pixels[i, j]
        R += r
        G += g
        B += b
print(R // (x * y), G // (x * y), B // (x * y))