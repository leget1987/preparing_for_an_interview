# 4. Написать программу, в которой реализовать две функции. В первой должен создаваться простой текстовый файл.
# Если файл с таким именем уже существует, выводим соответствующее сообщение.
# Необходимо открыть файл и подготовить два списка: с текстовой и числовой информацией.
# Для создания списков использовать генераторы. Применить к спискам функцию zip().
# Результат выполнения этой функции должен должен быть обработан и записан в файл таким образом,
# чтобы каждая строка файла содержала текстовое и числовое значение. Вызвать вторую функцию.
# В нее должна передаваться ссылка на созданный файл.
# Во второй функции необходимо реализовать открытие файла и простой построчный вывод содержимого.
# Вся программа должна запускаться по вызову первой функции.
import os
import random
from functools import reduce


def get_random_string():
    return reduce(lambda string, char: string + char, [chr(random.randint(ord('a'), ord('z'))) for _ in range(20)])


def create_text_file(name):
    if os.path.isfile(name):
        print('Файл с таким именем уже существует')
        return False
    with open(name, 'w', encoding='utf-8') as f:
        numbers = [random.randint(0, 100) for _ in range(20)]
        strings = [get_random_string() for _ in range(20)]
        f.writelines(['{} {}\n'.format(number, text) for number, text in zip(numbers, strings)])
    print_text_file(f)


def print_text_file(desc):
    with open(desc.name, 'r', encoding='utf-8') as f:
        for line in f:
            print(line)


create_text_file("new.txt")
