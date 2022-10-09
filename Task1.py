# Вычислить число c заданной точностью d
#  Пример:
# при d = 0.001, π = 3.141.$ $10^{-1} ≤ d ≤10^{-10}$

from unicodedata import decimal


def rnd(x, d):
    count = 0
    while d != 1:
        d *= 10
        count += 1
    num = round(x, count)
    return(num)

x = float(input('Введите число: '))
d = float(input('Введите точность: '))

if d >= 0.1 or d <= 0.0000000001:
    print('Точность должна быть в пределах от 0,1 до 0,0000000001')
else:
    print(rnd(x, d))
