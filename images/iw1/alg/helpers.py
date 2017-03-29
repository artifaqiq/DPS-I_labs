import numpy as np

def _avv_bright(arr2d):
    sum = 0.0
    for x in range(arr2d.shape[0]):
        for y in range(arr2d.shape[1]):
            sum = sum + arr2d[x, y] ** 2

    return np.sqrt(sum / (arr2d.shape[0] * arr2d.shape[1]))

def _normalize(arr2d, coef):
    for x in range(arr2d.shape[0]):
        for y in range(arr2d.shape[1]):
            arr2d[x, y] = arr2d[x, y] * coef
    return arr2d