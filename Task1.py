# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Пример:
# 6782 -> 23
# 0,56 -> 11

string = str(input('Введите число: '))
num = string.replace('.', '') 
num = int(num)
sum = 0
while num > 0:
    n = num % 10
    print(n)
    sum = sum + n
    print(sum)
    num = num // 10
    print(num)
print('Сумма цифр: ', sum)