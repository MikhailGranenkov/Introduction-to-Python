# Задача No31.

# Последовательностью Фибоначчи называется последовательность
# чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 13
# Задание необходимо решать через рекурсию
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,
# 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711


# # Вариант 1

# def fib(num):
#     if num == 1 or num == 2:
#         return 1
#     return fib(num - 1) + fib(num - 2)


# n = int(input('Введите число: '))

# print(fib(n))

# # Вариант 2
# def fibonacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# n = int(input("Введите число N: "))
# result = fibonacci(n)
# print("N-е число Фибоначчи:", result)


# Задача No33.

# Хакер Василий получил доступ к классному журналу
# и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4 Output: 1 3 3 3 1

# # Вариант 1 меняет мин на макс, а макс на мин
# def replace_grades(grades):
#     max_grade = max(grades)
#     min_grade = min(grades)
#     for i in range(len(grades)):
#         if grades[i] == min_grade:
#             grades[i] = max_grade
#         elif grades[i] == max_grade:
#             grades[i] = min_grade
#     return grades

# # Пример использования
# input_grades = [1, 3, 3, 3, 4]
# output_grades = replace_grades(input_grades)
# print(output_grades)  # Вывод: 1 3 3 3 1

# # Вариант 2
# import random

# def max_to_min(numbers):
#     max_num = max(numbers)
#     min_num = min(numbers)
#     while max_num in numbers:
#         i_max_num = numbers.index(max_num)
#         numbers[i_max_num] = min_num


# n = int(input("Введите количество оценок: "))
# marks = [random.randint(1, 5) for _ in range(n)]
# print(marks)

# max_to_min(marks)
# print(marks)


# # Вариант 3 с таймингом
# import random
# import time

# n = int(input("Введите количество оценок: "))
# first_num = random.randint(1, 5)
# min_num = first_num
# max_num = first_num
# i_max_nums = [0]

# start = time.time()
# marks = [first_num]

# for i in range(1, n):
#     num = random.randint(1, 5)
#     marks.append(num)
#     if min_num > num:
#         min_num = num
#     if max_num < num:
#         max_num = num
#         i_max_nums = [i]
#     elif max_num == num:
#         i_max_nums.append(i)
# print(marks)

# for i in i_max_nums:
#     marks[i] = min_num
    
# end = time.time()
# dif = end - start
# print(f'код работал {dif} секунд')


# Задача No35.

# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# # Вариант 1
# number = int(input('введите число: '))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):  # возводим в степень 0.5 (корень квадратный)
#         if n % i == 0:
#             return False
#     return True
# if is_prime(number):
#     print("yes")
# else:
#     print("no")

# # Вариант 2
# def prime(n):
#     for div in range(2, n //2 +1):  # делим без остатка на 2 (но не работает на 3-х значных числах (например 121))
#         if n % div == 0:
#            return 'NO'
#     return 'YES'      
         
# num = int(input('введите число: '))
# print(prime(num))

# # Вариант 3 оптимизированный
# def prime(n):
#     if n != 2 and n % 2 == 0:
#         return 'NO'
#     for div in range(3, int(n ** 0.5) +1, 2):
#         if n % div == 0:
#            return 'NO'
#     return 'YES'      
         

# num = int(input('введите число: '))
# print(prime(num))


# Задача No37.

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать
# циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

# # Вариант 1
# # Заголовок функции
# def reverse_sequence(* args):
    
#     reversed_sequence = list(args[::-1])  # Переворачиваем список
    
#     return reversed_sequence  # Выводим перевернутый список на экран
# # Получаем от пользователя количество элементов последовательности
# n = int(input('Введите количество элементов: '))
# # Получаем от пользователя элементы последовательности
# sequence = list(map(int, input('Введите элементы последовательности: ').split()))
# # Вызываем функцию и выводим результат на экран
# print('Перевернутая последовательность:', reverse_sequence(* sequence))

# # Вариант 2
# # Input: 5 -> 1 2 3 4 5 Output: 5 4 3 2 1
# def reversed(num):
#     el = input("Введите число: ")
#     if num == 1:
#         print(el, end=" ")
#         return
#     reversed(num - 1)
#     print(el, end=" ")


# n = int(input("Введите количество чисел последовательности: "))

# reversed(n)

# # Вариант 3
# def reversed(num):
#     el = input("Введите число: ")
#     if num == 1:        
#         return el + ' '
#     return reversed(num - 1) + el + ' '



# n = int(input("Введите количество чисел последовательности: "))

# print(reversed(n).strip())



# Дополнительно. Функции модуля.

# # Файл modul1
# def tri(a, h):
#     return 0.5 * a * h


# def rect(a, b):
#     return a * b


# def circle(r):
#     return 3.14 * r ** 2

# #
# # def main():
# #     print("Начало модуля 1")
# #     print("Начинаем считать площадь сложной фигуры")
# #     area_1 = rect(20, 30) + tri(20, 15) - circle(5)
# #     print(f"{area_1 = }")
# #
# #     print("Конец модуля 1")
# #
# # if __name__ == '__main__':
# #     main()

# if __name__ == '__main__':
#     print("Начало модуля 1")
#     print("Начинаем считать площадь сложной фигуры")
#     area_1 = rect(20, 30) + tri(20, 15) - circle(5)
#     print(f"{area_1 = }")
#     print("Конец модуля 1")



# # Файл modul2

#     from modul_1 import *

# print("Начало модуля 2")
# area_2 = rect(200, 300) + circle(50)
# print(f"{area_2 = }")

# print("Конец модуля 2")
