# Задания 2 лабораторной работы от 11 до 15 — стоимость каждого задания в баллах 2, 1, 2, 1, 1
# Макарова Полина, ПМИ-2, 29.09.2023

# Задание 11
def multiplication(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return x * y
    else:
        return -1

def Z11():
    list = []
    for i in range(0, 10):
        if multiplication(i, i) != -1:
            list.append(i)
    print(list)

# Задание 12
def Z12():
    s = "aboba abobus"
    s1 = s[s.find(" ") + 1:] + " " + s[:s.find(" ")]
    print(s1)

# Задание 13* Посмотреть дома
def Z13():
    a = set(input('Введите числа через пробел: '))
    b = -1
    for i in a:
        b += 1
    print(b)

# Задание 14*
def Z14():
    s = input()
    s1 = s[::-1]
    if s == s1:
        print(s, "=", s1)
    else:
        print(s, "!=", s1)

# Задание 15*
def Z15():
    sum = 0
    x = 0
    while x != "stop":
        sum += int(x)
        x = input()

    print(sum)