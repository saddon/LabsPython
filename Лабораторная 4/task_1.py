# TODO решите задачу
import json


def task() -> float:
    input_filename = "input.json"
    with open(input_filename) as file:
        data = json.load(file)
    sum_of_products = sum(i.get("score") * i.get("weight") for i in data)
    return round(sum_of_products, 3)


print(task())
