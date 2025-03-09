from PIL import Image, ImageDraw


def gradient(color):
    img = Image.new('RGB', (512, 200), (0, 0, 0))
    drawer = ImageDraw.Draw(img)

    def color_func(x):
        nonlocal color
        color = color.upper()
        return (x, 0, 0) if color == 'R' else (0, x, 0) if color == 'G' else (0, 0, x)

    for i in range(512):
        drawer.line(((i, 0), (i, 200)), color_func(i // 2))
    img.save('res.png', 'PNG')