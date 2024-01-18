# Семинар 15-01-24
# Задача №9. Факториал
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
# Решить задачу используя цикл while

# Input:       5
# Output:    120

# 1 Вариант
# n = int(input("Введите число:"))
# factorial = 1
# while n >1:
#     factorial *= n
#     n -= 1
# print(factorial)

# 2 Вариант
# n = int(input("Введите число:"))
# factorial = 1
# count = 2
# while count <= n
#     factorial *= count
#     count += 1
# print(factorial)


# Задача №11.  Фибоначчи
# Дано натуральное число A > 1.
# Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A.
# Если А не является числом Фибоначчи, выведите число -1.

# Input:     5
# Output:  6

# Ряд чисел Фибоначчи:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233,
# 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …

#Вариант 1

# n = int(input("введите число фибоначчи : "))

# fib_1 = 0
# fib_2 = 1
# fib_3 = fib_1+fib_2
# count = 1

# while  fib_1<n:
#     fib_1 = fib_2
#     fib_2 = fib_3
#     fib_3 = fib_1+fib_2
#     count = count +1

# if fib_1 !=n:
#     print("-1")
# else:
#     print(count)

#Вариант 2

# n = int(input("введите число фибоначчи : "))

# fib_1 = 1
# fib_2 = 1
# fib_3 = fib_1+fib_2
# count = 4

# while  fib_3<n:
#     fib_1 = fib_2
#     fib_2 = fib_3
#     fib_3 = fib_1+fib_2
#     count = count +1

# if fib_3 !=n:
#     print("-1")
# else:
#     print(count)

#Вариант 3

# n = int(input("введите число фибоначчи : "))

# fib_1 = 1
# fib_2 = 2
# count = 4

# while  fib_2<n:
#     fib_1, fib_2 = fib_2, fib_1 + fib_2 #Множественное присваивание
#     count = count + 1

# if fib_2 != n:
#     print("-1")
# else:
#     print(count)


# Задача №13.
# 1) Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
# статистики за прошлые годы. Их интересует,
# сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
# Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел. 
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# 2) Пользователь вводит число N (1 ≤ N ≤ 10).
# Далее построчно N чисел от -50 до 50.
# Нужно вывести наибольшее количество идущих подряд положительных чисел.

# Input:    6 -> -20 30 -40 50 10 -10
# Output: 2

#Вариант 1
# from random import randint #Импорт из библиотеки random функции randint (рандомные челые числа)

# days = int(input('введите количество дней: '))

# count = 0
# max_count = 0
# for i in range(days):
#     temp = randint(-50, 50)
#     print(temp, end=' ')
#     if temp >0:
#         count +=1
#         if count > max_count:
#             max_count = count
#     else:
#         count = 0
# print()
# print(max_count)

#Вариант 2
# from random import randint

# days = int(input('введите количество дней: '))

# count = 0
# max_count = 0
# for i in range(days):
#     temp = randint(-50, 50)
#     print(temp, end=' ')
#     if temp >0:
#         count +=1
#     else:
#         if count > max_count:
#             max_count = count
#         count = 0
# if count > max_count:
#     max_count = count
# print()
# print(max_count)


# Задача №15.
# 1) Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
# а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
# а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
# как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество арбузов.
# Вторая строка содержит N чисел, записанных на новой строчке каждое.
# Здесь каждое число – это масса соответствующего арбуза
# 2) Пользователь вводит одно число N.  Далее идут N чисел,
# записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)

# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# Вариант 1
# n = int(input("Введите число арбузов: "))
# min_weight = 10
# max_weight = 0
# # min_weight = float("inf")
# # max_weight = -float("inf")

# for _ in range(n):
#     weight = randint(1,10)
#     print(weight, end=" ")
#     if weight > max_weight:
#         max_weight = weight
#     if weight < min_weight:
#         min_weight = weight
# print()
# print(max_weight, min_weight)

#Вариант 2

# from random import randint

# n = int(input("Введите число арбузов: "))
# weight = randint(1, 10)
# min_weight = weight
# max_weight = weight

# for _ in range(n - 1):
#     weight = randint(1, 10)
#     print(weight, end=" ")
#     min_weight = min(weight, min_weight)
#     max_weight = max(weight, max_weight)
# print()
# print(f"{max_weight = } кг , {min_weight = } кг")


#Допольнительно (фишки)
# Срезы, диапазоны

# 0  1   2   3    4
# text = '2  3   4   5   7'
#        -5 -4  -3  -2   -1
       
# text = '23457'
# print(text[2]) -> 4
# print(text[-3]) -> 4
# print(text[1: 4]) -> '345'
# print(text[: 3]) -> '2345'
# print(text[2:]) -> '457'
# print(text[: : 2]) -> '247'

# text_2 = '234571235365676758'
# print(text_2[3: 9: 2])
# print(text_2[7: 1: -2])
# print(text_2[::-1]) #-> 857676563532175432


# range(start=0, stop, step=1)#

# range(5) -> range(start=0, stop=5, step=1) -> 0,1,2,3,4
# range(2, 10) -> range(start=2, stop=10, step=1) -> 2,3,4,5,6,7,8,9
# range(3, 15, 2) -> range(start=3, stop=15, step=2) -> 3,5,7,9,11,13
#print(*range(len(text),-1 , -1))

# new_text = 'Hello, world!'

# for symbol in new_text:
#     print(symbol)
    
# print(*range(len(new_text)))  

# for i in range(len(new_text)):
#     print(new_text[i:])


# print(new_text[-2:])
# print(int('1212341кг'[:-2]))

# for num in range(50):
#     if num % 2 == 0:
#         continue # ломает 1 круг
#     if num % 3 == 0:
#         print(num, end=' ')
#     if num == 32:
#         break # ломает весь цикл
# else:
#     print('Я всё, закончил!')