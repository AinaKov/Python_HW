# Дана последовательность чисел. Получить список уникальных элементов 
# заданной последовательности, список повторяемых и убрать дубликаты 
# из заданной последовательности.
# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

import random

n = int(input('Введите количество символов: '))
lst =[]
for i in range(n):
    lst.append(random.randint(0, 10))

print('Исходный список: ', lst)


dup = [el for i, el in enumerate(lst) if i != lst.index(el)]
new_lst = [el for i, el in enumerate(lst) if el not in dup]
uniq_lst = []
for el in lst:
        if el not in uniq_lst:
            uniq_lst.append(el)
        

print('Список повторяющихся элементов: ', dup)
print('Список неповторяющихся элементов: ', new_lst)
print('Список уникальных элементов: ', uniq_lst)
