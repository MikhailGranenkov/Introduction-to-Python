# Задача 1.
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.


# Вариант 1
# import pandas as pd

# # Загрузка данных из файла
# data = pd.read_csv("california_housing_train.csv")

# # Выбор данных, где количество людей от 0 до 500
# filtered_data = data[(data['population'] >= 0) & (data['population'] <= 500)]

# # Рассчет средней стоимости дома для выбранных данных
# avg = filtered_data['median_house_value'].mean()

# print(f"Средняя стоимость дома для домов с числом жителей от 0 до 500: {avg}")


# Вариант 2
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  # Средняя стоимость дома, где количество людей от 0 до 500




# Задача 2.
# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального
# значения переменной min_population и сохраните это значение в переменную
# max_households_in_min_population.
# Используйте модуль pandas.


# Вариант 1
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')

# max_households_in_min_population = df[df['population'] == df['population'].min()]['households'].max()


# Вариант 2
# import pandas as pd

# df = pd.read_csv('california_housing_train.csv')
# # Найти минимальное значение 'population'
# min_population = df['population'].min()

# # Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
# max_households_in_min_population = df[df['population'] == min_population]['households'].max()

