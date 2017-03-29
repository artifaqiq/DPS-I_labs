def _direct_fast_walsh_transorm(inner, _sums=0, _muls=0):
    length = len(inner)

    if length == 1:
        return inner, _sums, _muls

    left, right = [], []

    for i in range(int(length / 2)):
        left.append(inner[i] + inner[i + int(length / 2)])
        right.append(inner[i] - inner[i + int(length / 2)])
        _sums += 2

    left, _sums, _muls = _direct_fast_walsh_transorm(left, _sums, _muls)
    right, _sums, _muls = _direct_fast_walsh_transorm(right, _sums, _muls)

    result = [None] * length
    for i in range(int(length / 2)):
        result[i] = left[i] / 2
        result[i + int(length / 2)] = right[i] / 2

    return result, _sums, _muls


def reverse_fast_walsh_transform(inner):
    length = len(inner)
    sums, muls = 0, 0

    if length == 1:
        return inner, sums, muls

    left, right = [], []

    for i in range(int(length / 2)):
        left.append(inner[i] + inner[i + int(length / 2)])
        right.append(inner[i] - inner[i + int(length / 2)])
        sums += 2

    left, sums, muls = reverse_fast_walsh_transform(left)
    right, sums, muls = reverse_fast_walsh_transform(right)

    result = [None] * length
    for i in range(int(length / 2)):
        result[i] = left[i]
        result[i + int(length / 2)] = right[i]

    return result, sums, muls


def direct_fast_walsh_transorm(inner):
    a = _direct_fast_walsh_transorm(inner)
    array = a[0]

    array[5], array[2] = array[2], array[5]
    array[6], array[3] = array[3], array[6]
    array[7], array[4] = array[4], array[7]
    array[6], array[4] = array[4], array[6]

    return array, a[1], a[2]



