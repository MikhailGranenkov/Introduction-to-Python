# Фишка сплита
# text = "a a a     b     c  a   a d c d d"

# print(text.split())
# print(text.split(' '))

# Задача №25.
# Напишите программу, которая принимает на вход строку, и отслеживает,
# сколько раз каждый символ уже встречался. Количество повторов добавляется к символам
# с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию .split()


# Вариант 1
# string = "a a a b c a a d c d d"
# my_list = string.split()
# result = {}
# for el in my_list:
#     if el not in result:
#         print(el,end=" ")
#         result[el] = 0

#     else:
#         result[el] += 1
#         print(f"{el}_{result[el]}",end=" ")

# Вариант 2
# string = "a a a b c a a d c d d"
# my_list = string.split()
# result = {}
# res_str = ''
# for el in my_list:
#     if el not in result:
#         res_str += f'{el} ' 
#     else:
#         res_str += f"{el}_{result[el]} "
#     result[el] = result.get(el, 0) + 1
# res_str = res_str.rstrip()
# print(res_str)


# Задача №27.
# Пользователь вводит текст(строка).
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she
# sells are sea shells I'm sure So if she sells sea shells on the sea shore
# I'm sure that the shells are sea shore shells

# Output: 13


# my_string = "She    sells sea shells on the sea shore The shells that she sells are sea shells "\
#     "I'm sure So if she sells sea shells on the sea shore. I'm sure that the shells are sea shore shells"
# my_string = my_string.upper().replace('.','')
# my_list = my_string.split()
# print(my_list)
# print(len(set(my_list)))

# print(len(set(my_string.replace('.','').upper().split())))


# Задача №29.
# 1) Ваня и Петя поспорили, кто быстрее решит следующую задачу:
# “Задана последовательность неотрицательных целых чисел.
# Требуется определить значение наибольшего элемента последовательности,
# которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”.
# Однако 2  друга оказались не такими смышлеными.
# Никто из ребят не смог до конца сделать это задание.
# Они решили так: у кого будет меньше ошибок в коде, тот и выиграл спор.
# За помощью товарищи обратились к Вам, студентам

# 2) Задача – «На вход программе подаются натуральные числа,как только пользователь
# введёт 0 ввод прекращается. Вывести наибольший элемент получившейся последовательности». 
# Есть два кода с ошибками, нужно определить  где ошибок меньше.

# Примечание: Программные коды на следующих слайдах

# Ваня:

# n = int(input())
# max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number > n:
#        max_number = n
# print(max_number)

# Петя:

# n = int(input())
# max_number = -1
# while n < 0:
#    n = int(input())
#    if max_number < n:
#        n = max_number
# print(n)

# # Ваня:

# n = int(input())
# max_number = n # 1 max_number = 1000
# while n != 0:
#    n = int(input())
#    if max_number < n: # 2 if max_number > n
#        max_number = n
# print(max_number)




# # Петя:

# n = int(input())
# max_number = -1
# while n != 0: # 2 while n < 0:
#     if max_number < n:
#        max_number = n # 3 n = max_number
#     n = int(input()) # 1 Перенос строки
# print(max_number) # 4 print(n)


# Дополнительно.

# my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}
# print(f'{my_dict=}')
# print(f'{my_dict["Петров"]=}')
# print()
# print(my_dict)
# print(my_dict["Петров"])
# print()
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# print()
# print(f'{len(my_dict.keys())=}')
# print(f'{sum(my_dict.values())=}')
# print(f'{my_dict.items()=}')
# print()
# print(f'{list(my_dict.keys())[3]=}')
# print(f'{list(my_dict.values())=}')
# print(f'{list(my_dict.items())=}')
# print()

# for key in my_dict:
#     print(key, end='\t')
# print('\n')

# for key in my_dict.keys():
#     print(key, end='\t')
# print('\n')

# for value in my_dict.values():
#     print(value, end='\t')
# print('\n')

# for item in my_dict.items():
#     print(item, end='\t')
# print('\n')

# for key, value in my_dict.items():
#     print(key, value,sep='-', end='\t')
# print('\n')

# q,w,*e = (111,222,333)
# print(q)
# print(w)
# print(e)

# my_list = [(1,2), (11,22,33, 44), (111,222,333)]
# for q,w,*e in my_list:
#     print(q, w, e, sep='-')
    
# for key, value in my_dict.items():    
#     print(key,value, sep=': ', end='\t')
# print('\n')

# my_dict = {'Иванов':1, 'Петров': 2, 'Сидоров':3, 'Николаев':4}

# text = 'hello world!'
# text = text[6:] + ' ' + text[: 5]

# my_dict['Алексеев'] = my_dict['Петров']
# del my_dict['Петров']

# my_dict['Алексеев'] = my_dict.pop('Петров')

# from random import randint

# nums_list = [randint(1,5) for _ in range(5)]

# nums_set = {randint(1,5) for _ in range(5)}

# nums_dict = {i: randint(1,5)  for i in range(5)}

# nums_gen = (randint(1,5) for _ in range(5))

