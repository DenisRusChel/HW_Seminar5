# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

player1 = 'Игрок 1'
player2 = 'Игрок 2'
total_sweets = 150

priority = randint(0,2) #  чья очередь 
if priority == 1:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")


def movePlayer(name):
    quantity = int(input(f"{name}, введите количество конфет от 1 до 28: "))
    while quantity < 1 or quantity > 28:
        quantity = int(input(f"{name}, введите корректное количество конфет: "))
    return quantity


def resultMove(name, res, counter, total_sweets):
    print(f"Ходил {name}, он взял {res}, теперь у него {counter}. Осталось на столе {total_sweets} конфет.")



counter1 = 0 
counter2 = 0

while total_sweets > 28:
    if priority:
        res = movePlayer(player1)
        counter1 += res
        total_sweets -= res
        priority = False
        resultMove(player1, res, counter1, total_sweets)
    else:
        res = movePlayer(player2)
        counter2 += res
        total_sweets -= res
        priority = True
        resultMove(player2, res, counter2, total_sweets)

if priority:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")