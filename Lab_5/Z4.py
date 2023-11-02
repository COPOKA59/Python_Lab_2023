import pandas as pd
import numpy as np
import lxml
import html5lib
from bs4 import BeautifulSoup

def Z4():
    # 1
    df = pd.read_csv('Lab_5/marks.csv', encoding = 'windows-1251', sep = ';')

    # 2
    print(f'��� �������:\n{df.to_string()}\n')

    # 3
    print(f'������ 50 ��������:\n{df.head(50)}\n')

    # 4
    url = "https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2_%D0%B8_%D0%B7%D0%B0%D0%B2%D0%B8%D1%81%D0%B8%D0%BC%D1%8B%D1%85_%D1%82%D0%B5%D1%80%D1%80%D0%B8%D1%82%D0%BE%D1%80%D0%B8%D0%B9_%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D1%8B"
    table = pd.read_html(url, match='(���������� ��������)')[0]
    print(f"{table[['�������� (����������� ��������)', '�������']]}\n")

    # 5
    print(f'���������� �����: {len(table)}, ���������� ��������: {len(table.columns)}.')