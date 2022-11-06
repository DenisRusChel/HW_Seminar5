# Создайте программу для игры в ""Крестики-нолики"".

import random


game_field = ['1','2','3','4','5','6','7','8','9']
player_field = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
enemy_field = [' ',' ',' ',' ',' ',' ',' ',' ',' ',]
mark = 'X'



def printField(game_field: list):
    print(f'\n\n{game_field[0]:^5}|{game_field[1]:^5}|{game_field[2]:^5}')
    print('----------------')
    print(f'{game_field[3]:^5}|{game_field[4]:^5}|{game_field[5]:^5}')
    print('----------------')
    print(f'{game_field[6]:^5}|{game_field[7]:^5}|{game_field[8]:^5}\n\n')

def playerTurn(game_field: list, mark):
        move = int(input('Игрок делайте ваш ход: '))
        if (0 < move < 10) and game_field[move-1].isdigit():
            game_field[move-1] = mark
            return move
        else:
            print('Эта клетка занята! Сделайте другой ход. ')

def enemyTurh():
    print('Ход компьютера: ')
    while True:
        move = random.randint(0,9)
        if (0 < move < 10) and game_field[move-1].isdigit():
            game_field[move-1] = mark
            return move
            break
    
     
def setPlayerMove(move: int):
    global player_field
    player_field[move-1] = 1

def setEnemyMove(move: int):
    global enemy_field
    enemy_field[move-1] = 1

def getMark():
    global mark
    return mark

def changeMark():
    global mark
    if mark == 'O':
        mark = 'X'
    else:
        mark = 'O'




while True:
    printField(game_field)
    move = playerTurn(game_field, mark)
    printField(game_field)
    setPlayerMove(move)
    changeMark()
    move = enemyTurh()
    printField(game_field)
    setEnemyMove(move)
    changeMark()
    print(player_field)
    print(enemy_field)
    print(game_field)



    



