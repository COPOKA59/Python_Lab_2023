# Задание 2
# 19.10.2023

import numpy as np

def Z2():
	students = np.array(["Вася", "Коля", "Петя", "Вася", "Коля"])
	marks = np.array([
		[4,5,4,3,4,5],
		[2,3,4,3,2,3],
		[4,4,3,3,2,3],
		[5,5,5,5,4,5],
		[3,3,4,3,4,5]
		])

	name = input('Введите имя студента: ')

	students_marks = marks[students == name]
	print('\nОценки:')
	for mark in students_marks:
		for m in mark:
			print(m, end=' ')
		print()

#Z2()