from cmath import pi as pi
from math import cos as cos
from math import sin as sin

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

from sig.operations import *

x_func = lambda t: sin(3 * t)
y_func = lambda t: cos(t)
N = 16 # <-- replace on your N

def sampled(func, n, period=(2 * pi)):
    out = []
    for i in range(n):
        out.append(round(func(period * (i + 1) / n), 5))

    return out

import numpy

with PdfPages('result.pdf') as pdf:

    x = sampled(x_func, N)
    y = sampled(y_func, N)

    x_range = np.arange(0, 2 * pi, 0.1)  # <--replace on your function
    y_range = np.sin(3 * x_range)

    plt.plot(x_range, y_range)
    plt.title('Inner signal x')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$x = f(t)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), x, "b:o")
    plt.title('Sampled signal x. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    x_range = np.arange(0, 2 * pi, 0.1)  # <--replace on your function
    y_range = np.cos(x_range)

    plt.plot(x_range, y_range)
    plt.title('Inner signal y')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y = f(t)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), y, "b:o")
    plt.title('Sampled signal y. N = {0}'.format(N))
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

### convolve

    plt.plot(np.arange(N), convolve(x, y)[0],  "r:o")
    plt.title('x * y. Classic')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y = f(t)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), fconvolve(x, y), "r:o")
    plt.title('x * y. Fast')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y = f(t)$')
    pdf.savefig()
    plt.close()

### correlation

    plt.plot(np.arange(N), correlate(x, y)[0], "r:o")
    plt.title('x corr y. Classic')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y = f(t)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), fcorrelate(x, y), "r:o")
    plt.title('x corr y. Fast')
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y = f(t)$')
    pdf.savefig()
    plt.close()