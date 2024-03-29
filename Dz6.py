# Задача № 1
# Элементы из заданного диапазона
# Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума).
# На вход подается список с элементами list_1 и границы диапазона
# в виде чисел min_number, max_number.

# Пример

# На входе:

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# На выходе:

# 1
# 2
# 3
# 6
# 7
# 9
# 10
# 11
# 13
# 14
# 16
# 19

# Вариант 1
# def find_indexes(list_1, min_number, max_number):
#     indexes = []
#     for i, element in enumerate(list_1):
#         if min_number <= element <= max_number:
#             indexes.append(i)
#     return indexes

# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10

# print(*find_indexes(list_1, min_number, max_number), sep='\n')

# Вариант 2 !!!
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = 0
# max_number = 10
# for i in range(len(list_1)):
#   if min_number <= list_1[i] <= max_number:
#     print(i)


# Задача 2
# Арифметическая прогрессия
# Заполните массив элементами арифметической прогрессии.
# Её первый элемент a1 , разность d и количество элементов n будет задано автоматически.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# Пример
# На входе:

# a1 = 2
# d = 3
# n = 4
# На выходе:

# 2
# 5
# 8
# 11

# Вариант 1
# def arithmetic_progression(a1, d, n):
#     progression = [a1]
#     for i in range(1, n):
#         progression.append(progression[-1] + d)
#     return progression

# a1 = 2
# d = 3
# n = 5

# print(*arithmetic_progression(a1, d, n), sep='\n')

# Вариант 2!!!
# a1 = 2
# d = 3
# n = 5
# for i in range(n):
#   print(a1 + i * d)

