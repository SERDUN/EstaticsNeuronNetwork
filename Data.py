import json
import urllib, json
import urllib.request, json

# Підготовка тренувальних даних

train_data_0 = json.loads(open("train_data/vlad.json").read())['result']
train_data_1 = json.loads(open("train_data/serdun.json").read())['result']
train_data_2 = json.loads(open("train_data/loha.json").read())['result']

# Підготовка тестових даних
test_data_0 = json.loads(open("test_data/vlad.json").read())['result']
test_data_1 = json.loads(open("test_data/serdun.json").read())['result']
test_data_2 = json.loads(open("test_data/loha.json").read())['result']
