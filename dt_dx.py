import matplotlib.pyplot as plt
import numpy
import scipy as sp

from scipy import interpolate

from Data import train_data_0


def showFunction(areaF):
    size_list = len(areaF["xReal"])
    plt.plot(areaF["xReal"], areaF["yReal"], 'ro')
    plt.show()


def f(x):
    x_points = [0, 1, 2, 3, 4, 5]
    y_points = [12, 14, 22, 39, 58, 77]

    tck = interpolate.splrep(x_points, y_points)
    return interpolate.splev(x, tck)


areaF = train_data_0[2]
#
# showFunction(areaF)

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 2, 2, 2, 2, 2, 3, 3]
#
x = numpy.array(areaF["xReal"])
y = 1080 - numpy.array(areaF["yReal"])

dt_dx = 0;

for i in range(len(y) - 1):
    c = y[i + 1] - y[i]
    if (c > dt_dx):
        dt_dx = c





newX = []
newY = []

lastX = 0

for i in range(len(x)):
    if (x[i] > lastX):
        newX.append(x[i])
        newY.append(y[i])
        lastX = x[i]


plt.plot(x, y, 'ro')
plt.plot(newX[::10], newY[::10], 'ro')

def mnkGP(x, y):
    d = 7  # степень полинома
    fp, residuals, rank, sv, rcond = sp.polyfit(x, y, d, full=True)  # Модель
    f = sp.poly1d(fp)  # аппроксимирующая функция
    print('Коэффициент -- a %s  ' % round(fp[0], 4))
    print('Коэффициент-- b %s  ' % round(fp[1], 4))
    print('Коэффициент -- c %s  ' % round(fp[2], 4))
    y1 = [fp[0] * x[i] ** 2 + fp[1] * x[i] + fp[2] for i in range(0, len(x))]  # значения функции a*x**2+b*x+c
    so = round(sum([abs(y[i] - y1[i]) for i in range(0, len(x))]) / (len(x) * sum(y)) * 100, 4)  # средняя ошибка
    print('Average quadratic deviation ' + str(so))
    fx = sp.linspace(x[0], x[-1] + 1, len(x)*2)  # можно установить вместо len(x) большее число для интерполяции
    # plt.plot(x, y, 'o', label='Original data', markersize=10)
    plt.plot(f(fx))
    plt.grid(True)
    plt.show()

mnkGP(x[::80],y[::80])
