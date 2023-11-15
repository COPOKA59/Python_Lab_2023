import numpy as np
import pandas as pd

def Z5():
    # 1. Загрузите данные из файла в объект DataFrame, Добавьте заголовки к
    # столбцам: «index», «year», «month», «day», «min_t», «average_t», «max_t»,
    # «rainfall».
    # Расшифровка:
    #  index – индекс ВМО,
    #  year – год,
    #  month – месяц,
    #  day – день,
    #  min_t – минимальная температура воздуха,
    #  average_t – средняя температура воздуха,
    #  max_t – максимальная температура воздуха,
    #  rainfall – количество осадков

    df = pd.read_table('wr88125.txt', encoding='utf-8', sep=';', header=None)  # na_values='     '
    df.columns = ["index", "year", "month", "day", "min_t", "average_t", "max_t", "rainfall"]

    # 2. Удалите столбец index.
    df = df.drop("index", axis=1)

    df = df.replace(r'^\s*$', np.nan, regex=True)
    print(df[df.index == 2074])
    print(df[df.index == 2074].values)

    # 3. Используя метод info(), oтветьте на вопросы:
    # 3.1. Есть ли в данных пропущенные значения?
    # 3.2. В каком столбце данных больше всего пропущенных значений?
    print('\ndf.info() >>> ')
    df.info()
    print('<<<\n')
    # Ответы на вопросы:
    # 1) Да, пропущенные значения есть
    # 2) Больше всего данных пропущено в max_t

    # 4. В данных за какой год больше всего пропусков?
    print(f'\nБольше всего пропусков за {df.isnull().groupby(df["year"]).sum().sum(axis=1).idxmax()} год.\n')

    # 5. Объедините столбцы «Год», «Месяц» и «День» в один столбец «Дата» в
    # формате гггг-мм-дд (2000-01-20). Данные в новом столбце должны иметь
    # формат datetime;
    df["date"] = pd.to_datetime(df[['year', 'month', 'day']])

    # 6. Для каждого наблюдения рассчитайте размах температур (разность
    # максимальной и минимальной суточных температур) и количество
    # предшествующих ему дней без осадков (используйте циклы Python и
    # условный оператор):
    df["min_t"] = pd.to_numeric(df["min_t"])
    df["max_t"] = pd.to_numeric(df["max_t"])
    df["average_t"] = pd.to_numeric(df["average_t"])
    df["rainfall"] = pd.to_numeric(df["rainfall"])

    df["temp_dif"] = np.nan
    df["no_rains"] = np.nan
    df.loc[df.index == 0, "temp_dif"] = df["max_t"][0] - df["min_t"][0]
    df.loc[df.index == 0, "no_rains"] = 0
    #df["temp_dif"][0] = df["max_t"][0] - df["min_t"][0]
    #df["no_rains"][0] = 0

    days_count = 0
    rows = df.shape[0]
    temp_dif = None
    for i in range(1, rows):
        days_count = 0
        for j in range(i - 1, -1, -1):
            if df["rainfall"][j] == 0:
                days_count += 1
            else:
                break
        df.loc[df.index == i, "temp_dif"] = df["max_t"][i] - df["min_t"][i]
        df.loc[df.index == i, "no_rains"] = days_count

    # 7. Определите самый длинный период засухи
    idLast = df["no_rains"].idxmax()
    print(f'Самый длительный период засухи: с {df["date"][idLast - df["no_rains"][idLast]].date()} до {df["date"][idLast - 1].date()}.')

    # 8. Для каждого года вычислите среднегодовую температуру и общее количество
    # осадков. Запишите результаты в объекты Series.
    # 8.1. Какой год можно считать самым теплым? Какой самым холодным?
    # 8.2. В какой год выпало больше всего осадков? В какой меньше всего?
    avgTemp = pd.Series(df.groupby(df["year"])["average_t"].mean())
    rainfall = pd.Series(df.groupby(df["year"])["rainfall"].sum())
    print('\nКакой год можно считать самым теплым? Какой самым холодным?')
    print(f'{avgTemp.idxmax()} > {avgTemp.max():.5f}')
    print(f'{avgTemp.idxmin()} > {avgTemp.min():.5f}')
    print('\nВ какой год выпало больше всего осадков? В какой меньше всего?')
    print(f'{rainfall.idxmax()} > {rainfall.max()}')
    print(f'{rainfall.idxmin()} > {rainfall.min()}')

    # 9. Выведете наблюдения, удовлетворяющие условиям:
    # 9.1. Средняя температура воздуха ниже -30 оС (для некоторых регионов
    # можно использовать -10 оС, -35оС, -40 оС).
    # 9.2. Средняя температура воздуха выше 27оС и количество дней без осадков
    # больше 3.
    print('\n\nСредняя температура воздуха ниже -30 оС (для некоторых регионов можно использовать -10 оС, -35оС, -40 оС)')
    print(df[df["average_t"] < -30])
    print('\n\nСредняя температура воздуха выше 27оС и количество дней без осадков больше 3')
    print(df[(df["average_t"] > 27) & (df["no_rains"] > 3)])

#Z5()