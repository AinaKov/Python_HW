
import random
from random import randint
import datetime


def wheel_of_random():
    person = []

    data_n = open('Name.txt', 'r', encoding='utf-8')
    name_r = random.choice(data_n.readlines()).split('\n')
    person.append(''.join(name_r))

    data_s = open('Surname.txt', 'r', encoding='utf-8')
    surname_r = random.choice(data_s.readlines()).split('\n')
    surname_r = ''.join(surname_r)

    if 'ж_' in person[0]:
        person[0] = person[0].replace('ж_', '')
        surname_r = surname_r + 'а'

    person.append(surname_r)

    y = random.randrange(1960, 2000)
    m = random.randrange(1, 12)
    if m == 4 or m == 6 or m == 9 or m == 11:
        d = random.randrange(1, 31)
    elif m == 2:
        d = random.randrange(1, 29)
    else:
        d = random.randrange(1, 32)

    date = datetime.date(y, m, d).strftime('%d.%m.%Y')
    person.append(date)

    data_j = open('Job.txt', 'r', encoding='utf-8')
    job_r = random.choice(data_j.readlines()).split('\n')
    person.append(''.join(job_r))

    n = random.randrange(1, 4) 

    for i in range(n):
        num = '+79'
        for i in range(9):
            num_tel = str(random.randrange(0, 9))
            num = num + num_tel
        person.append(num)
    
    return(person)
