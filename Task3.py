# Задайте список из вещественных чисел. Напишите программу, которая найдёт
# разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.20

import random

n = 5
lst = []
for i in range(n):
    lst.append(round(random.uniform(0, 10), 2))

print(f'Список случайных чисел: {lst}')

new_lst = []
for i in range(n):
    new_lst.append((lst[i] - int(lst[i])))

num_max = new_lst[0]
num_min = new_lst[0]
max = lst[0]
min = lst[0]

for i in range(n):
    if new_lst[i] > num_max:
        num_max = new_lst[i]
        max = lst[i]
    if new_lst[i] < num_min:
        num_min = new_lst[i]
        min = lst[i]

dif = round(num_max - num_min, 2)

print('Число с максимальной дробной частью: ', max)
print('Число с минимальной дробной частью: ', min)
print('Разница  дробных частей: ', dif)
