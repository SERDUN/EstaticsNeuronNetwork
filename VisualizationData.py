import matplotlib.pyplot as plt

from Data import train_data_correct, train_data_incorrect, test_correct_data, test_incorrect_data
from Utils import interpolateAndNormalizeDate


def drawNormalizarionValue(normValue, msg):
    for i in range(len(normValue)): plt.plot(normValue[i])
    plt.legend(["graph of normalized data for the test: " + msg])
    plt.gca().invert_yaxis()
    plt.show()


def showUserTest(correct_data, incorect_data):
    plt.plot(correct_data['xReal'], correct_data['yReal'], lw=2)
    plt.plot(incorect_data['xReal'], incorect_data['yReal'], lw=2)
    plt.legend(('1 user real test incorrect', '2 user real test correct'))
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawCorrectData():
    for i in range(len(train_data_correct)):
        plt.plot(train_data_correct[i]["xReal"], train_data_correct[i]["yReal"])
    plt.legend(["Raw correct data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawIncorrectData():
    for i in range(len(train_data_incorrect)):
        plt.plot(train_data_incorrect[i]["xReal"], train_data_incorrect[i]["yReal"])
    plt.legend(["Raw incorrect data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawIncorrectDataTest():
    for i in range(len(test_incorrect_data)):
        plt.plot(test_incorrect_data[i]["xReal"], test_incorrect_data[i]["yReal"])
    plt.legend(["Raw incorrect data"])
    plt.gca().invert_yaxis()
    plt.show()


def showAllRawCorrectDataTest():
    for i in range(len(test_correct_data)):
        plt.plot(test_correct_data[i]["xReal"], test_correct_data[i]["yReal"])
    plt.legend(["Raw correct data"])
    plt.gca().invert_yaxis()
    plt.show()


def showNormalizarionValueDataTest():
    secondPersonData = []
    for x in range(len(test_incorrect_data)):
        result = interpolateAndNormalizeDate(test_incorrect_data[x], 0)
        secondPersonData.append(result)

    for i in range(len(secondPersonData)):
        plt.plot(secondPersonData[i])
    plt.gca().invert_yaxis()
    plt.show()


# showAllRawCorrectData()
# showAllRawIncorrectData()
# showAllRawCorrectDataTest()
showAllRawIncorrectDataTest()
showNormalizarionValueDataTest()