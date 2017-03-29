from cmath import pi as pi
from math import sin as sin
from math import cos as cos

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages

import walsh

N = 8


x_func = lambda t: sin(3 * t) + cos(7 * t)


def sampled(func, n, period=(2 * pi)):
    out = []
    for i in range(n):
        out.append(round(func(period * (i + 1) / n), 5))
    return out


with PdfPages('result.pdf') as pdf:

    x = sampled(x_func, N)

    x_range = np.arange(0, 2 * pi, 0.1)
    y_range = np.sin(3 * x_range) + np.cos(7 * x_range)

    plt.plot(x_range, y_range)
    plt.title('Inner signal')
    plt.xlabel(r'$x$')
    plt.ylabel(r'$x = f(t)$')
    pdf.savefig()
    plt.close()

    plt.plot(np.arange(N), x, "b:o")
    plt.title('Sampled signal. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    #discrete
    walshed_dicrete = walsh.direct_discrete_walsh_transorm(x)
    plt.plot(np.arange(N), walshed_dicrete[0], "r:o")
    plt.title('Discrete Walsh transform. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    rev_walshed = walsh.reverse_discrete_walsh_transform(walshed_dicrete[0])
    plt.plot(np.arange(N), rev_walshed[0], "r:o")
    plt.title('Reverse Walsh transform. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    #fast
    walshed_fast = walsh.direct_fast_walsh_transorm(x)
    plt.plot(np.arange(N), walshed_fast[0], "g:o")
    plt.title('Fast Walsh transform. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    rev_walshed = walsh.reverse_discrete_walsh_transform(walshed_fast[0])
    plt.plot(np.arange(N), rev_walshed[0], "g:o")
    plt.title('Reverse Fast Walsh transform. N = {0}'.format(N))
    plt.xlabel(r'$t$')
    plt.ylabel(r'$y$')
    pdf.savefig()
    plt.close()

    fig = plt.figure()
    fig.suptitle('Сomplexity', fontsize=14, fontweight='bold')

    ax = fig.add_subplot(111)

    ax.text(1, 8, 'DWT', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5})
    ax.text(1, 7, 'FWT', style='italic',
            bbox={'facecolor': 'red', 'alpha': 0.5})
    ax.text(2, 9, 'Sums', style='italic',
            bbox={'facecolor': 'gray', 'alpha': 0.5})
    ax.text(3, 9, 'Muls', style='italic',
            bbox={'facecolor': 'gray', 'alpha': 0.5})

    ax.text(2, 8, walshed_dicrete[1], style='italic')
    ax.text(3, 8, walshed_dicrete[2], style='italic')
    ax.text(2, 7, walshed_fast[1], style='italic')
    ax.text(3, 7, walshed_fast[2], style='italic')

    ax.axis([0, 10, 0, 10])

    pdf.savefig()
    plt.close()

