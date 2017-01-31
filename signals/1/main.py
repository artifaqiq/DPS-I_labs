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

func = lambda x: sin(3 * x) + cos(x)

def sampled(func, n):
    out = []
    for i in range(n):
        out.append(func(2 * pi * (i + 1) / n))

    return out

with PdfPages('result.pdf') as pdf:

    N = 16
    inner = sampled(func, N)
    spectrum = dft(inner)

    # DFT
    x = np.arange(0, 2 * pi, 0.1);
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
    spectrum = fft(inner)

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

    plt.plot(np.arange(N), [x.real for x in ifft(spectrum)], "r:o")
    plt.title('Inverse FFT')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    d = pdf.infodict()
    d['Title'] = 'Multipage PDF Example'
    d['Author'] = u'Jouni K. Sepp\xe4nen'
    d['Subject'] = 'How to create a multipage pdf file and set its metadata'
    d['Keywords'] = 'PdfPages multipage keywords author title subject'
    d['CreationDate'] = datetime.datetime(2009, 11, 13)
    d['ModDate'] = datetime.datetime.today()