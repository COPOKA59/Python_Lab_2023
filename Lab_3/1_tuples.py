# 1 tuples (с кортежами)
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


cities_with_tuples = []
location_list = []
print('\nВведите сначала название страны, а затем названия её городов. Вводится в одну строчку через пробел.')

for i in range(K):
	loc_len = 0
	while loc_len < 2:
		location_list = [s for s in input(f'{i+1}) ').split(' ') if s != '']
		loc_len = len(location_list)
		if loc_len < 2:
			print('Нужно ввести одну страну и хотя бы один город.\n')
	cities_with_tuples += [(location_list[j], location_list[0]) for j in range(1,loc_len)]
# print(cities_with_tuples)

city = ''
found = False
for i in range(3):
	city = input(f'\nВведите название {i+1}-го города > ')

	for city_tuple in cities_with_tuples:
		if city in city_tuple:
			print(f'Город {city} расположен в стране {city_tuple[1]}.')
			found = True
			break
	if not found:
		print(f'По городу {city} данных нет.')


	found = False
# 1) Россия Москва Пермь                                                                                                                                                              
# 2) Америка Вашингтон Нью-Йорк                                                                                                                                                       
# 3) Япония Токио