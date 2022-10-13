#Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import os

data = open('file4.txt', 'r', encoding='utf-8')
lst = "".join(data.readlines())

def split(s):
    return [char for char in s]

lst1 = split(lst)

def rle_encode(X):
    rle_encode = []
    counter = 1
    for i in range(1, len(X)):
        if X[i] != X[i - 1]:
            rle_encode.append(X[i-1])
            rle_encode.append(counter)
            counter = 1
        else:
            counter += 1
    rle_encode.append(X[len(X)-1])
    rle_encode.append(counter)
    return rle_encode

def rle_decode(X):
    rle_decode = []
    for i in range(len(X)-1):
        if not i % 2:
            rle_decode.append(X[i]*X[i+1])
    return ("".join(map(str,rle_decode)))


en_co = rle_encode(lst1)
print('Код файла: ', "".join(map(str,en_co)))
de_co = rle_decode(en_co)
print('')
print('Расшифровка кода: ', de_co)

result_dir = 'file'

if not os.path.exists(result_dir):
    os.mkdir(result_dir)

with open(f'{result_dir}\\{de_co[:5]}.txt', 'w', encoding='utf-8') as file:
    file.write(de_co)







