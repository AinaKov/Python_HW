# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


path1 = '1.txt'
data1 = open(path1, 'r')
for el in data1:
    line1 = el.split('+')
    a1 = (int(line1[0].partition('x^')[2]))
data1.close()

path2 = '2.txt'
data2 = open(path2, 'r')
for el in data2:
    line2 = el.split('+')
    a2 = (int(line2[0].partition('x^')[2]))
data2.close()

line = line1 + line2
print (line)

if a1 > a2:
    n = a1
else:
    n = a2

while n > -1:
    if n > 1:
        num = 'x^' + str(n)
    elif n == 1:
        num = 'x'
    elif n == 0:
        num = '=0'
    else:
        break
    
    a = 0

    for el in line:
        if num in el:
            b = (int(el.partition(num)[0]))
            a = a + b
            print(f'{b}{num}+', end='')
            
    n = n-1

# не хватает мозгов довести свой код до конца