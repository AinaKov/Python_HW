# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

n = int(input('Введите число: '))
fib_pos = []
fib_neg = []
fib1 = 0
fib2 = 1
fib_nul = [1, 0, 1]
m = n - 1

if n > 1:
    for i in range(n - 1):
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        fib_pos.append(fib_sum)

    for i in range(n - 1):
        fib_neg.append(fib_pos[m - 1] * (- 1) ** (m))
        m = m - 1

    fib = fib_neg + fib_nul + fib_pos

elif n == 1:
    fib = fib_nul

elif n == 0:
    fib = [0]

print(fib)
