# Задайте натуральное число N. Напишите программу, которая составит список 
# простых множителей числа N.

def natur(x):
    lst = []
    n = 2
    while x >= n:
        if not x % n:
            lst.append(n)
            x = x / n
        else:
            n += 1
    return lst

print(natur(int(input('Введите число: '))))
