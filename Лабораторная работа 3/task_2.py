# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, separator=','):
    first_group = set(first.split(separator))
    second_group = set(second.split(separator))
    intersection = list(first_group.intersection(second_group))
    intersection.sort()
    return intersection


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
find_common_participants(participants_first_group, participants_second_group, '|')
