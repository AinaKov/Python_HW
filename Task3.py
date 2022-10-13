
import random
import os

# не могу подключить numpy

board = [7, 8, 9, 4, 5, 6, 1, 2, 3]
os.system('cls||clear')

def draw_board(board):
   print(f'\nИгровое поле \n\n {board[0]} | {board[1]} | {board[2]} \n___|___|___ \n {board[3]} | {board[4]} | {board[5]} \n___|___|___ \n {board[6]} | {board[7]} | {board[8]} \n   |   |   ')

def check_win(board):
   comb_win = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for ind in comb_win:
       if board[ind[0]] == board[ind[1]] == board[ind[2]]:
          return board[ind[0]]
   return False

def input_symbol(symb):
   valid = False
   while not valid:
      move = input(f'Выбираем место для {symb} ')
      try:
         move = int(move)
      except:
         print("Ошибка. Введите число с игрового поля")
         continue
      if move >= 1 and move <= 9:
         if(str(board[board.index(move)]) not in 'XO'):
            board[board.index(move)] = symb
            valid = True
         else:
            print('Эта ячейка занята')
      else:
         print("Ошибка. Введите число с игрового поля")

# def out_red(text):
#     print("\033[31m".format(text))


name1 = input('Введите имя 1 игрока: ')
os.system('cls||clear')
name2 = input('Введите имя 2 игрока: ')
os.system('cls||clear')
name = [name1, name2]
player1 = random.choice(name)
player2 = [pl for pl in name if pl not in player1]
player2 = ''.join(player2)

print('Первым ходит ', player1)
nxt = input()
os.system('cls||clear')

def play(board):
   count = 0
   win = False
   while not win:
      os.system('cls||clear')
      draw_board(board)
      if not count % 2:
         player = player1
      else:
         input_symbol('O')
         player = player2
      count += 1
      if count > 4:
         tmp = check_win(board)
         if tmp:
            print(player, "выиграл!")
            win = True
            break
      if count == 9:
         print('Игра окончена. Ничья')
         break
      draw_board(board)
      
play(board)
