# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень: '))
k_ch = k

print(f'Многочлен степени {k}: ', end='')

for i in range(k):
    if k_ch > 1:
        n = random.randint(0, 101)
        print(f'{n}x^{k_ch}+', end='')
        k_ch -= 1
    elif k_ch == 1:
        n = random.randint(0, 101)
        print(f'{n}x+', end='')

n = random.randint(0, 101)
print(f'{n}=0')
