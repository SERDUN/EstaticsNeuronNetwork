import numpy
from keras.datasets import mnist
from keras.layers import Dense
from keras.models import Sequential
from keras.utils import np_utils
from Data import train_data_0, train_data_1, test_data_0, test_data_1
from Utils import interpolateAndNormalizeDate, prepareArray

formatedTrainData = []
resultTrain = []

formatedTestData = []
resultTest = []

sizeInput = 600
sizeInpuTest = 6


def prepareDataForTrain(data, title, id_result):
    secondPersonData = []
    for x in range(len(data)):
        result = interpolateAndNormalizeDate(data[x], id_result)[1::]
        if (id_result == 0):
            resultTrain.append(numpy.array([1, 0]))
        else:
            resultTrain.append(numpy.array([0, 1]))

        flush = prepareArray(result[:sizeInput], sizeInput)
        secondPersonData.append(flush)
    formatedTrainData.extend(secondPersonData)


def prepareDataForTest(data, title, id_result):
    secondPersonData = []
    for x in range(len(data)):
        result = interpolateAndNormalizeDate(data[x], id_result)[1::]
        if (id_result == 0):
            resultTest.append(numpy.array([1.0, 0.0]))
        else:
            resultTest.append(numpy.array([0.0, 1.0]))

        flush = prepareArray(result[:sizeInput], sizeInput)
        secondPersonData.append(flush)
        formatedTestData.extend(secondPersonData)


numpy.random.seed(42)

flush = numpy.zeros(sizeInput)
firsPerson = train_data_0
secondPerson = train_data_1

prepareDataForTrain(train_data_0, "Fomin", 0)
prepareDataForTrain(train_data_1, "Kate", 1)

prepareDataForTest(test_data_0, "Fomin", 0)
prepareDataForTest(test_data_1, "Kate", 1)
#
# Y_train = np_utils.to_categorical(y_train, 10)
# Y_test = np_utils.to_categorical(y_test, 10)

# Создаем последовательную модель
model = Sequential()

# Добавляем уровни сети
model.add(Dense(600, input_dim=sizeInput, activation="relu", kernel_initializer="normal"))
model.add(Dense(2, activation="softmax", kernel_initializer="normal"))

# Компилируем модель
model.compile(loss="categorical_crossentropy", optimizer="SGD", metrics=["accuracy"])

print(model.summary())

# Обучаем сеть
model.fit(numpy.array(formatedTrainData), numpy.array(resultTrain), epochs=25, validation_split=0.2, verbose=2)

# Оцениваем качество обучения сети на тестовых данных
scores = model.evaluate(numpy.array(formatedTestData)[1::], numpy.array(resultTest), verbose=0)
print("Точность работы на тестовых данных: %.2f%%" % (scores[1] * 100))
