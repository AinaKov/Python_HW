# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num = int(input('Введите число:'))

a = '0'
b = '1'
var = ''

if num < 0:
    k = -1
else:
    k = 1

num2 = num * k

if num2 != 0:
    while num2 > 1:
        if (num2 % 2):
            var += b
        else:
            var += a
        num2 = num2 // 2
    var += b
else:
    var = a

itog = var[::-1]
itog = int(itog) * k

print(itog)
