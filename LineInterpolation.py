import json
import random

import matplotlib.pyplot as plt
import numpy as np
import numpy

from Calc import NeuralNetwork

sizeInput = 401
input_nodes = sizeInput - 1
hidden_nodes = 200
output_nodes = 2
learning_rate = 0.1
formatedTrainData = []

# Підготовка навчальних даних

train_30_data_incorrect = json.loads(open("train_data/30_train_data_incorrect.json").read())['result']
train_30_data_correct = json.loads(open("train_data/30_train_data_correct.json").read())['result']
flush = numpy.zeros(sizeInput)
firsPerson = train_30_data_correct
secondPerson = train_30_data_incorrect

# Підготовка тестових даних
test_incorrect_data = json.loads(open("test_data/tests_incorect_data.json").read())['result'][0]
test_correct_data = json.loads(open("test_data/tests_corect_data.json").read())['result'][0]


def interpolateAndNormalizeDate(dots, identificator):
    newXX = []
    newYY = []
    for i in range(1, len(dots['yReal']) - 1):

        x1 = dots['xReal'][i]
        y1 = dots['yReal'][i]
        x2 = dots['xReal'][i + 1]
        y2 = dots['xReal'][i + 1]
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
    for line in tmp[::5]: new.append(line)
    return new


def showUserTest():
    plt.plot(train_30_data_incorrect[0]['xReal'], train_30_data_incorrect[0]['yReal'], lw=2)
    plt.plot(train_30_data_correct[0]['xReal'], train_30_data_correct[0]['yReal'], lw=2)
    plt.legend(('1 user real test incorrect', '2 user real test correct'))
    plt.gca().invert_yaxis()


def drawNormalizarionValue(normValue, msg):
    for i in range(len(normValue)): plt.plot(normValue[i])
    plt.legend(["graph of normalized data for the test: " + msg])
    plt.show()


def prepareArray(result):
    flush = numpy.zeros(sizeInput)
    for z in range(len(flush)):
        if z < len(result[:sizeInput]): flush[z] = result[:sizeInput - 1][z]
    return flush


def guessTest(msg, json):
    result = interpolateAndNormalizeDate(json, 1)
    formatedTestData = prepareArray(result)
    result = n.query(((numpy.asfarray(formatedTestData[:sizeInput - 1]) * 0.99) + 0.01))
    drawNormalizarionValue([formatedTestData], msg)
    print(str(msg) + " ->")
    print(str(result))


# Підготовка тренувальних даних


def prepareDataFor1Test():
    secondPersonData = []
    for x in range(len(firsPerson)):
        result = interpolateAndNormalizeDate(firsPerson[x], 1)
        flush = prepareArray(result[:sizeInput])
        secondPersonData.append(flush)

    formatedTrainData.extend(secondPersonData)
    drawNormalizarionValue(secondPersonData, "First test")


def prepareDataFor2Test():
    secondPersonData = []
    for x in range(len(secondPerson)):
        result = interpolateAndNormalizeDate(secondPerson[x], 0)
        flush = prepareArray(result[:sizeInput])
        secondPersonData.append(flush)
    formatedTrainData.extend(secondPersonData[:])
    drawNormalizarionValue(secondPersonData, "Second test")


def trainNetwork():
    epochs = 20
    for e in range(epochs):
        for record in formatedTrainData:
            all_values = record

            inputs = (numpy.asfarray(all_values[1:]) * 0.99) + 0.01
            targets = numpy.zeros(output_nodes) + 0.01

            index_correct_answer = int(all_values[0])
            targets[index_correct_answer] = 0.99
            n.train(inputs, targets)


prepareDataFor1Test()
prepareDataFor2Test()
random.shuffle(formatedTrainData)

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
trainNetwork()

guessTest("(0) [result for correct test: ]: ", test_correct_data)
guessTest("(1) [result for incorrect test: ]: ", test_incorrect_data)

showUserTest()
