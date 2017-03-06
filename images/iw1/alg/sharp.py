import numpy as np
from PIL import Image

from .helpers import _avv_bright, _normalize

def inc_sharp(sharp_image, value=50):
    sharp_image = sharp_image.convert('L')

    array = np.array(sharp_image).astype(np.uint8)
    in_brigt = _avv_bright(array)

    max_size = max(array.shape[0], array.shape[1])
    value_x = int(value * array.shape[0] / max_size)
    value_y = int(value * array.shape[1] / max_size)

    freq = np.fft.fft2(array)

    for x in range(0, value_x):
        for y in range(freq.shape[1]):
            freq[x, y] = 0

    for x in range(freq.shape[0]):
        for y in range(0, value_y):
            freq[x, y] = 0

    array = np.fft.ifft2(freq)
    array = array.real.astype(np.uint8)

    out_bright = _avv_bright(array)
    array = _normalize(array, in_brigt / out_bright)

    sharp_image = Image.fromarray(array)
    return sharp_image