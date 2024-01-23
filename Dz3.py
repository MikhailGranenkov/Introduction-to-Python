# Задача 1
# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
# Найдите количество и выведите его.

# Пример:

# list_1 = [1, 2, 3, 4, 5]
# k = 3
# Вывод 1

import random

size = int(input("Введите размер списка: "))
k = int(input("Введите число k: "))
list_1 = [] 
for _ in range(size):
    num = random.randint(0, 10)
    list_1.append(num)
count = list_1.count(k)
print(list_1)
print(count)