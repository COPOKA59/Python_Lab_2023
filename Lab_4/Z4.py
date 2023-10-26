# Задание 4
# 26.10.2023
import numpy as np

#0. Дана квадратная матрица А nxn, все элементы которой больше или равны 0.
#1. Проверить, для всех столбцов  S[j]= ∑_(i=0)^(n-1)▒a_ij <1
#	Если для какого-то столбца это не выполняется, то изменить некоторые элементы этого столбца.
#2. Найти определитель матрицы А.
#3. Найти матрицу В = Е – А. Е – единичная матрица.
#4. Найти матрицу С равную обратной к матрице В.
#5. Задать вектор У.
#6. Найти Х= С*У
#7. Для заданной матрицы А и вектора У найти вектор Х, если А*Х + У = Х

def print_matrix(A):
    for i in range(len(A)):
        for j in range(len(A[0])):
            print(f'{A[i][j]:6.2f}', end='  ')
        print()

def Z4():
    # 0
    N = 3
    A = np.array(np.round(np.random.rand (N, N), 2))
    print(f'\nA:')
    print_matrix(A)

    # 1
    summ = A.sum(axis=0)
    for i in range(N):
        print(f'Сумма {i}-столбца: {summ[i]:2.2f}')
        if summ[i] < 1:
            print('     Сумма меньше 1')
            for j in range(N):
                if A[j, i] < 0.34 and A[j, i].sum(axis=0) < 1: A[j, i] = 0.34
            summ = A.sum(axis=0)
            print(f'Новая сумма: {summ[i]:2.2f}')
    print(f'\nA:')
    print_matrix(A)

    # 2
    print(f'\nОпределитель матрицы А: {np.linalg.det(A):2.7f}')

    # 3
    E = np.ones((N, N))
    B = np.subtract(E, A)
    print(f'\nB = Е – А:')
    print_matrix(B)

    # 4
    if np.linalg.det(B) == 0:
        print('Определитель матрицы B равен 0 ->\n невозможно найти обратную ей матрицу.\n')
    else:
        C = np.linalg.inv(B)
        print(f'\nC:')
        print_matrix(C)

    # 5
    Y = np.array([[30],[17],[10]], dtype=np.float64)
    print(f'\nY:')
    print_matrix(Y)

    # 6
    if np.linalg.det(B) != 0:
        X = np.dot(C, Y)
        print(f'\nC•Y:')
        print_matrix(X)

    # 7
    # AX + Y = X
    # AX - X = -Y
    for i in range(N):
        A[i, i] -= 1
    Y_neg = np.array([-y for y in Y])
    X_1 = np.linalg.solve(A, Y_neg)
    print(f'\n\nAx + Y = x\nx:')
    print_matrix(X_1)



Z4()