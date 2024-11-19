from PIL import Image
import numpy as np


def bw_convert():
    image = np.asarray(Image.open('image.jpg').convert('RGB'))
    gray = np.stack([np.round(
        0.2989 * image[:, :, 0] + 0.5870 * image[:, :, 1] + 0.1140 * image[:, :, 2]).astype(np.uint8)] * 3, axis=-1)
    Image.fromarray(gray).save('res.jpg')