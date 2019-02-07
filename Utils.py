from itertools import groupby

import numpy

HEIHT_SCREEN = 1080
WIDTH_SCREEN = 1080


def interpolateAndNormalizeDate(dots, identificator):
    newXX = []
    newYY = []

    size_list = len(dots['yReal']) - 1

    filteredDataX = dots["xReal"]
    filteredDataY = dots["yReal"]
    # for i in range(1, len(filteredDataX) - 1):
    #
    #     x1 = filteredDataX[i]
    #     y1 = filteredDataY[i]
    #     x2 = filteredDataX[i + 1]
    #     y2 = filteredDataY[i + 1]
    #     if x1 - x2 != 0:
    #         k = (y1 - y2) / (x1 - x2)
    #         b = y2 - k * x2
    #         for j in range(x2 - x1): newXX.append(x2 + j)
    #         for j in range(x2 - x1): newYY.append((x2 + j) * k + b)
    #
    tmp = []

    maxValue = max(filteredDataY)
    minValue = min(filteredDataY)

    tmp.append(identificator)
    for i in range(len(filteredDataY)):
        current = filteredDataY[i]
        numerator = current - minValue
        denominator = maxValue - minValue
        normValue = numerator / denominator

        tmp.append(normValue)
    new = []
    for line in tmp[0::15]: new.append(line)

    return new



#
#
# def interpolateAndNormalizeDate(dots, identificator):
#     # newXX = []
#     # newYY = []
#
#     size_list = len(dots['yReal']) - 1
#
#     filteredDataX = dots["xReal"]
#     filteredDataY = dots["yReal"]
#     # for i in range(1, len(filteredDataX) - 1):
#     #
#     #     x1 = filteredDataX[i]
#     #     y1 = filteredDataY[i]
#     #     x2 = filteredDataX[i + 1]
#     #     y2 = filteredDataY[i + 1]
#     #     if x1 - x2 != 0:
#     #         k = (y1 - y2) / (x1 - x2)
#     #         b = y2 - k * x2
#     #         for j in range(x2 - x1): newXX.append(x2 + j)
#     #         for j in range(x2 - x1): newYY.append((x2 + j) * k + b)
#
#     tmp = []
#
#     maxValue = max(filteredDataY)
#     minValue = min(filteredDataY)
#
#     tmp.append(identificator)
#     for i in range(len(filteredDataY)):
#         current = filteredDataY[i]
#         numerator = current - minValue
#         denominator = maxValue - minValue
#         normValue = numerator / denominator
#
#         tmp.append(normValue)
#     new = []
#     for line in tmp[0::15]: new.append(line)
#
#     return new
def interpolateDate(dots, identificator):
    newXX = []
    newYY = []

    size_list = len(dots['yReal']) - 1

    filteredDataX = dots["xReal"][100:size_list - 50]
    filteredDataY = dots["yReal"][100:size_list - 50]
    for i in range(1, len(filteredDataX) - 1):

        x1 = filteredDataX[i]
        y1 = filteredDataY[i]
        x2 = filteredDataX[i + 1]
        y2 = filteredDataY[i + 1]
        if x1 - x2 != 0:
            k = (y1 - y2) / (x1 - x2)
            b = y2 - k * x2
            for j in range(x2 - x1): newXX.append(x2 + j)
            for j in range(x2 - x1): newYY.append((x2 + j) * k + b)

    return newYY


def prepareArray(result, sizeInput):
    flush = numpy.zeros(sizeInput)
    for z in range(len(flush)):
        if z < len(result[:sizeInput]): flush[z] = result[:sizeInput][z]
    return flush


def getSignsForData(x, y):
    yMin = min(y)
    yMax = max(y)
    s = 0
    dt_dx = 0;
    for i in range(len(y) - 1):
        s += y[i] * (x[i + 1] - x[i])
        c = y[i + 1] - y[i]
        if c > dt_dx:
            dt_dx = c

    group = groupby(y)
    result = []
    index = 0
    for k, g in group:
        length = len(list(g))
        result.append((k, length, index))
        index += length

    group = max(result, key=lambda a: a[1])
    overflow = group[0]
    return [yMax, yMin, s, dt_dx, overflow]


def normalizationCoordinate(value):
    current = value
    numerator = current
    denominator = HEIHT_SCREEN
    norm = numerator / denominator
    return norm


def normalizationArea(value):
    current = value
    numerator = current
    denominator = HEIHT_SCREEN * WIDTH_SCREEN
    norm = numerator / denominator
    return norm


def normalization(signs):
    yMin = signs[1]
    yMax = signs[0]
    s = signs[2]
    dt_dx = signs[3]
    overflow = signs[4]

    yMinNorm = normalizationCoordinate(yMin)
    yMaxNorm = normalizationCoordinate(yMax)
    sNorm = normalizationArea(s)
    dtDxNorm = normalizationCoordinate(dt_dx)
    overflowNorm = normalizationCoordinate(overflow)
    return [yMaxNorm, yMinNorm, sNorm, dtDxNorm, overflowNorm]
