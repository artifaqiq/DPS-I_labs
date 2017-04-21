import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

inner = [6, 10, 7, 2, 10, 12, 8, 6, 1, 6, 4, 13, 11, 8, 12, 13]

def low_pass_filter(signal):
    length = len(signal)
    out = []

    for i in range(0, length, 2):
        out.append((signal[i] + signal[i + 1]) / 2)

    return out


def high_pass_filter(signal):
    length = len(signal)
    out = []

    for i in range(0, length, 2):
        out.append((signal[i] - signal[i + 1]) / 2)

    return out


DEPTH = 20

matrix = [
    inner
]

for i in range(DEPTH):
    row = []
    for x in low_pass_filter(matrix[i]):
        row.append(x)

    for x in high_pass_filter(matrix[i]):
        row.append(x)

    matrix.append(row)


with PdfPages('result.pdf') as pdf:

    x_range = np.arange(len(inner))
    y_range = inner

    plt.plot(x_range, y_range)
    plt.axis([0, len(inner),  - (max(inner) * 1.5), (max(inner) * 1.5)])
    plt.title('Inner signal')
    pdf.savefig()
    plt.close()

    for i in range(1, len(matrix)):
        x_range = np.arange(len(matrix[i]))
        y_range = matrix[i]

        print(matrix[i])

        plt.plot(x_range, y_range)
        plt.axis([0, len(inner), - (max(inner) * 1.5), (max(inner) * 1.5)])
        plt.title('Level ' + str(i))
        pdf.savefig()
        plt.close()
