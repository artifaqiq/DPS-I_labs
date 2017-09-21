from PIL import Image
import numpy as np


def roberts(image):
    pixels = np.asarray(image)
    size = image.size
    new_pixels = pixels.copy()

    for i in range(size[1] - 1):
        for j in range(size[0] - 1):
            new_pixels[i][j] = (
                np.abs(np.square(
                    pixels[i + 1][j] - pixels[i][j + 1]
                ))
                +
                np.abs(np.square(
                    pixels[i][j] - pixels[i + 1][j + 1]
                ))
            )

    return Image.fromarray(new_pixels)


def blur(image):
    pixels = np.asarray(image)
    size = image.size
    new_pixels = pixels.copy()

    for i in range(1, size[1] - 1):
        for j in range(1, size[0] - 1):
            new_pixels[i][j] = (
                np.mean([
                    pixels[i - 1][j - 1],
                    pixels[i - 1][j],
                    pixels[i - 1][j + 1],
                    pixels[i][j - 1],
                    pixels[i][j],
                    pixels[i][j + 1],
                    pixels[i + 1][j - 1],
                    pixels[i + 1][j],
                    pixels[i + 1][j + 1]
                ], axis=0, dtype=int)
            )

    return Image.fromarray(new_pixels)
