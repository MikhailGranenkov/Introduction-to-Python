# -*- coding: utf-8 -*-
"""Sem9.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TnLa-WvFKaVTsSbWlisoBckfe_-zDwsA
"""

# csv #- comma-separated values - данные разделенные запятой
# df = pd.read_csv('file.csv', # функция считывания внешнего файла формата csv (можно выбрать необходимый формат)
#                  encoding='windows-1251',
#                  headler=0,  # - какую строку считать заголовком(по умолчанию нулевую)
#                  sep = ';',
#                  index_col='название_столбца',
#                  parse_dates=['Date'],
#                  dayfirst=True)
# 'file.csv' - путь к файлу,
# sep - разделитель sep(по умолчаниию ',')
# encoding – параметр в read_csv, отвечает за кодировку текста, которая может быть различной. Самая распространённая – utf
# index_col='название_столбца' - название столбца, который будет выступать как столбец индексов
# index_col=[0] - индекс столбца, который будет выступать как столбец индексов
# parse_dates – указывает, стоит ли воспринимать даты как даты (по умолчанию они воспринимаются пандасом как строки).
    # пример pd.read_csv(path, parse_dates=['some_date', 'another_date'])
    # Параметр с датами может принимать несколько значений:
    # True – пытается перевести в дату первую колонку
    # список колонок – parse_dates=['some_date', 'another_date']
    # пытается перевести в дату указанные в списке колонки и столбцы create_data, payment_data
    # будут обрабатываться как даты
# dayfirst=True  - первое значение в дате это день или нет - True/False
# df['Date'].dt.day - номер дня недели в соответствии с данными в колонке с датами !!!!!
# df['Date'].dt.day_name() - название дня недели в соответствии с данными в колонке с датами
# df['Date'].dt.month - номер месяца в соответствии с данными в колонке с датами
# df['Date'].dt.month_name() - название месяца в соответствии с данными в колонке с датами

import pandas as pd
import numpy as np

"""## Задача №57.
1. Прочесть с помощью pandas файл california_housing_test.csv, который находится в папке sample_data
2. Посмотреть сколько в нем строк и столбцов
3. Определить какой тип данных имеют столбцы
"""

df = pd.read_csv('/content/sample_data/california_housing_test.csv')
df.sample(5)

df.shape

df.dtypes

df.info()

"""## Задача №59.
1. Проверить есть ли в файле пустые значения
2. Показать median_house_value где median_income < 2
3. Показать данные в первых 2 столбцах
4. Выбрать данные где housing_median_age < 20 и median_house_value > 70000
"""

df.isna().sum()

df[df["median_income"] < 2]["median_house_value"]

df.loc[df["median_income"] < 2, "median_house_value"]

df.head()

df[["longitude", "latitude"]]

df.columns[:2]

df[df.columns[:2]]

df.loc[:4, ["longitude", "latitude"]]

df.loc[:4, :"latitude"]

df.iloc[:, :2]

# Выбрать данные где housing_median_age < 20 и median_house_value > 70000
df[(df["housing_median_age"] < 20) & (df["median_house_value"] > 70000)]

"""## Задача №61.
1. Определить какое максимальное и минимальное значение median_house_value

2. Показать максимальное median_house_value, где median_income = 3.1250

3. Узнать какая максимальная population в зоне минимального значения median_house_value
"""

df['median_house_value'].min(), df['median_house_value'].max()

df.median_house_value.min(), df.median_house_value.max()

df[df["median_income"]==3.125]["median_house_value"].max()

df[df["median_house_value"]==df["median_house_value"].min()]["population"].max()

"""1. Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
"""

df_h = pd.read_csv("/content/sample_data/california_housing_train.csv")

df_h[df_h["population"]<=500]["median_house_value"].median()

"""1. Дан файл california_housing_train.csv.
2. Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
"""

df_h.sample(4)

min_population = df_h[df_h["population"]==df_h["population"].min()]
min_population