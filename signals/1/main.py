import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from math import sin as sin
from math import cos as cos
import cmath
from cmath import pi as pi


func = lambda x: sin(3 * x) + cos(x)


def dft(inner):
    out = []
    length = len(inner)

    for m in range(length):
        temp = complex(.0, .0)
        for n in range(length):
            arg = -2 * pi * m * n / length
            temp = temp + complex(inner[n] * cos(arg), inner[n] * sin(arg))

        out.append(temp)

    return out

def idft(inner):
    out = []
    length = len(inner)

    for m in range(length):
        temp = complex(.0, .0)
        for n in range(length):
            arg = 2 * pi * m * n / length
            temp = temp + complex(inner[n] * cos(arg), inner[n] * sin(arg))

        out.append(temp / length)

    return out

def _w(k, n):
    if k % n == 0:
        return 1
    arg = -2 * pi * k / n
    return complex(cos(arg), sin(arg))


def fft(inner):
    out = []
    length = len(inner)

    if(length == 2):
        out.append(inner[0] + inner[1])
        out.append(inner[0] - inner[1])

    else:
        even = [inner[x] for x in range(0, len(inner), 2)]
        odd = [inner[x] for x in range(1, len(inner), 2)]

        even = fft(even)
        odd = fft(odd)

        out = [None] * length
        for i in range(0, int(length / 2)):
            out[i] = even[i] + _w(i, length) * odd[i]
            out[i + int(length / 2)] = even[i] - _w(i, length) * odd[i]
    return out


def ifft(inner):
    pass

def sampled(func, n):
    out = []
    for i in range(n):
        out.append(func(2 * pi * (i + 1) / n))

    return out

with PdfPages('result.pdf') as pdf:

    N = 16

    inner = sampled(func,N)
    spectrum = dft(inner)

    # DFT
    x = np.arange(0, 2 * pi, 0.1);
    y = np.sin(3 * x) + np.cos(x)

    plt.plot(x, y)
    plt.title('Inner signal')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), inner, "b:o")
    plt.title('Sampled signal. N = 16')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[0] for x in spectrum], "go")
    plt.title('DFT. Amplitude spectrum')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[1] for x in spectrum], "go")
    plt.title('DFT. Phase spectrum')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N),[x.real for x in idft(spectrum)], "r:o")
    plt.title('Inverse DFT')
    pdf.savefig()
    plt.close()

    #FFT

    spectrum = fft(inner)

    plt.plot(np.arange(N), [cmath.polar(x)[0] for x in spectrum], "go")
    plt.title('FFT. Amplitude spectrum')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), [cmath.polar(x)[1] for x in spectrum], "go")
    plt.title('FFT. Phase spectrum')
    pdf.savefig()
    plt.close()

    


    # We can also set the file's metadata via the PdfPages object:
    d = pdf.infodict()
    d['Title'] = 'Multipage PDF Example'
    d['Author'] = u'Jouni K. Sepp\xe4nen'
    d['Subject'] = 'How to create a multipage pdf file and set its metadata'
    d['Keywords'] = 'PdfPages multipage keywords author title subject'
    d['CreationDate'] = datetime.datetime(2009, 11, 13)
    d['ModDate'] = datetime.datetime.today()