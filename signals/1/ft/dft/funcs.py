from cmath import pi as pi
from math import sin as sin
from math import cos as cos

def dft(inner):
    out = []
    iters = (0, 0)
    length = len(inner)

    for m in range(length):
        temp = complex(.0, .0)
        for n in range(length):
            arg = -2 * pi * m * n / length
            temp = temp + complex(inner[n] * cos(arg), inner[n] * sin(arg))
            iters = (iters[0] + 1, iters[1] + 2)

        out.append(temp)

    return (out,iters)

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