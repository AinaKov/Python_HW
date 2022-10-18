# Напишите программу вычисления арифметического выражения заданного строкой.

# я думала над этим заданием неделю и мне чуть-чуть не хватало мозгов. 
# потом я все-таки решила посмотреть семинар с разбором этого задания 
# и, к счастью, у Александра была такая же логика выполнения. 
# Мне не хватало знаний именно о том, как разбить строку на составляющие.
# Остальное было описнао примерно также. В свою очередь хочу сказать, 
# что разобралась с функцией re.findall и добавила значения с плавающей точкой и возвдением в степень.
# а также, я написала код, который работает со скобками в скобках.
# все это я пишу, в надежде, что Вы не будете считать, что я просто списала решение.


import re

math = input('Введите выражение: ')

#math = '(30.5*(7.25-4.25))^(2+1)'

elements = re.findall(r'[\d.|\d]+|[()\^\+\-*\/]', math)

def calculator(m):
    calc = {'^': lambda x, y: x ** y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y,
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y}

    for i in range(m.count('^')):
        for el in m:
            if str(el) in '^':
                idx = m.index(el)
                res = calc[el](float(m[idx - 1]), float(m[idx + 1]))
                m[idx-1:idx+2] = [res]
                break

    for i in range(m.count('*') + m.count('/')):
        for el in m:
            if str(el) in '*/':
                idx = m.index(el)
                res = calc[el](float(m[idx - 1]), float(m[idx + 1]))
                m[idx-1:idx+2] = [res]
                break

    for i in range(m.count('-') + m.count('+')):
        for el in m:
            if str(el) in '-+':
                idx = m.index(el)
                res = calc[el](float(m[idx - 1]), float(m[idx + 1]))
                m[idx-1:idx+2] = [res]
                break
    return m

bracket = []
for i in range(len(elements)):
    if '(' == elements[i]:
        bracket.append(i)

bracket = list(reversed(bracket))

if len(bracket):
    for el in bracket:
        br = elements.index(')', el)
        res = elements[el+1:br]
        calculator(res)
        #print(res)
        elements[el:br+1] = res

#print(elements)
calculator(elements)

print(f'Ответ: {elements[0]}')