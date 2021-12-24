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
gameplayer2 = random.choice(["ножницы","камень","бумага"])

if gameplayer2 == "камень" and gameplayer1 == "бумага":
    print("player1:", gameplayer1, "win")
    print("player2:", gameplayer2, "lose")

elif gameplayer2 == "бумага" and gameplayer1 == "камень":
    print("player2:", gameplayer2, "win")
    print("player1:", gameplayer1, "lose")

elif gameplayer2 == "бумага" and gameplayer1 == "ножницы":
    print("player1:", gameplayer1, "win")
    print("player2:", gameplayer2, "lose")

elif gameplayer2 == "ножницы" and gameplayer1 == "бумага":
    print("player2:", gameplayer2, "win")
    print("player1:", gameplayer1, "lose")

elif gameplayer2 == "камень" and gameplayer1 == "ножницы":
    print("player2:", gameplayer2, "win")
    print("player1:", gameplayer1, "lose")

elif gameplayer2 == "ножницы" and gameplayer1 == "камень":
    print("player1:", gameplayer1, "win")
    print("player2:", gameplayer2, "lose")

else:
    print("ничья")
    print("player1:", gameplayer1)
    print("player2:", gameplayer2)


