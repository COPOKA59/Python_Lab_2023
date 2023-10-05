# Задания 2 лабораторной работы от 1 до 10 — стоимость каждого 1 балл
# Макарова Полина, ПМИ-2, 29.09.2023

import random

# Задание 1
def Z1():
    s = input('Введите строку: ')
    n = int(input('Введите 1 или 2 способ: '))
    if n == 1:
        print(s[0], s[len(s) - 1])
    elif n == 2:
        for i in range(0, len(s)):
            if i == 0:
                print(s[i])
            if i == len(s) - 1:
                print(s[i])
    else:
        print('Неверно введены данные')

# Задание 2
def Z2():
    x, y = map(float, input('Введите два числа через пробел ').split(' '))
    print('Сложение двух чисел: {0}'.format(x*y))

# Задание 3
def Z3():
    s = input('Введите строку: ')
    n = int(input('Введите 1 или 2 способ: '))
    if n == 1:
        print(s[0] + s[1], s[len(s) - 2:])
    elif n == 2:
        for i in range(0, len(s)):
            if i == 0:
                print(s[i] + s[i + 1])
            elif i == len(s) - 1:
                print(s[i - 1] + s[i])
    else:
        print('Неверно введены данные')

# Задание 4
def Z4():
    n = int(input('Введите 1 или 2 способ: '))
    years_list = []
    if n == 1:
        print('1 способ:')
        for i in range(6):
            years_list.append(int(input('Введите год, когда вам было {0}:\n'.format(i))))
        print('Список: ', years_list)
        return years_list
    elif n == 2:
        print('2 способ:')
        years_list.append(int(input('Введите дату вашего рождения: ')))
        for i in range(5):
            years_list.append(years_list[0]+1+i)
        print('Список: ', years_list)
        return years_list
    else:
        print('Неверно введены данные')

# Задание 5
def Z5():
    years_list = Z4()
    print('Третий год рождения: {0}'.format(years_list[3]))

# Задание 6
def Z6():
    things = ["mozzarella", "cinderella", "salmonella"]
    print('Начальный список', things)
    things[1] = things[1].upper()
    print('Доработанный список', things)

# Задание 7
def Z7():
    things = ["mozzarella", "cinderella", "salmonella"]
    print('Начальный список', things)
    things.remove("cinderella")
    print('Доработанный список', things)

# Задание 8
def Z8():
    print('Сгенерировнный список от 0 до 14 нечётных чисел')
    list = [c for c in range(0, 15) if c % 2 != 0]
    print(list)

# Задание 9
def Z9():
    print('Сгенерировнный список случайных чисел от 0 до 140: ')
    list = [random.randint(0, 141) for i in range(10)]
    print(list)
    print('Все элементы списка с чётными индексами: ')
    new_list = [list[i] for i in range(len(list)) if i % 2 == 0]
    print(new_list)

# Задание 10
def Z10():
    list = [random.randint(0, 141) for i in range(10)]
    print('Сгенерированный список: ')
    print(list)
    new_list = [list[i] for i in range(1, len(list)) if list[i - 1] < list[i]]
    print(new_list)