"""
Написать игру “камень-ножницы-бумага”.
Первому игроку предмет выпадает случайно.
За второго игрока предмет выбирает пользователь. На ваше усмотрение, можно также выдавать второму игроку предмет случайно.
Игра пишет, кому какой предмет выпал, и пишет результат.

Например:
Игрок1: камень
Игрок2: бумага
Бумага накрыла камень. Игрок2 победил.
"""
import random

gameplayer1 = input("камень-ножницы-бумага?")
gameplayer2 = random.choice(["ножницы", "камень", "бумага"])

if gameplayer1 == gameplayer2:
    print("ничья")

elif gameplayer1== "камень":
    if gameplayer2== "ножницы":
        print("player1:", gameplayer1, "win")
        print("player2:", gameplayer2, "lose")
    else:
        print("player2:", gameplayer2, "win")
        print("player1:", gameplayer1, "lose")

#else:
       # print("player2:", gameplayer2, "win")
        #print("player1:", gameplayer1, "lose")


