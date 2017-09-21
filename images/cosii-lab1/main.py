from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import sys, os

from processing import elemental, filters


if __name__ == '__main__':
    NUM_BINS = 128
    C = 50

    image_path = sys.argv[1]
    image_name = os.path.basename(image_path)

    source_image = Image.open(image_path)

    def gist(data):
        return [np.mean(i) for i in data]


    with PdfPages('./resources/report.pdf') as pdf:

        print "[INFO] Processing source image {} ...".format(image_path)

        plt.hist(gist(source_image.getdata()), NUM_BINS, alpha=0.75, facecolor='g')
        plt.title('Source image')
        plt.grid(True)
        pdf.savefig()
        plt.close()

        print "[INFO] Processing Logarithmic Correction ... "
        log_processed_image = elemental.logarithmic(source_image, C)
        log_processed_image.save("./resources/log_" + image_name)
        plt.hist(gist(log_processed_image.getdata()), NUM_BINS, alpha=0.75, facecolor='g')
        plt.title('Logarithmic correction')
        plt.grid(True)
        pdf.savefig()
        plt.close()
        print "[INFO] Saved to ./resources/log_" + image_name

        print "[INFO] Processing Roberts Filter ... "
        roberts_filtered_image = filters.roberts(source_image)
        roberts_filtered_image.save("./resources/roberts_" + image_name)
        plt.hist(gist(roberts_filtered_image.getdata()), NUM_BINS, alpha=0.75, facecolor='g')
        plt.title('Roberts filter')
        plt.grid(True)
        pdf.savefig()
        plt.close()
        print "[INFO] Saved to ./resources/roberts_" + image_name

        print "[INFO] Processing Blur Filter ... "
        blured_image = filters.blur(source_image)
        blured_image.save("./resources/blur_" + image_name)
        plt.hist(gist(blured_image.getdata()), NUM_BINS, alpha=0.75, facecolor='g')
        plt.title('Blur filter')
        plt.grid(True)
        pdf.savefig()
        plt.close()
        print "[INFO] Saved to ./resources/blur_" + image_name

    print "[INFO] Saved report to ./resources/report.pdf"
