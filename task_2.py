# 2. Дополнить следующую функцию недостающим кодом:
# def print_directory_contents(sPath):
# """
# Функция принимает имя каталога и распечатывает его содержимое
# в виде «путь и имя файла», а также любые другие
# файлы во вложенных каталогах.
#
# Эта функция подобна os.walk. Использовать функцию os.walk
# нельзя. Данная задача показывает ваше умение работать с
# вложенными структурами.
# """

import os


def print_directory_contents(sPath):
    for child in os.listdir(sPath):
        child_path = os.path.join(sPath, child)
        if os.path.isdir(child_path):
            print_directory_contents(child_path)
        else:
            print(child_path)


print_directory_contents(os.getcwd())
