import numpy as np
import numpy
import matplotlib.pyplot as plt

from Data import train_data_0, train_data_1


def showFunction(areaF):
    size_list = len(areaF["xReal"])
    plt.plot(areaF["xReal"], areaF["yReal"], 'ro')
    plt.show()


areaF = train_data_0[4]
#
# showFunction(areaF)

# x = [1, 2, 3, 4, 5, 6, 7, 8]
# y = [2, 2, 2, 2, 2, 2, 3, 3]
#
x = numpy.array(areaF["xReal"])
y = 1080-numpy.array(areaF["yReal"])

plt.plot(x, y, 'ro')
plt.plot(x, y, 'b')

plt.show()

s = 0
for i in range(0, len(x) - 1):
    s += y[i] * (x[i + 1] - x[i])
    print(str(x[i + 1]) + " * " + str(y[i]))
print(s)
