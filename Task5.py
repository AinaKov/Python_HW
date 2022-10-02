# 5. Реализуйте алгоритм перемешивания списка.
import random

array = []
n = 5
print('Введите элементы массива:')
for i in range(n):
    array.append(input())
print(array)

# этот способ я нашла  в интернете
newarr = sorted(array, key=lambda A: random.random())
print(newarr)

#самый простой 
random.shuffle(array)
print(array)
