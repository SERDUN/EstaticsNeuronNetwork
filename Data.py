import json


# Підготовка тренувальних даних

train_data_correct = json.loads(open("train_data/training_correct_data_50.json").read())['result']
train_data_incorrect = json.loads(open("train_data/training_not_correct_data_50.json").read())['result']


# Підготовка тестових даних
test_incorrect_data = json.loads(open("test_data/test_not_correct_data_2.json").read())['result']
test_correct_data = json.loads(open("test_data/test_correct_data_2.json").read())['result']
