from PIL import Image


def twist_image(file, res_name):
    img = Image.open(file)
    res = Image.new('RGB', img.size)
    x, y = img.size
    res.paste(img.crop((0, 0, x // 2, y)), (x // 2, 0))
    res.paste(img.crop((x // 2, 0, x, y)), (0, 0))
    res.save(res_name)