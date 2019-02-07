import json
import urllib, json
import urllib.request, json

# Підготовка тренувальних даних
#
train_data_0 = json.loads(open("train_data/not_calm_condition.json").read())['result']
train_data_3 = json.loads(open("train_data/calm_condition.json").read())['result']
#
# # Підготовка тестових даних
test_data_0 = json.loads(open("test_data/not_calm_condition.json").read())['result']
test_data_1 = json.loads(open("test_data/calm_condition.json").read())['result']
# # test_data_2 = json.loads(open("test_data/loha.json").read())['result']
# #
#
# train_data_1 = json.loads(open("train_data/number/n1.json").read())['result']
# train_data_2 = json.loads(open("train_data/number/n2.json").read())['result']
# train_data_3 = json.loads(open("train_data/number/n3.json").read())['result']
# train_data_4 = json.loads(open("train_data/number/n4.json").read())['result']
# train_data_5 = json.loads(open("train_data/number/n5.json").read())['result']
# #
# #
# # # Підготовка тестових даних
# test_data_1 = json.loads(open("test_data/number/n1.json").read())['result']
# test_data_2 = json.loads(open("test_data/number/n2.json").read())['result']
# test_data_3 = json.loads(open("test_data/number/n3.json").read())['result']
# test_data_4 = json.loads(open("test_data/number/n4.json").read())['result']
# test_data_5 = json.loads(open("test_data/number/n5.json").read())['result']