# 4. Задайте список из N элементов, заполненных числами из промежутка 
# [-N, N]. Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input('Введите число N: '))
f = open('file.txt')
fd = (f.readlines())
spisok = []
sum = 1
for i in range(N * 2 + 1):
    spisok.append(int(fd[-N + i]))
    sum = sum * spisok[i]
print('Список: ', spisok)
print('Произведение элементов: ', sum)