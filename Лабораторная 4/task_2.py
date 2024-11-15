# TODO импортировать необходимые молули
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
indent = 4
ensure_ascii = False


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline='\n') as input_file:
        with open(OUTPUT_FILENAME, "w") as output_file:
            reader = csv.DictReader(input_file, delimiter=',')
            lines = [line for line in reader]
            # TODO считать содержимое csv файла
            json.dump(lines, output_file, indent=indent, ensure_ascii=ensure_ascii)
            # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
