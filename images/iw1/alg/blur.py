import numpy as np
from PIL import Image

from .helpers import _avv_bright, _normalize

def blur(blur_image, value=60):
    blur_image = blur_image.convert('L')
    array = np.array(blur_image).astype(np.uint8)
    in_brigt = _avv_bright(array)

    max_size = max(array.shape[0], array.shape[1])
    value_x = int(value * array.shape[0] / max_size)
    value_y = int(value * array.shape[1] / max_size)

    freq = np.fft.fft2(array)

    for x in range(freq.shape[0] - value_x, freq.shape[0]):
        for y in range(freq.shape[1]):
            freq[x, y] = 0

    for x in range(freq.shape[0]):
        for y in range(freq.shape[1] - value_y, freq.shape[1]):
            freq[x, y] = 0

    array = np.fft.ifft2(freq)
    array = array.real.astype(np.uint8)

    out_bright = _avv_bright(array)
    array = _normalize(array, in_brigt / out_bright)

    blur_image = Image.fromarray(array)
    return blur_image