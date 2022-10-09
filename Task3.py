# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.

import random


n = int(input('Введите количество символов: '))
lst =[]
for i in range(n):
    lst.append(random.randint(0, 10))

print('Исходный список: ', lst)

dup = [el for i, el in enumerate(lst) if i != lst.index(el)]
new_lst = [el for i, el in enumerate(lst) if el not in dup]

print('Список неповторяющихся элементов: ', new_lst)

