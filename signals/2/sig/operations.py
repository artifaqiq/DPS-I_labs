import numpy.fft

def convolve(x, y):

    length = len(x)
    out, sums, muls = [], 0, 0

    for m in range(length):
        sum = .0
        for n in range(length):
            sum = sum + x[n] * y[m - n]
            sums, muls = sums + 1, muls + 1

        out.append(sum / length)

    return (out, sums, muls)


def correlate(x, y):
    length = len(x)
    out, sums, muls = [], 0, 0

    for m in range(length):
        sum = .0
        for n in range(length):
            sum = sum + x[n] * y[m + n if m + n < length else m + n - length]
            sums, muls = sums + 1, muls + 1

        out.append(sum / length)

    return (out, sums, muls)

def fconvolve(x, y):
    cx = numpy.fft.fft(x)
    cy = numpy.fft.fft(y)

    cz = [a * b for a,b in zip(cx, cy)]

    return numpy.fft.ifft(cz)

def fcorrelate(x, y):
    cx = numpy.fft.fft(x)
    cx = [a.conjugate() for a in cx]

    cy = numpy.fft.fft(y)

    cz = [a * b for a, b in zip(cx, cy)]

    return numpy.fft.ifft(cz)

