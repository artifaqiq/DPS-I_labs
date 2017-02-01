import cmath
import datetime
from cmath import pi as pi
from math import cos as cos
from math import sin as sin

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from ft import dft as dft
from ft import idft as idft
from ft import fft as fft
from ft import ifft as ifft
import ft

func = lambda x: sin(3 * x) + cos(x)

import numpy.fft

def sampled(func, n):
    out = []
    for i in range(n):
        out.append(func(2 * pi * (i + 1) / n))

    return out

with PdfPages('result.pdf') as pdf:

    N = 16
    inner = sampled(func, N)
    spectrum, iters_dft = dft(inner)

    # DFT
    x = np.arange(0, 2 * pi, 0.1)
    y = np.sin(3 * x) + np.cos(x)

    plt.plot(x, y)
    plt.title('Inner signal')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y = f(x)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), inner, "b:o")
    plt.title('Sampled signal. N = 16')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[0] for x in spectrum], "go")
    plt.title('DFT. Amplitude spectrum')
    plt.xlabel(r'$f$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[1] for x in spectrum], "go")
    plt.title('DFT. Phase spectrum')
    pdf.savefig()
    plt.xlabel(r'$f$')
    plt.close()

    plt.plot(np.arange(N),[x.real for x in idft(spectrum)], "r:o")
    plt.title('Inverse DFT')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    #FFT
    spectrum, iters_fft = fft(inner)

    plt.plot(np.arange(N), [cmath.polar(x)[0] for x in spectrum], "go")
    plt.title('FFT. Amplitude spectrum')
    pdf.savefig()
    plt.xlabel(r'$f$')
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[1] for x in spectrum], "go")
    plt.title('FFT. Phase spectrum')
    plt.xlabel(r'$f$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [x.real / N for x in ifft(spectrum)], "r:o")
    plt.title('Inverse FFT')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    fig = plt.figure()
    fig.suptitle('Сomplexity', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)

    ax.text(1, 8, 'DFT', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5})
    ax.text(1, 7, 'FFT', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5})
    ax.text(2, 9, 'Iterations', style='italic',
            bbox={'facecolor': 'gray', 'alpha': 0.5})

    ax.text(2, 8, iters_dft, style='italic')
    ax.text(2, 7, iters_fft, style='italic')





    ax.axis([0, 10, 0, 10])

    pdf.savefig()
    plt.close()

