from PIL import Image, ImageDraw


def board(num, size):
    img_size = num * size
    img = Image.new('RGB', (img_size, img_size), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i in range(num):
        for j in range(num):
            if (i + j) % 2 == 0:
                draw.rectangle((j * size, i * size, (j + 1) * size - 1, (i + 1) * size - 1), fill=(0, 0, 0))
    img.save('res.png')