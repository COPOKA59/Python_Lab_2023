# Задания 2 лабораторной работы от 16 до 19 — стоимость каждого задания в баллах 2, 2, 1, 3

import random

# Задание 16
def Z16():
    #print('Введите строку, что бы расставить заглавные буквы:')
    #s = str(input())
    s = 'adawdwd awdawd aw, awdawd. awdwad !adawd! aw ?awd awda'
    s_stop = ' ,.;:!?'
    s_new = s[0].upper()

    for i in range(1, len(s)):
        b = s[i]
        if s[i] not in s_stop:
            if s[i-1] in s_stop:
                b = b.upper()
        s_new += b

    print('Данная строка: ', s)
    print('Новая строка:  ', s_new)

# Задание 17
def Z17():
    s_1 = 'AAAABCCCCCDDDD'
    s_2 = '4AB5C4D'
    ch = '23456789'

    value = 1
    s = ''
    for i in s_2:
        if i in ch:
            value = int(i)
        else:
            s += i*value
            value = 1
    print(s)
    print(s == s_1)

# Задание 18
def Z18(len):
    #len = int(input('Введите количество символов в пароле: '))
    sequence = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()-+'
    s = ''
    for i in range(len):
        s += random.choice(sequence)
    print(s)
    return s

# Задание 19
def Z19():
    up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    down = 'abcdefghijklmnopqrstuvwxyz'
    ch = '1234567890'
    simv = '!@#$%^&*()-+'
    password = {'up': '',
                'down': '',
                'ch': '',
                'simv': ''}
    #s = Z18(12)
    s = 'AbscsdbAclvbdsBE'
    if len(s) > 12:
        print('Введённый пароль: ', s)
        s_new = s
        for i in s:
            if i in up:
                password['up'] += i
            elif i in down:
                password['down'] += i
            elif i in ch:
                password['ch'] += i
            elif i in simv:
                password['simv'] += i
            else:
                print('Недопустимый символ')
        """
        if password['up'] > 0:
            if password['down'] > 0:
                if password['ch'] > 0:
                    if password['simv'] > 0:
                        print('Надёжный пароль')
                    else:
                        print('Нет спец.символов')
                else:
                    print('Нет цифр')
            else:
                print('Нет строчных букв')
        else:
            print('Нет заглавных букв')
        """
        b = True
        m = max(password['up'], password['down'], password['ch'], password['simv'])
        #print(m)
        if password['up'] == '':
            print('Нет заглавных букв')
            b = False
            for i in range(0, len(s_new)):
                if s[i] == m[1]:
                    s_new = s[:i]
                    s_new += random.choice(up)
                    s_new += s[i+1:]
            s = s_new
        if password['down'] == '':
            print('Нет строчных букв')
            b = False
            for i in range(0, len(s_new)):
                if s[i] == m[2]:
                    s_new = s[:i]
                    s_new += random.choice(down)
                    s_new += s[i + 1:]
            s = s_new
        if password['ch'] == '':
            print('Нет цифр')
            b = False
            for i in range(0, len(s_new)):
                if s[i] == m[3]:
                    s_new = s[:i]
                    s_new += random.choice(ch)
                    s_new += s[i + 1:]
            s = s_new
        if password['simv'] == '':
            print('Нет спец.символов')
            b = False
            for i in range(0, len(s_new)):
                if s[i] == m[0]:
                    s_new = s[:i]
                    s_new += random.choice(simv)
                    s_new += s[i + 1:]
            s = s_new

        if b == True:
            print('Надёжный пароль')
        print(f'\nПредлагаемый пароль: {s_new}\n')
    else:
        print('В пароле недостаточно символов')
