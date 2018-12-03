import matplotlib.pyplot as plt
import urllib.request, json
from Data import train_data_0, train_data_1, test_data_0
from Utils import interpolateAndNormalizeDate


def drawNormalizarionValue(normValue, msg):
    for i in range(len(normValue)): plt.plot(normValue[i])
    plt.legend(["graph of normalized data for the test: " + msg])
    plt.gca().invert_yaxis()
    plt.show()


def showUserTest(correct_data, incorect_data):
    plt.plot(correct_data['xReal'], correct_data['yReal'], lw=2)
    plt.plot(incorect_data['xReal'], incorect_data['yReal'], lw=2)
    plt.plot(test1['xReal'], test1['yReal'], lw=2)
    plt.legend(('1 user real test incorrect', '2 user real test correct'))
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawCorrectData():
    size_list = len(train_data_0)
    for i in range(size_list):
        x = train_data_0[i]["xReal"][50:size_list - 50]
        y = train_data_0[i]["yReal"][50:size_list - 50]
        plt.plot(x, y)
        plt.legend(["Raw correct data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawIncorrectData():
    for i in range(len(train_data_1)):
        plt.plot(train_data_1[i]["xReal"], train_data_1[i]["yReal"])
    plt.legend(["Raw incorrect data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawIncorrectDataTest():
    for i in range(len(test_data_0)):
        plt.plot(test_data_0[i]["xReal"], test_data_0[i]["yReal"])
    plt.legend(["Raw incorrect data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawCorrectDataTest():
    for i in range(len(test_data_1)):
        plt.plot(test_data_1[i]["xReal"], test_data_1[i]["yReal"])
    plt.legend(["Raw correct data"])
    plt.gca().invert_yaxis()
    plt.show()


def showNormalizarionValueDataTest():
    secondPersonData = []
    for x in range(len(test_data_0)):
        result = interpolateAndNormalizeDate(test_data_0[x], 0)
        secondPersonData.append(result)

    for i in range(len(secondPersonData)):
        plt.plot(secondPersonData[i])
    plt.gca().invert_yaxis()
    plt.show()


def showRawData(data):
    for i in range(len(data)):
        plt.plot(data[i]["xReal"][50:len(data) - 50], data[i]["yReal"][50:len(data) - 50])
    plt.legend(["Raw incorrect data"])
    plt.gca().invert_yaxis()
    plt.show()


#
# showRawData(triangle)
#
showAllRawCorrectData()
showAllRawIncorrectData()
#
# showAllRawCorrectDataTest()
# showAllRawIncorrectDataTest()
# showNormalizarionValueDataTest()
