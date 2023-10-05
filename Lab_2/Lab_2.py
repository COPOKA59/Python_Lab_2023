# Лабораторная работа № 2
# Макарова Полина, ПМИ-2, 29.09.2023

from Z1_10 import *
from Z11_15 import *

if __name__ == '__main__':
    run = True
    while run:
        print('Выберите номер задания от 1 до 15: ')
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
        elif Z == 8:
            Z8()
            run = False
        elif Z == 9:
            Z9()
            run = False
        elif Z == 10:
            Z10()
            run = False
        elif Z == 11:
            Z11()
            run = False
        elif Z == 12:
            Z12()
            run = False
        elif Z == 13:
            Z13()
            run = False
        elif Z == 14:
            Z14()
            run = False
        elif Z == 15:
            Z15()
            run = False
        else:
            print('Вы ввели неверное число')