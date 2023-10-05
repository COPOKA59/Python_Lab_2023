def robot():
    M = N = x = y = 0;
    command = ""
    valid_commands = ["N", "S", "W", "E", "X"]
    while M < 1 or M > 10 or N < 1 or N > 10:
        M, N = map(int, input("Введите размер комнаты MxN через пробел\n").split())
    while x < 1 or x > M or y < 1 or y > N:
        x, y = map(int, input("Введите Начальное положение РОБОТА\n").split())
    file = open('ROBOT.txt', 'r')
    commands = file.readline().replace(" ", "").upper()
    while command != "X":
        for command in commands:
            print(command)
            if command in valid_commands:
                if command == "N":
                    if x + 1 <= M: x += 1
                if command == "S":
                    if x - 1 >= 0: x -= 1
                if command == "E":
                    if y + 1 <= M: x + 1
                if command == "W":
                    if y - 1 >= 0: y -= 1

            else:
                print("Недопустимая команда ", command)
            print("РОБОТ находится на позиции {}, {} ".format(x, y))
    print("СТОП")