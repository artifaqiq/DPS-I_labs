from PIL import Image
from alg import *

SOURCE = "./parrot.jpg"
image = Image.open(SOURCE)

print("Blur image " + SOURCE); image_blur = blur(image)
print("Sharp image " + SOURCE); image_sharp = inc_sharp(image)
print("Stretch image " + SOURCE); image_stretch = stretch(image)


blur_im_path = "./" + SOURCE.split(".")[-2] + ".blur." + SOURCE.split(".")[-1]
image_blur.save(blur_im_path, "JPEG"); print("Blur image save as " + blur_im_path);

sharp_im_path = "./" + SOURCE.split(".")[-2] + ".sharp." + SOURCE.split(".")[-1]
image_sharp.save(sharp_im_path, "JPEG"); print("Sharp image save as " + sharp_im_path);

stretch_im_path = "./" + SOURCE.split(".")[-2] + ".stretch." + SOURCE.split(".")[-1]
image_stretch.save(stretch_im_path, "JPEG"); print("Stretch image save as " + stretch_im_path);
