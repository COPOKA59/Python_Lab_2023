def bedroom():
    print("""Вы в спальне. Куда идем?
    1 - в ванную
    2 - в коридор""")

    s = input()
    if s == '1':
        bathroom()
    elif s == '2':
        hallway()
    else:
        print("Неверный ввод, попробуйте ещё раз!")
        bedroom()


def bathroom():
    print("""Вы в ванной. Куда идем?
    1 - в коридор
    2 - в спальню""")

    s = input()
    if s == '1':
        hallway()
    elif s == '2':
        bedroom()
    else:
        print("Неверный ввод, попробуйте ещё раз!")
        bathroom()


def hallway():
    print("""Вы в коридоре. Куда идем?
    1 - в спальню
    2 - в ванную
    3 - на кухню
    4 - в дверь""")

    s = input()
    if s == '1':
        bedroom()
    elif s == '2':
        bathroom()
    elif s == '3':
        kitchen()
    elif s == '4':
        print("Вы вышли из квартиры. Победа!!!")
    else:
        print("Неверный ввод, попробуйте ещё раз!")
        hallway()


def kitchen():
    print("""Вы на кухне. Куда идем?
    1 - в коридор
    2 - в окно""")

    s = input()
    if s == '1':
        hallway()
    elif s == '2':
        print("""Вы выпали в окно и разбились...
        Вы проиграли.
        Попробовать еще раз?
        1 - да""")
        s = input()
        if s == '1':
            bedroom()
    else:
        print("Неверный ввод, попробуйте ещё раз!")
        kitchen()