import numpy as np
from PIL import Image

from .helpers import _avv_bright, _normalize

def stretch(stretch_image, value=500):
    stretch_image = stretch_image.convert('L')
    array = np.array(stretch_image).astype(np.uint8)
    in_bright = _avv_bright(array)

    max_size = max(array.shape[0], array.shape[1])
    value_x = int(value * array.shape[0] / max_size)
    value_y = int(value * array.shape[1] / max_size)

    freq = np.fft.fftn(array)

    newFreq = np.ndarray(shape=(freq.shape[0] + value_x, freq.shape[1] + value_y), dtype=np.complex)
    newFreq.fill(0 + 0j)

    for x in range(0, freq.shape[0]):
        for y in range(0, freq.shape[1]):
            newFreq[x, y] = freq[x, y]

    freq = newFreq

    array = np.fft.ifftn(freq)
    array = array.real.astype(np.uint8)

    out_bright = _avv_bright(array)
    array = _normalize(array, in_bright / out_bright)

    stretch_image = Image.fromarray(array)
    return stretch_image