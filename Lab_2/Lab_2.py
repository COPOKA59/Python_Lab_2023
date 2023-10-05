# Лабораторная работа № 2
# Макарова Полина, ПМИ-2, 29.09.2023

from Z1_10 import *
from Z11_15 import *
from Z16_19 import *

if __name__ == '__main__':
    run = True
    while run:
        print('Выберите номер задания от 1 до 15: ')
        Z = int(input())
        if Z == 1:
            Z1()
        elif Z == 2:
            Z2()
        elif Z == 3:
            Z3()
        elif Z == 4:
            Z4()
        elif Z == 5:
            Z5()
        elif Z == 6:
            Z6()
        elif Z == 7:
            Z7()
        elif Z == 8:
            Z8()
        elif Z == 9:
            Z9()
        elif Z == 10:
            Z10()
        elif Z == 11:
            Z11()
        elif Z == 12:
            Z12()
        elif Z == 13:
            Z13()
        elif Z == 14:
            Z14()
        elif Z == 15:
            Z15()
        elif Z == 16:
            Z16()
        elif Z == 17:
            Z17()
        elif Z == 18:
            Z18()
        elif Z == 19:
            Z19()
        else:
            print('Вы ввели неверное число')
        print('Нажмите любую цифру > 1, что бы продолжить:\nОтменить повтор 1.')
        if int(input()) == 1:
            run = False