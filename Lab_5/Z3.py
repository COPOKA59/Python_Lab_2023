import numpy as np
import pandas as pd

def Z3():
    # 1
    A = pd.Series([1,2,np.NaN,3,4,np.NaN,7,8,np.NaN,10])
    print(f'Создание серии:\n{A}')

    # 2
    print(f'\nЭлементы не равные NaN:\n{A[A.notnull()]}')

    # 3
    print(f'\nКорень квадратный из чисел:\n{np.sqrt(A)}')

    # 4
    print(f'\nЗамена NaN на "-1":')
    A[A.isnull()] = -1
    print(A)

Z3()