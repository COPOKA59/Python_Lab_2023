import numpy as np
import pandas as pd

def Z2():
   # 1
   arr = np.random.randint(1, 101, 20)
   series = pd.Series(arr)
   print(series)

   # 2
   print(series[5:11])

   # 3
   print(series[(series >= 10) & (series <= 50)])

   # 4
   numbers = [int(input("Введите число: ")) for i in range(3)]
   print(series[series.isin(numbers)].index)

   # 5
   print(series[series.apply(lambda x: x % 2 == 0)])

   # 6
   series[series > 70] = 0
   print(series)
