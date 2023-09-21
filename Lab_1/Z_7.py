# поиск НОД
def NOD(a, b):
	if (a == 0):
		return b
	return NOD(b % a, a)

# сокращение дроби
def lowest(den3, num3):
	common_factor = NOD(num3, den3)

	den3 = int(den3 / common_factor)
	num3 = int(num3 / common_factor)
	return num3, den3

# Суммирование двух дробей
def addFraction(num1, den1, num2, den2):
	# поиск НОД
	den3 = NOD(den1, den2)

	# наименьший общий множитель (lcm)
	den3 = (den1 * den2) / den3

	# сумма числителей после приведения к общему знаменателю
	num3 = ((num1) * (den3 / den1) +
			(num2) * (den3 / den2))

	return lowest(den3, num3)