# Лабораторная работа № 3
# Макарова Полина, ПМИ-2, 12.10.2023

from Z1_4 import *

if __name__ == '__main__':
    run = True
    while run:
        print('Выберите номер задания от 1 до 4: ')
        Z = int(input())
        if Z == 1:
            Z1()
        elif Z == 2:
            Z2()
        elif Z == 3:
            Z3()
        elif Z == 4:
            Z4()
        else:
            print('Вы ввели неверное число')
        print('Нажмите любую цифру > 1, что бы продолжить:\nОтменить повтор 1.')
        if int(input()) == 1:
            run = False