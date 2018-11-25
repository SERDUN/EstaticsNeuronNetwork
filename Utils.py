import numpy


def interpolateAndNormalizeDate(dots, identificator):
    newXX = []
    newYY = []
    for i in range(1, len(dots['yReal']) - 1):

        x1 = dots['xReal'][i]
        y1 = dots['yReal'][i]
        x2 = dots['xReal'][i + 1]
        y2 = dots['yReal'][i + 1]
        if x1 - x2 != 0:
            k = (y1 - y2) / (x1 - x2)
            b = y2 - k * x2
            for j in range(x2 - x1): newXX.append(x2 + j)
            for j in range(x2 - x1): newYY.append((x2 + j) * k + b)

    tmp = []
    maxValue = max(newYY)
    minValue = min(newYY)
    tmp.append(identificator)
    for i in range(len(newYY)):
        current = newYY[i]
        numerator = current - minValue
        denominator = maxValue - minValue
        normValue = numerator / denominator
        tmp.append(normValue)
    new = []
    for line in tmp[50::7]: new.append(line)
    return tmp


def prepareArray(result, sizeInput):
    flush = numpy.zeros(sizeInput)
    for z in range(len(flush)):
        if z < len(result[:sizeInput]): flush[z] = result[:sizeInput][z]
    return flush
