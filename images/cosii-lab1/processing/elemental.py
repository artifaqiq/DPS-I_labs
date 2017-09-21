from numpy import log1p
from PIL import Image


def logarithmic(image, c=1):
    data = image.getdata()

    new_data = []
    for px in data:
        new_color = ()
        for color in px:
            new_color += int(c * log1p(color)),

        new_data.append(new_color)

    new_image = Image.new(image.mode, image.size)
    new_image.putdata(new_data)
    return new_image

