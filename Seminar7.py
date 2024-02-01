
# Задача №47.
# 1) У вас есть код, который вы не можете менять 
# (так часто бывает, когда код в глубине программы используется множество раз 
# и вы не хотите ничего сломать): 

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))

# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation. Однако вы поняли, что для вашей текущей задачи вам
# не нужно никак преобразовывать список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# 2) Есть код:

# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#          print(‘ok’)
# else:
#          print(‘fail’)

# - В переменную transformation нужно прописать такую функцию,
#  что бы в переменной transformed_values получилась копия списка values


# transformation = lambda x: x**2
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# transformation = lambda x: x
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')


# Задача №49.  
# 1) Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет самую большую площадь.
# Напишите функцию find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая планета. Круговые орбиты не
# учитывайте: вы знаете, что у вашей звезды таких планет нет, зато искусственные
# спутники были были запущены на круговые орбиты. Результатом функции должен быть кортеж,
# содержащий длины полуосей эллипса орбиты самой далекой планеты.
# Каждая орбита представляет из себя кортеж из пары чисел - полуосей ее эллипса.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b - длины полуосей эллипса.
# При решении задачи используйте списочные выражения. Подсказка:
# проще всего будет найти эллипс в два шага: сначала вычислить самую большую площадь эллипса,
# а затем найти и сам эллипс, имеющий такую  площадь.
# Гарантируется, что самая далекая планета ровно одна

# 2) - Дан список размеров(длина, ширина) эллипсов 
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого
# большого эллипса и возвращает кортеж с его размерами.
# Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
# -   Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
# При решении задачи используйте списочные выражения.
# Гарантируется, что самый большой эллипс всего один.


# 1
# def find_farthest_orbit(list_of_orbits):
#     s_max = 0
#     for a, b in list_of_orbits:
#         if a != b:
#             s = 3.14 * a * b
#             if s > s_max:
#                 s_max = s
#                 a_b = a, b
#     return a_b
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


# 3
# def find_farthest_orbit(list_of_orbits):
#     list_of_ellips = list(filter(lambda a_b: a_b[0] != a_b[1], list_of_orbits))
#     list_of_areas = list(map(lambda a_b: pi * a_b[0]*a_b[1], list_of_ellips))
#     max_area = max(list_of_areas)
#     i_max_area = list_of_areas.index(max_area)
#     return list_of_ellips[i_max_area]


# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


# 2
# def find_farthest_orbit(list_of_orbits):
#     list_of_ellips = [a_b for a_b in list_of_orbits if a_b[0] != a_b[1]]
#     list_of_areas = [a * b * pi for a, b in list_of_ellips]
#     max_area = max(list_of_areas)
#     i_max_area = list_of_areas.index(max_area)
#     return list_of_ellips[i_max_area]
#
#
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(find_farthest_orbit(orbits))


# Задача №51.
# Напишите функцию same_by(characteristic, objects), которая проверяет,
# все ли объекты имеют одинаковое значение некоторой характеристики, и возвращают True,
# если это так. Если значение характеристики для разных объектов отличается - то False.
# Для пустого набора объектов, функция должна возвращать True.
# Аргумент characteristic - это функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод:							               Вывод:
# values = [1, 21, 101, 61]		               same
# if same_by(lambda x: x % 2 == 0, values):
# 	print(‘same’)
# else:
# 	print(‘different’)


# 1
# def same_by(characteristic, objects):
#     return len(set(map(characteristic, objects))) < 2


# values = [11, 21, 101, 61]
# if same_by(lambda x: x % 2 == 0, values):
#     print("same")
# else:
#     print("different")


# 2
# def same_by(characteristic, objects):
#     new_list = list(filter(characteristic, objects))
#     # print(f"{objects=}")
#     # print(f"{new_list=}")
#     return objects == new_list or not new_list


# values = [11, 21, 101, 61]
# if same_by(lambda x: x % 2 == 0, values):
#     print("same")
# else:
#     print("different")


# 3
# def same_by(characteristic, objects):
#     new_list = list(map(characteristic, objects))
#     print(f"{new_list=}")
#     return any(new_list) == all(new_list) or not new_list


# values = [10, 20, 100, 61]
# if same_by(lambda x: x % 2 == 0, values):
#     print("same")
# else:
#     print("different")



# Дополнительно. Функции высшего порядка.


# def my_lambda(x, y):
#     return x * y

# my_lambda(2,3)

# f = lambda x, y: x * y

# f(2,3)




# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = filter(lambda x: x % 2 == 0, my_list)
# print(*res_list)
# print(list(res_list))




# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = list(filter(lambda x: x % 2 == 0, my_list))
# print(res_list)

# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     if f(el):
#         res_list.append(el)
# print(res_list)

# f = lambda x: x % 2 == 0
# [el for el in my_list if f(el)]
# print(res_list)




# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = map(lambda x: x % 2 == 0, my_list)
# print(*res_list)
# print(list(res_list))




# my_list = [1,2,34,5,7,8,90,0,3,67,89,35,2]

# res_list = list(map(lambda x: x % 2 == 0, my_list))
# print(res_list)
# #2
# res_list=[]
# f = lambda x: x % 2 == 0
# for el in my_list:
#     res_list.append(f(el))
# print(res_list)
# #3
# f = lambda x: x % 2 == 0
# [f(el) for el in my_list]
# print(res_list)


# print(all([True, True, True, True]))
# print(all([True, False, True, True]))
# print(all([False, False, False, False]))
# print()
# print(any([True, True, True, True]))
# print(any([True, False, True, True]))
# print(any([False, False, False, False]))
# print()
# print(all([1, 2, 3, 4]))
# print(all([1, 0, 3, 4]))
# print(all([0, 0, 0, 0]))
# print()
# print(any([1, 2, 3, 4]))
# print(any([1, 0, 3, 4]))
# print(any([0, 0, 0, 0]))
# print()
# print(all(['dfg', 'sdf', 'sdf', 'cvb']))
# print(all(['dfg', '', 'sdf', 'cvb']))
# print(all(['', '', '', '']))
# print()
# print(any(['dfg', 'sdf', 'sdf', 'cvb']))
# print(any(['dfg', '', 'sdf', 'cvb']))
# print(any(['', '', '', '']))
# print()
# print(all([[''], ('',), {''}, ['']]))
# print(all([[''], [], [''], ['']]))
# print(all([{}, {}, {}, []]))
# print()
# print(any([[''], ('',), {''}, ['']]))
# print(any([[''], [], [''], ['']]))
# print(any([{}, {}, {}, []]))
# print()


