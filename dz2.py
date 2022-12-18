import random

name1 = input('Введите имя 1 игрока ')
name2 = input('Введите имя 2 игрока ')
player = random.randrange(1,3)

if player == 1:
    print(f'первый ход делает игрок {name1} ')
else:
    print(f'первый ход делает игрок {name2} ')

Summa_cand = int(input('Введите кол во конфет: '))

while Summa_cand:
    if Summa_cand > 28:
        player1 = int(input(f"{name1} Сколько возьмешь конфет? За раз можно максимум 28 "))
        if player1 > 28:
            print("error! Возьми меньше 29 ")
            player1 = int(input(f"{name1} Сколько возьмешь конфет? За раз можно максимум 28 "))
        Summa_cand -= player1

        if Summa_cand > 28:
            player2 = int(input(f"{name2} Сколько возьмешь конфет? За раз можно максимум 28 "))
            if player2 > 28:
                print("error! Возьми меньше 29 ")
                player2 = int(input(f"{name2} Сколько возьмешь конфет? За раз можно максимум 28 "))
            Summa_cand -= player2

            if Summa_cand <= 28:
                if player == 1:
                    print(f'Осталось {Summa_cand} конфет,а значит побеждает {name1}')
                else:
                    print(f'Осталось {Summa_cand} конфет,а значит побеждает {name2}')
        else:
            if player == 1:
                print(f'Осталось {Summa_cand} конфет,а значит побеждает {name2}')
            else:
                print(f'Осталось {Summa_cand} конфет,а значит побеждает {name1}')