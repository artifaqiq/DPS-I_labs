import numpy as np
from PIL import Image


def colour_by_clusters(marked_image, stat, n_clusters):
    clustered_image = Image.new(size=marked_image.size, mode='RGB')
    marked_image_pixels = np.asarray(marked_image)
    clustered_pixels = np.asarray(clustered_image).copy()

    rgb = rgb_random_generator()
    cluster_to_color = {}

    for x in range(n_clusters):
        cluster_to_color[x + 1] = rgb.next()

    for x in range(1, marked_image.size[1] - 1):
        for y in range(1, marked_image.size[0] - 1):
            if is_black_pixel(marked_image_pixels[x][y]):
                pass
            else:
                try:
                    clustered_pixels[x][y] = cluster_to_color[
                        stat[str(marked_image_pixels[x][y])]['cluster']
                    ]
                except KeyError:
                    pass

    return Image.fromarray(clustered_pixels)


def mark(car_types_image_path):
    history = []

    full = Image.open(car_types_image_path)
    history.append(full)

    bin_image = _binarize(full)

    history.append(bin_image)

    mrk_images = _mark(bin_image)
    history += mrk_images

    return history


def geom_stat(mrk_image):
    stat = {}
    pixels = np.asarray(mrk_image)

    for x in range(1, mrk_image.size[1]):
        for y in range(1, mrk_image.size[0]):
            if is_black_pixel(pixels[x][y]):
                pass
            else:
                if str(pixels[x][y]) not in stat:
                    stat[str(pixels[x][y])] = {
                        'color': str(pixels[x][y]),
                        'area': 0,
                        'perimeter': 0
                    }
                stat[str(pixels[x][y])]['area'] += 1
                if filter(
                        lambda pixel: is_black_pixel(pixel),
                        [
                            pixels[x - 1][y],
                            pixels[x][y - 1],
                            pixels[x][y],
                            pixels[x + 1][y],
                        ]
                ):
                    stat[str(pixels[x][y])]['perimeter'] += 1

    for color in stat:
        stat[color]['compact'] = stat[color]['perimeter'] ** 2 / stat[color]['area']

    return stat


def _binarize(image, threshold=220):
    new = Image.new(mode='1', size=image.size)
    data = np.asarray(image)
    new_data = []

    for x in data:
        for pixel in x:
            if np.mean(pixel) < threshold:
                new_data.append(False)
            else:
                new_data.append(True)

    new.putdata(new_data)
    return new


def _mark(bin_image):
    pixels = np.asarray(bin_image)
    rgb = rgb_random_generator()

    history = []
    mrk_image = Image.new(size=bin_image.size, mode='RGB')
    mrk_pixels = np.asarray(mrk_image).copy()

    for x in range(1, bin_image.size[1] - 1):
        for y in range(1, bin_image.size[0] - 1):
            if pixels[x][y]:
                pass
            elif not is_black_pixel(mrk_pixels[x][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y - 1]
            elif not is_black_pixel(mrk_pixels[x - 1][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y - 1]
            elif not is_black_pixel(mrk_pixels[x - 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y]
            else:
                mrk_pixels[x][y] = rgb.next()

    history.append(Image.fromarray(mrk_pixels))

    for x in reversed(range(1, bin_image.size[1] - 1)):
        for y in reversed(range(1, bin_image.size[0] - 1)):
            if is_black_pixel(mrk_pixels[x][y]):
                pass
            elif not is_black_pixel(mrk_pixels[x][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y + 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y + 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y]

    history.append(Image.fromarray(mrk_pixels))

    for x in reversed(range(1, bin_image.size[1] - 1)):
        for y in range(1, bin_image.size[0] - 1):
            if is_black_pixel(mrk_pixels[x][y]):
                pass
            elif not is_black_pixel(mrk_pixels[x][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y - 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y - 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y]

    history.append(Image.fromarray(mrk_pixels))

    for x in range(1, bin_image.size[1] - 1):
        for y in reversed(range(1, bin_image.size[0] - 1)):
            if pixels[x][y]:
                pass
            elif not is_black_pixel(mrk_pixels[x - 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y]
            elif not is_black_pixel(mrk_pixels[x - 1][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y + 1]
            elif not is_black_pixel(mrk_pixels[x][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y + 1]

    history.append(Image.fromarray(mrk_pixels))

    for y in range(1, bin_image.size[0] - 1):
        for x in range(1, bin_image.size[1] - 1):
            if pixels[x][y]:
                pass
            elif not is_black_pixel(mrk_pixels[x][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y - 1]
            elif not is_black_pixel(mrk_pixels[x - 1][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y - 1]
            elif not is_black_pixel(mrk_pixels[x - 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y]

    history.append(Image.fromarray(mrk_pixels))

    for x in reversed(range(1, bin_image.size[1] - 1)):
        for y in reversed(range(1, bin_image.size[0] - 1)):
            if is_black_pixel(mrk_pixels[x][y]):
                pass
            elif not is_black_pixel(mrk_pixels[x][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y + 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y + 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y]

    history.append(Image.fromarray(mrk_pixels))

    for y in range(1, bin_image.size[0] - 1):
        for x in reversed(range(1, bin_image.size[1] - 1)):
            if is_black_pixel(mrk_pixels[x][y]):
                pass
            elif not is_black_pixel(mrk_pixels[x][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y - 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y - 1]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y - 1]
            elif not is_black_pixel(mrk_pixels[x + 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x + 1][y]

    history.append(Image.fromarray(mrk_pixels))

    for y in reversed(range(1, bin_image.size[0] - 1)):
        for x in range(1, bin_image.size[1] - 1):
            if pixels[x][y]:
                pass
            elif not is_black_pixel(mrk_pixels[x - 1][y]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y]
            elif not is_black_pixel(mrk_pixels[x - 1][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x - 1][y + 1]
            elif not is_black_pixel(mrk_pixels[x][y + 1]):
                mrk_pixels[x][y] = mrk_pixels[x][y + 1]

    history.append(Image.fromarray(mrk_pixels))

    return history


def k_means():
    pass


def rgb_random_generator():
    while True:
        yield (
            int(np.random.random() * 255),
            int(np.random.random() * 255),
            int(np.random.random() * 255)
        )


def is_white_pixel(pixel):
    return np.array_equal(pixel, (255, 255, 255))


def is_black_pixel(pixel):
    return np.array_equal(pixel, (0, 0, 0))


def array_contains(arr, intersect):
    return bool(filter(lambda x: np.array_equal(x, intersect), arr))
