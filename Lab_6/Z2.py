import numpy as np
import pandas as pd

def Z2():
    # Выберите все верные ответы касательно следующих четырех Series:
    # 1) Серия (1) совпадает с серией (2), так как в каждом из случаев серия создаётся из
    # списка строк
    # 2) Серия (2) совпадает с серией (3), так как в каждом из случаев серия создаётся из
    # списка символов
    # 3) Серия (1) не совпадает с серией (4), так как в (4) используются двойные кавычки
    # "" вместо одинарных ''

    print(pd.Series('abcde'))
    print(pd.Series(['abcde']))
    print(pd.Series(list('abcde')))
    print(pd.Series("abcde"))

    # Верно только 1 утверждение

#Z2()
