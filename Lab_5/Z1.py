import pandas as pd

def Z1():
	# 1
	d0 = {}
	with open('a.txt', 'r') as f:
		line = ''
		while True:
			line = f.readline().rstrip('\n').split()
			if not line:
				break
			else:
				d0[line[0]] = int(line[1])

	# 2
	series0 = pd.Series(d0)
	# 3
	print(f'{series0}\n')

	# 4
	print('Ученики 8 класса:')
	for student in series0[series0 == 8].index:
		print(student)
	# 5
	series0 += 1
	print(f'\nПеревод в следующий класс:\n{series0}\n')
	# 6
	print(f'Класс | Кол-во чел.\n{series0.value_counts()}\n')
	# 7
	print(series0[["Avdeev", "Leonov"]])

Z1()