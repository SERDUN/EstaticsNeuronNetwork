import random

import numpy as np
import numpy

from Calc import NeuralNetwork
from Data import train_data_correct, train_data_incorrect, test_correct_data, test_incorrect_data
from Utils import interpolateAndNormalizeDate, prepareArray
from VisualizationData import drawNormalizarionValue, showUserTest

sizeInput = 2000
input_nodes = sizeInput - 1
hidden_nodes = 250
output_nodes = 2
learning_rate = 0.2
formatedTrainData = []
epochs = 10

# Підготовка навчальних даних

flush = numpy.zeros(sizeInput)
firsPerson = train_data_correct
secondPerson = train_data_incorrect








def guessTest(msg, json):
    result = interpolateAndNormalizeDate(json, 1)
    formatedTestData = prepareArray(result,sizeInput)
    result = n.query(((numpy.asfarray(formatedTestData[:sizeInput - 1]) * 0.99) + 0.01))
    drawNormalizarionValue([formatedTestData], msg)
    print(str(msg) + " ->")
    print(str(result))


# Підготовка тренувальних даних


def prepareDataFor1Test():
    secondPersonData = []
    for x in range(len(firsPerson)):
        result = interpolateAndNormalizeDate(firsPerson[x], 1)
        flush = prepareArray(result[:sizeInput],sizeInput)
        secondPersonData.append(flush)

    formatedTrainData.extend(secondPersonData)
    drawNormalizarionValue(secondPersonData, "First test")


def prepareDataFor2Test():
    secondPersonData = []
    for x in range(len(secondPerson)):
        result = interpolateAndNormalizeDate(secondPerson[x], 0)
        flush = prepareArray(result[:sizeInput],sizeInput)
        secondPersonData.append(flush)
    formatedTrainData.extend(secondPersonData[:])
    drawNormalizarionValue(secondPersonData, "Second test")


def trainNetwork():
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

guessTest("incorrect:  ", test_correct_data[0])
# guessTest("(1) [result for correct test: ]: ", test_correct_data[0])


showUserTest(train_data_correct[0], train_data_incorrect[0])
