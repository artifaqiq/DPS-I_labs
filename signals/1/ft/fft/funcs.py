from cmath import pi as pi
from math import sin as sin
from math import cos as cos

def _w(k, n):
    if k % n == 0:
        return 1
    arg = -2 * pi * k / n
    return complex(cos(arg), sin(arg))

def fft(inner, iters=(0,0)):
    out = []
    length = len(inner)

    if(length == 2):
        out.append(inner[0] + inner[1])
        out.append(inner[0] - inner[1])
        iters = (iters[0] + 2, iters[1])

    else:
        even = [inner[x] for x in range(0, len(inner), 2)]
        odd = [inner[x] for x in range(1, len(inner), 2)]

        even, iters = fft(even, iters)
        odd, iters = fft(odd, iters)

        out = [None] * length
        for i in range(0, int(length / 2)):
            out[i] = even[i] + _w(i, length) * odd[i]
            out[i + int(length / 2)] = even[i] - _w(i, length) * odd[i]
            iters =(iters[0] + 2, iters[1] + 2)

    return (out, iters)


def ifft(inner):
    length = len(inner)
    out = []

    if (length == 2):
        out.append(complex(inner[0] + inner[1]))
        out.append(complex(inner[0] - inner[1]))

    else:
        even = [inner[x] for x in range(0, len(inner), 2)]
        odd = [inner[x] for x in range(1, len(inner), 2)]

        even = ifft(even)
        odd = ifft(odd)

        out = [None] * length
        for i in range(0, int(length / 2)):
            out[i] = even[i] + _w(i, length).conjugate() * odd[i]
            out[i + int(length / 2)] = even[i] - _w(i, length).conjugate() * odd[i]

    return out