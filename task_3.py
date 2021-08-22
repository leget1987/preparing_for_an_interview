# 3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации (нуль
# необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.


import random


def random_number(start, finish):
    elem_lst = []
    elem_dir = {}
    for _ in range(10):
        rnd = int((finish - start) * random.random() + start)
        elem_lst.append(rnd)
        elem_dir.update({'elem_{}'.format(rnd): rnd})
    return elem_lst, elem_dir


print(random_number(1, 71))
