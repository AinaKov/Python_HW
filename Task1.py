# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

num = int(input('Введите число: '))
sum = 0
while num > 0:
    n = num % 10
    sum = sum + n
    num = num // 10
print('Сумма цифр: ', sum)