# -*- coding: utf-8 -*-
import PIL.Image as Image
from numpy import *
from matplotlib.pyplot import *
from matplotlib.image import *

from numpy import save, load

image = Image.open('./image.png').convert('L')
image = array(image) / 255.0
image2 = Image.fromarray(image).save("image.tiff")


CL = [(1 + sqrt(3)) / (4 * sqrt(2)),
    (3 + sqrt(3)) / (4 * sqrt(2)),
    (3 - sqrt(3)) / (4 * sqrt(2)),
    (1 - sqrt(3)) / (4 * sqrt(2))]


def hpf_coeffs(CL):
    N = len(CL)
    CH = [(-1)**k * CL[N - k - 1]
        for k in xrange(N)]
    return CH


def pconv(data, CL, CH, delta = 0):
    assert(len(CL) == len(CH))         # Размеры списков коэффициентов должны быть равны
    N = len(CL)
    M = len(data)
    out = []                           # Список с результатом, пока пустой
    for k in xrange(0, M, 2):  # Перебираем числа 0, 2, 4…
        sL = 0                         # Низкочастотный коэффициент
        sH = 0                         # Высокочастотный коэффициент
        for i in xrange(N):      # Находим сами взвешенные суммы
            sL += data[(k + i - delta) % M] * CL[i]
            sH += data[(k + i - delta) % M] * CH[i]
        out.append(sL)                 # Добавляем коэффициенты в список
        out.append(sH)
    return out


def icoeffs(CL, CH):
    assert(len(CL) == len(CH))         # Размеры списков коэффициентов должны быть равны
    iCL = []  # Коэффициенты первой строки
    iCH = []  # Коэффициенты второй строки
    for k in xrange(0, len(CL), 2):
        iCL.extend([CL[k-2], CH[k-2]])
        iCH.extend([CL[k-1], CH[k-1]])
    return (iCL, iCH)


def dwt2(image, CL):
    CH = hpf_coeffs(CL)   # Вычисляем недостающие коэффициенты
    w, h = image.shape    # Размеры изображения
    imageT = image.copy() # Копируем исходное изображение для преобразования
    for i in xrange(h):   # Обрабатываем строки
        imageT[i, :] = pconv(imageT[i, :], CL, CH)
    for i in xrange(w):   # Обрабатываем столбцы
        imageT[:, i] = pconv(imageT[:, i], CL, CH)

    # Переупорядочиваем столбцы и строки
    data = imageT.copy()
    data[0:h/2, 0:w/2] = imageT[0:h:2, 0:w:2]
    data[h/2:h, 0:w/2] = imageT[1:h:2, 0:w:2]
    data[0:h/2, w/2:w] = imageT[0:h:2, 1:w:2]
    data[h/2:h, w/2:w] = imageT[1:h:2, 1:w:2]
    return data


def idwt2(data, CL):
    w, h = data.shape  # Размеры изображения

    # Переупорядочиваем столбцы и строки обратно
    imageT = data.copy()
    imageT[0:h:2, 0:w:2] = data[0:h / 2, 0:w / 2]
    imageT[1:h:2, 0:w:2] = data[h / 2:h, 0:w / 2]
    imageT[0:h:2, 1:w:2] = data[0:h / 2, w / 2:w]
    imageT[1:h:2, 1:w:2] = data[h / 2:h, w / 2:w]

    CH = hpf_coeffs(CL)
    iCL, iCH = icoeffs(CL, CH)
    image = imageT.copy()  # Копируем исходное изображение для преобразования
    for i in xrange(w):  # Обрабатывем столбцы
        image[:, i] = pconv(image[:, i], iCL, iCH, delta=len(iCL) - 2)
    for i in xrange(h):  # Обрабатывем строки
        image[i, :] = pconv(image[i, :], iCL, iCH, delta=len(iCL) - 2)

    return image


data = dwt2(image, CL)

for threshold in arange(0.05, 1.25, 0.1):
    data[abs(data) < threshold] = 0
    image2 = Image.fromarray(idwt2(data, CL).astype(float64))
    image2.save("image.compressed.threshold=" + str(threshold) + ".tiff")






