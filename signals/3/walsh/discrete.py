_FUNC = [
    [+1, +1, +1, +1, +1, +1, +1, +1], #0
    [+1, -1, -1, +1, +1, -1, -1, +1], #4
    [+1, -1, +1, -1, -1, +1, -1, +1], #6
    [+1, +1, -1, -1, -1, -1, +1, +1], #2
    [+1, +1, -1, -1, +1, +1, -1, -1], #3
    [+1, -1, +1, -1, +1, -1, +1, -1], #7
    [+1, -1, -1, +1, -1, +1, +1, -1], #5
    [+1, +1, +1, +1, -1, -1, -1, -1], #1
]


def direct_discrete_walsh_transorm(inner):
    length = len(inner)

    result = []
    sums, muls = 0, 0

    for k in range(length):
        sum = .0
        for i in range(length):
            sum += inner[i] * _FUNC[k][i]
            sums += 1; muls += 1
        result.append(sum / length)

    return result, sums, muls


def reverse_discrete_walsh_transform(inner):
    length = len(inner)

    result = []
    sums, muls = 0, 0

    for k in range(length):
        sum = .0
        for i in range(length):
            sum += inner[i] * _FUNC[k][i]
            sums +=1; muls += 1
        result.append(sum)

    return result, sums, muls
