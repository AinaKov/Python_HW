# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. 
# Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


import random
import os

num = 2021
lim = 28
os.system('cls||clear')

game = int(input(f'На столе {num} конфета, возьмите не больше {lim} штук. \nВыигрывает тот, кто забрал конфеты последним. \nСколько игроков 1 или 2? '))
os.system('cls||clear')

if game == 1 or game == 2:
    balance = num
    count = 0

    name1 = input('Введите имя 1 игрока: ')
    os.system('cls||clear')

    if game == 2:
        name2 = input('Введите имя 2 игрока: ')
        name = [name1, name2]
        player1 = random.choice(name)
        player2 = [pl for pl in name if pl not in player1]
        player2 = ''.join(player2)
        
        os.system('cls||clear')
        print('Первым начинает: ', player1)
        nxt = input()

        while balance > 0:
            os.system('cls||clear')
            print(f'Осталось {balance} конфет')

            player = player1 if not count % 2 else player2

            sweet = int(input(f'{player}, cколько конфет Вы возьмете? '))
            if sweet <= lim and sweet > 0:
                balance -= sweet
                count += 1
            elif sweet > lim:
                print('Вы взяли слишком много')
                nxt = input()
            else:
                print('Нужно взять конфеты')
                nxt = input()
    else:
        player1 = name1
        player2 = 'Компьютер'

        while balance > 0:
            os.system('cls||clear')
            print(f'Осталось {balance} конфет')

            if not count % 2:
                player = player1
                sweet = int(input(f'{player1}, cколько конфет Вы возьмете? '))
                if sweet <= lim and sweet > 0:
                    balance -= sweet
                    count += 1
                elif sweet > lim:
                    print('Вы взяли слишком много')
                    nxt = input()
                else:
                    print('Нужно взять конфеты')
                    nxt = input()
            else:
                player = player2
                if balance > lim * 2 :
                    sweet = random.randint(1, lim + 1)
                elif lim + 1 < balance <= lim * 2:
                    sweet = balance - (lim + 1)
                elif balance < lim + 1:
                    sweet = balance
                elif balance == lim + 1:
                    sweet = random.randint(1, lim + 1)
                    print(f'Вы не оставили мне шансов')

                print(f'Я взял {sweet} конфет')
                nxt = input()
                balance -= sweet
                count += 1

    os.system('cls||clear')
    print(f'Игра окончена\nВыиграл(а) {player}')
  
else:
    print('Введите 1 или 2')