# Лабораторная работа № 1
# Макарова Полина, ПМИ-2, 21.09.2023

from random import randrange
import codecs
from Z_6 import *
from Z_7 import *

# Задание 1
def Z1():
    n = 0
    while n == 0:
        N = randrange(1, 101)
        number = 0
        run = True

        print('Угадайте число в диапазоне от 1 до 100.\n')

        while run:
            number = 0
            while not number:
                try:
                    number = int(input('Ваше число: '))
                except:
                    print('Неверно введено значение')
                    number = 0
                else:
                    if number > 100:
                        print('Число не может быть больше 100.')
                        number = 0
                    elif number < 1:
                        print('Число не может быть меньше 1.')
                        number = 0

            if number == N:
                print(f'\nВы угадали!\nЗагаданное число {N}.')
                run = False
            elif N < number:
                print(f'Загаданное число меньше {number}.')
            else:
                print(f'Загаданное число больше {number}.')

        n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 2
def Z2():
    n = 0
    a = b = c = 0
    print('Задание № 2:\nРешение квадратного уравнения вида: a*x^2 + b*x + c = 0')
    while n == 0:
        a, b, c = map(int, input('Введите значения переменных a, b и c через пробел: ').split(' '))

        D = b * b - 4 * a * c
        print('Дискриминант равен D =', D)
        if D == 0:
            X = -b / 2 * a
            print('Решение квадратного уравнения: {0}'.format(X))
        elif D > 0:
            X1 = (-b + abs(D)) / 2 * a
            X2 = (-b - abs(D)) / 2 * a
            print('Решение квадратного уравнения: {0}, {1}'.format(X1, X2))
        else:
            print('Нет действительных корней')

        n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 3
def Z3():
    # Функция NOD берётся из файла Z_7
    n = 0
    while n == 0:
        N = M = 0

        while not (N and M):
            try:
                N, M = map(int, input('N, M (через пробел): ').split(' '))
            except:
                print('Неверно введённое значение')
                N = M = 0
            else:
                if N < 1 or M < 1:
                    print('Значение не должно быть меньше 1')
                    N = M = 0

        nod = NOD(N, M)
        d = N * M // nod
        print(d)
        n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 4
def Z4():
    n = 0
    while n == 0:
        S = int(input("Введите сумму: "))
        S_inp = S
        if (S % 100 == 0):
            banknote_5000 = S // 5000
            S %= 5000
            banknote_1000 = S // 1000
            S %= 1000
            banknote_500 = S // 500
            S %= 500
            banknote_200 = S // 200
            S %= 200
            banknote_100 = S // 100
            f = codecs.open('out.txt', 'w', encoding='utf-8')
            f.write("""{} сумма
                {} банкнот по 5000
                {} банкнот по 1000
                {} банкнот по 500
                {} банкнот по 200
                {} банкнот по 100
                """.format(S_inp, banknote_5000, banknote_1000, banknote_500, banknote_200, banknote_100))
            f.close()
        else:
            print("Такую сумму снять невозможно!")

        n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 5
def Z5():
    n = 0
    while n == 0:
        file = open('Lab_1/ROBOT.txt', 'r')
        commands = file.readline().replace(" ", "").upper()
        print('ppp', commands)
        M = N = x = y = 0;
        command = ""
        valid_commands = ["N", "S", "W", "E", "X"]

        while M < 1 or M > 10 or N < 1 or N > 10:
            print('Максимальный размер комнаты 10 на 10, минимальный 1 на 1')
            M, N = map(int, input("Введите размер комнаты MxN через пробел\n").split())
        while x < 1 or x > M or y < 1 or y > N:
            print('Начальное положение робота не должно быть меньше 1 или быть дальше комнаты')
            x, y = map(int, input("Введите Начальное положение РОБОТА\n").split())

        while command != "X":
            for command in commands:
                print(command)

                if command in valid_commands:
                    if command == "N":
                        if x + 1 <= M: x += 1
                    if command == "S":
                        if x - 1 >= 1: x -= 1
                    if command == "E":
                        if y + 1 <= M: x + 1
                    if command == "W":
                        if y - 1 >= 1: y -= 1

                else:
                    print("Недопустимая команда ", command)
                print("РОБОТ находится на позиции {}, {} ".format(x, y))
        print("СТОП")
        n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 6
def Z6():
    # Берём функцию из файла Z_6
    n = 0
    while n == 0:
        bedroom()

    n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))

# Задание 7
def Z7():
    # Берём функции из файла Z_7
    n = 0
    while n == 0:
        k = 0
        fractions = []

        while not k:
            try:
                k = int(input('Введите количество дробей: '))
            except:
                print('Неверно введено значение')
                k = 0
            else:
                if k < 2:
                    print('Нужно ввести хотя бы 2 дроби.')
                    k = 0

        num = den = 0
        for i in range(k):
            print('\nДробь № {}:'.format(i + 1))

            while not den:
                try:
                    num, den = map(int, input('Введите числитель и знаменатель через слэш (/) > ').split('/'))
                except:
                    print('Неверно введённое значение.')
                    den = 0
                else:
                    if den == 0:
                        print('Знаменатель не может быть равен 0. Повторите попытку:')
                        den = 0
                    elif den < 0 or num < 0:
                        print('Нужно ввести положительные дроби. Повторите попытку:')
                        den = 0

            fractions.append((num, den))
            num = den = 0
        print()

        num1 = fractions[0][0]
        den1 = fractions[0][1]
        num3 = 0;
        den3 = 0
        for i in range(1, k):
            num2 = fractions[i][0]
            den2 = fractions[i][1]

            num3, den3 = addFraction(num1, den1, num2, den2)
            print(f'{num1}/{den1} + {num2}/{den2} = {num3}/{den3}')
            num1 = num3;
            den1 = den3

        # Вывод результата
        if num1 > den1:
            N = num1 // den1
            n = num1 % den1
            print(f'{num1}/{den1} = {N} {n}/{den1}')
        elif num1 == den1:
            print(f'{num1}/{den1} = 1')
        elif num1 == 0:
            print(f'{num1}/{den1} = 0')
        else:
            print(f'{num1}/{den1}')

    n = int(input('Введите 0 что бы повторить или другое число, для завершения: '))


if __name__ == '__main__':
    run = True
    while run:
        print('Выберите номер задания от 1 до 7: ')
        Z = int(input())
        if Z == 1:
            Z1()
            run = False
        elif Z == 2:
            Z2()
            run = False
        elif Z == 3:
            Z3()
            run = False
        elif Z == 4:
            Z4()
            run = False
        elif Z == 5:
            Z5()
            run = False
        elif Z == 6:
            Z6()
            run = False
        elif Z == 7:
            Z7()
            run = False
        else:
            print('Вы ввели неверное число')