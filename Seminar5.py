# Задача No31.

# Последовательностью Фибоначчи называется последовательность
# чисел a0, a1, ..., an, ..., где
# a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7 Output: 21
# Задание необходимо решать через рекурсию


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

# Задача No35.

# Напишите функцию, которая принимает одно число и проверяет,
# является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
# Input: 5 Output: yes

# number = int(input('введите число: '))

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True
# if is_prime(number):
#     print("yes")
# else:
#     print("no")

# Задача No37.

# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать
# циклы (даже для ввода и вывода).
# Input: 2 -> 3 4 Output: 4 3

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

