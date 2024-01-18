# Семинар 18-01-24 
# Задача №17.
# Решение в группах
# Дан список чисел. Определите, сколько в нем встречается различных чисел.

# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# Примечание: Пользователь может вводить значения списка или список задан изначально.


# import random

# size = int(input("Введите размер списка: "))
# # list_1 = [] 

# # for _ in range(size):
# #     num = random.randint(1, 5)
# #     list_1.append(num)
# # print(list_1)

# list_1 = [random.randint(1, 5) for _ in range(size)]
# print(list_1)

# # Вариант 1

# print(len(set(list_1)))

# # Вариант 2

# unique = []
# for num in list_1:
#     if num not in unique:
#         unique.append(num)
# print(len(unique))

# # [unique.append(num) for num in list_1 if num not in unique]

# unique_2 = [list_1[i] for i in range(len(list_1)) if list_1[i] not in list_1[i + 1:]] 
# print(len(unique_2))


# Задача №19.
# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов
# вправо, K – положительное число.

# Input: [1, 2, 3, 4, 5] k = 3
# Output:  [3, 4, 5, 1, 2]
# Примечание: Пользователь может вводить значения списка или список задан изначально.

# #Вариант 1 сдвиг в право
# n = int(input('введите количество целых чисел: '))

# numbers = [i for i in range(1, n+1)]
# print(numbers)
# k = int(input('введите K: '))
# print(numbers[-k:] + numbers[:-k])

# #Вариант 2 сдвиг влево
# n = int(input('введите количество целых чисел: '))

# numbers = [i for i in range(1, n+1)]
# print(numbers)
# k = int(input('введите K: '))
# print(numbers[k:] + numbers[:k])

# #Вариант 3 сдвиг вправо
# for _ in range(k):
#     last_num = numbers.pop()
#     numbers.insert(0, last_num)
# print(numbers)


# Задача №21.
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#  {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально. Пользователь его не вводит

# #Вариант 1
# list_dicts = [{"V": "S001", "VI":"S059"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

# unique = set()

# for cur_dict in list_dicts:
#     for value in cur_dict.values():
#         unique.add(value)
# print(unique)

# #Вариант 2
# unique = set()

# for cur_dict in list_dicts:
#     unique.add(*cur_dict.values()) работает с одним элементом в словаре
# print(unique)

# #Вариант 3
# unique = set()

# for cur_dict in list_dicts:
#     unique.update(cur_dict.values()) # работает со всеми элементами списка/словаря
# print(unique)


#Разбор функций
# my_set = {123,2345,4567,6789,890,567}
# print(my_set)
# text = 'Hello world!'
# my_tuple = (1,2,3,4,5)
# num = 55


# my_set.add(text)
# print(my_set)
# my_set.add(my_tuple)
# print(my_set)
# my_set.add(num)
# print(my_set)

# my_set.update(text)
# print(my_set)
# my_set.update(my_tuple)
# print(my_set)
# my_set.update(num)
# print(my_set)


# Задача №23. 
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]

# Output: 2 

# Пояснение: (-1 < 5, 2 < 3)

# Примечание: Пользователь может вводить значения списка или список задан изначально.

#Вариации
# numbers = []
#
# for i in range(size):
#     if i%2==0:
#         numbers.append(randint(-5, 5))
# numbers = [randint(-5, 5) for i in range(size) if i%2==0]

# for i in range(size):
#     if i%2==0:
#         numbers.append(randint(-5, 5))
#     else:
#         numbers.append("Hello")
# 
# numbers = [randint(-5, 5) if i%2==0 else "Hello" for i in range(size) ]

#Решение
# from random import randint

# size = int(input("Введите размер массива: "))
# numbers = [randint(-5, 5) for _ in range(size)]
# print(numbers)
# count = 0

# for i in range(size - 1):
#     if numbers[i] < numbers[i + 1]:
#         count += 1
# print(count)

# print(sum([1 for i in range(size - 1) if numbers[i] < numbers[i + 1]]) )


#Дополнительно
#Копирование списков
# import copy

# num = 45
# text = 'hello'
# my_list = [1,2,3,4,5, [11,22,33, [777,888,999]]]
# print(my_list)

# my_list_2 = my_list
# print(my_list_2)
# print()
# my_list_2[2] = 999
# print(my_list)
# print(my_list_2)
# print()

# my_list_3 = my_list.copy()
# print(my_list_3)
# print()
# my_list_3[3] = 0
# print(my_list)
# print(my_list_3)
# print()

# my_list_4 = my_list[:]
# print(my_list_4)
# print()
# my_list_4[-1][1] = '~~~~'
# print(my_list)
# print(my_list_4)
# print()

# my_list_5 = copy.deepcopy(my_list)
# print(my_list_5)
# print()
# my_list_5[-1][-1][1] = 'XXX'
# print(my_list)
# print(my_list_5)

#Кортеж
# import copy

# my_tuple = (1,2,3,4,5, [11,22,33, [777,888,999]])
# print(my_list)

# my_tuple_2 = my_tuple[:]
# print(my_tuple_2)
# print()
# my_tuple_2[-1][1] = '~~~~'
# print(my_tuple)
# print(my_tuple_2)
# print()

# my_tuple_3 = copy.deepcopy(my_tuple)
# print(my_tuple_3)
# print()
# my_tuple_3[-1][-1][1] = 'XXX'
# print(my_tuple)
# print(my_tuple_3)

