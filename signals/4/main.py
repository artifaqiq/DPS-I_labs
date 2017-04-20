inner = [6, 10, 7, 2, 10, 12, 8, 6, 1, 6, 4, 13, 11, 8, 12, 13]


def low_pass_filter(signal):
    length = len(signal)
    out = []

    for i in range(0, length, 2):
        out.append((inner[i] + inner[i + 1]) / 2)

    return out


def high_pass_filter(signal):
    length = len(signal)
    out = []

    for i in range(0, length, 2):
        out.append((inner[i] - inner[i + 1]) / 2)

    return out


N = 4

matrix = [
    inner
]

for i in range(N):
    row = []
    for x in low_pass_filter(matrix[i]):
        row.append(x)

    for x in high_pass_filter(matrix[i]):
        row.append(x)

    matrix.append(row)

for x in matrix:
    print(x)