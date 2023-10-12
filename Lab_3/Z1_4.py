# Задания 3 лабораторной работы от 1 до 4 — стоимость каждого 2,5 балла
# Макарова Полина, ПМИ-2, 29.09.2023

import random

# Задание 1
def Z1():
    K = None
    while K == None:
        try:
            K = int(input('Введите количество стран > '))
        except:
            print('Неверное значение. Повторите попытку.\n')
        else:
            if K < 1:
                print('Значение должно быть положительным числом.\n')
                K = None

    # countries = {}
    cities = {}
    location_list = []
    print('\nВведите сначала название страны, а затем названия её городов. Вводится в одну строчку через пробел.')

    for i in range(K):
        loc_len = 0
        while loc_len < 2:
            location_list = [s for s in input(f'{i + 1}) ').split(' ') if s != '']
            loc_len = len(location_list)
            if loc_len < 2:
                print('Нужно ввести одну страну и хотя бы один город.\n')
        # countries[location_list[0]] = {location_list[j] for j in range(1, loc_len)}
        cities.update({location_list[j]: location_list[0] for j in range(1, loc_len)})

    city = ''
    found = False
    for i in range(3):
        city = input(f'\nВведите название {i + 1}-го города > ')

        # for key in countries.keys():
        # 	if city in countries[key]:
        # 		print(f'Город {city} расположен в стране {key}.')
        # 		found = True
        # 		break
        # if not found:
        # 	print(f'По городу {city} данных нет.')

        if city in cities.keys():
            print(f'Город {city} расположен в стране {cities[city]}.')
        else:
            print(f'По городу {city} данных нет.')
        found = False
    # 1) Россия Москва Пермь
    # 2) Америка Вашингтон Нью-Йорк
    # 3) Япония Токио

# Задание 2
def Z2():
    N = None
    while N == None:
        try:
            N = int(input('Введите количество заказов > '))
        except:
            print('Неверное значение. Повторите попытку.\n')
        else:
            if N < 1:
                print('Значение должно быть положительным числом.\n')
                N = None
    orders = {}  # {'personA': {'pizza1': 3, 'pizza2': 1}, 'personC': {}, 'personB': {}}
    orders_with_tuples = {}  # {'personA': [('pizza1', 3), ('pizza2', 1)], 'personC': {}, 'personB': {}}
    orders_list = []
    print('\nВведите имя заказчика, название пиццы и её количество поочерёдно через пробел.')

    for i in range(N):
        check = False
        list_len = 0
        while not check:
            orders_list = [s for s in input(f'{i + 1}-й заказ > ').split(' ') if s != '']
            list_len = len(orders_list)
            if list_len != 3:
                print('Нужно ввести ровно 3 элемента: имя заказчика, название пиццы, её количество.\n')
            elif not orders_list[2].isdigit():
                print('Последний элемент должен быть числом.\n')
            else:
                orders_list[2] = int(orders_list[2])
                check = True

        if orders_list[0] in orders.keys():
            if orders_list[1] in orders[orders_list[0]].keys():
                orders[orders_list[0]][orders_list[1]] += orders_list[2]
            else:
                orders[orders_list[0]][orders_list[1]] = orders_list[2]
        else:
            orders[orders_list[0]] = {orders_list[1]: orders_list[2]}

    orders = dict(sorted(orders.items()))
    for person in orders.keys():
        orders[person] = dict(sorted(orders[person].items()))
    for person in orders.keys():
        print(f'{person}:')
        for pizza in orders[person].keys():
            print(f'\t{pizza} {orders[person][pizza]}')

    # Максим Пепперони 1
    # Алиса Итальянская 2
    # Алиса Итальянская 1
    # Алиса Американо 1
    # Максим Маргарита 2

# Задание 3
# https://metanit.com/python/tutorial/3.4.php
def Z3():
    N = int(input('Введите максимальное возможное число: '))
    Z = random.randint(1, N+1)
    yesSet = set()
    noSet = set()
    intSet = set()

    while len(yesSet) != 1 or len(intSet) != 1:
        a = input('Введите предпологаемые числа: ').split()
        if a == ['FFF']:
            print('Возможные числа: ')
            if len(yesSet) == 0:
                for i in range(1, N+1):
                    if i not in noSet:
                        yesSet.add(i)
                print(yesSet)
            else:
                print(yesSet)
        else:
            intSet = set([int(val) for val in a])
            if Z in intSet:
                if len(intSet) == 1:
                    print('Вы угадали число !')
                    yesSet = intSet
                else:
                    print('Да')
                    if len(yesSet) == 0:
                        yesSet = intSet
                    else:
                        yesSet = yesSet.intersection(intSet)
            else:
                print('Нет')
                noSet = noSet.union(intSet)
                yesSet = yesSet.difference(noSet)
                print('Что бы попросить помощь напишите: FFF')


# Задание 4
def Z4():
    file = open('ROD.txt', 'r')
    N = int(input('Введите кол-во человек в древе: '))
    ch = {}
    rod = {}
    print('Пара: имя_потомка имя_родителя:')
    for i in range(1, N):
        potomok, predok = file.readline().replace("\n", "").split(' ')
        #ch[i] = (potomok, predok)
        #print(f'{i} пара: ', ch[i][0], ch[i][1])
        ch[potomok] = predok
        print(f'{i} пара: ', potomok, predok)
        # Если предка нет в словаре:
        if rod.get(predok) == None:
            rod[predok] = 0
            # Если потомок в словаре существует:
            if rod.get(potomok) != None:
                # Назначаем потомку соответствующее значение:
                rod[potomok] = rod[predok] + 1
                # Выбираем те ключи, где обновилось значение потомка от предка:
                keys = [key for key in ch if ch[potomok] == predok]
                # Изменяем значение:
                if keys != []:
                    print('keys: ', keys)
                    for i in keys:
                        rod[i] += 1
        # Устанавливаем значение потомка:
        rod[potomok] = rod[predok] + 1
    rod = dict(sorted(rod.items()))
    print(rod)
    print(ch)