# Introduction-to-Python


## Семинар 1 11-01-24

### Задача №1.
За день машина проезжает n километров.
Сколько дней нужно, чтобы проехать маршрут длиной m километров?
При решении этой задачи нельзя пользоваться условной конструкцией if и циклами.
Input:
n = 700км/д
s= 750км
Output:
2

### Задача №3.
В некоторой школе решили набрать три новых математических класса и оборудовать
кабинеты для них новыми партами. За каждой партой может сидеть два учащихся.
Известно количество учащихся в каждом из трех классов.
Выведите наименьшее число парт, которое нужно приобрести для них.

Input: 20 21 22(ввод чисел НЕ в одну строку)
Output: 32

### Задача №5.  
Вагоны в электричке пронумерованы натуральными числами,
начиная с 1 (при этом иногда вагоны нумеруются от «головы» поезда,
а иногда – с «хвоста»; это зависит от того, в какую сторону едет электричка).
В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j.
Он хочет определить, сколько всего вагонов в электричке.
Напишите программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать невозможно.

Input: 3 4(ввод на разных строках)
Output: 6

### Задача №7.
Дано натуральное число - год.
Требуется определить, является ли год с данным номером високосным.
Если год является високосным, то выведите YES, иначе выведите NO.
Напомним, что в соответствии с григорианским календарем, год является високосным,
(если его номер кратен 4, но не кратен 100), а также если он кратен 400.

Input: 2016
Output: YES

### Дополнительно. Разбор лекции. Фишки. Ввод-вывод.

## Dz1
### Задача 1
Найдите сумму цифр трехзначного числа n.
Результат сохраните в перменную res.
n = 123 -> res = 6 (1 + 2 + 3)
n = 100 -> res = 1 (1 + 0 + 0)

### Задача 2
Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали n журавликов.
Сколько журавликов сделал каждый ребенок, если известно,
что Петя и Сережа сделали одинаковое количество журавликов,
а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
Выведите через пробел количество журавликов, сделанных Петей, Катей и Сережей.

n = 6 -> 1 4 1  
n = 24 -> 4 16 4    
n = 60 -> 10 40 10

### Задача 3
Вы пользуетесь общественным транспортом? 
Вероятно, вы расплачивались за проезд и получали билет с номером.
Счастливым билетом называют такой билет с шестизначным номером,
где сумма первых трех цифр равна сумме последних трех.
Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
Вам требуется написать программу, которая проверяет счастливость билета с номером
n и выводит на экран yes или no.

n = 385916 -> yes
n = 123456 -> no

### Задача 4
Определите, можно ли от шоколадки размером a × b долек отломить c долек,
если разрешается сделать один разлом по прямой между дольками
(то есть разломить шоколадку на два прямоугольника).
Выведите yes или no соответственно.

Пример:
a, b, c = 3, 2, 4 -> yes
a, b, c = 3, 2, 1 -> no


## Семинар 2 15-01-24

### Задача №9. Факториал
По данному целому неотрицательному n вычислите значение n!.
N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1
Решить задачу используя цикл while

Input:       5
Output:    120

### Задача №11.  Фибоначчи
Дано натуральное число A > 1.
Определите, каким по счету числом Фибоначчи оно является,
то есть выведите такое число n, что φ(n)=A.
Если А не является числом Фибоначчи, выведите число -1.

### Задача №13.
Уставшие от необычно теплой зимы, жители решили узнать,
действительно ли это самая длинная оттепель за всю историю наблюдений за погодой.
Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями
статистики за прошлые годы. Их интересует,
сколько дней длилась самая длинная оттепель. Оттепелью они называют период,
в который среднесуточная температура ежедневно превышала 0 градусов Цельсия.
Напишите программу, помогающую синоптикам в работе.
Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
В следующих строках располагается N целых чисел. 
Каждое число – среднесуточная температура в соответствующий день.
Температуры – целые числа и лежат в диапазоне от –50 до 50

Пользователь вводит число N (1 ≤ N ≤ 10).
Далее построчно N чисел от -50 до 50.
Нужно вывести наибольшее количество идущих подряд положительных чисел.

Input:    6 -> -20 30 -40 50 10 -10
Output: 2

### Задача №15.
Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя,
а другой для тещи. Понятно, что для себя нужно выбрать арбуз потяжелей,
а для тещи полегче. Но вот незадача: арбузов слишком много и он не знает
как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!

Пользователь вводит одно число N – количество арбузов.
Вторая строка содержит N чисел, записанных на новой строчке каждое.
Здесь каждое число – это масса соответствующего арбуза
Пользователь вводит одно число N.  Далее идут N чисел,
записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)

Input:	5 -> 5 1 6 5 9
Output:	1 9

### Допольнительно (фишки). Срезы, диапазоны

## Dz2

### Задача 10:
На столе лежат n монеток.
Некоторые из них лежат вверх решкой, а некоторые – гербом.
Определите минимальное число монеток, которые нужно перевернуть,
чтобы все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
Пример использования 
На входе:
coins = [0, 1, 0, 1, 1, 0]
На выходе:
3

### Задача 10
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки.
Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа.
Примечание: числа S и P задавать не нужно, они будут передаваться в тестах.
В результате вы должны вывести все возможные пары чисел X и Y через пробел,
такие что X <= Y.

На входе:

s = 12
p = 27
На выходе:

3 9

### Задача 14
Требуется вывести все целые степени двойки (т.е. числа вида 2k),
не превосходящие числаN.

Пример

n=16
Вывод
1
2
4
8
16


## Семинар 3 18-01-24 

### Задача №17.
Решение в группах
Дан список чисел. Определите, сколько в нем встречается различных чисел.

Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6

Примечание: Пользователь может вводить значения списка или список задан изначально.

### Задача №19.
Дана последовательность из N целых чисел и число K.
Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов
вправо, K – положительное число.

Input: [1, 2, 3, 4, 5] k = 3
Output:  [3, 4, 5, 1, 2]
Примечание: Пользователь может вводить значения списка или список задан изначально.

### Задача №21.
Напишите программу для печати всех уникальных значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
 {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]

Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
Примечание: Список словарей задан изначально. Пользователь его не вводит

### Задача №23. 
Дан массив, состоящий из целых чисел.
Напишите программу, которая подсчитает количество элементов массива,
больших предыдущего (элемента с предыдущим номером) 

Input: [0, -1, 5, 2, 3]

Output: 2 

Пояснение: (-1 < 5, 2 < 3)

Примечание: Пользователь может вводить значения списка или список задан изначально.

###Дополнительно. Копирование списков. Кортеж.

## Dz3
###Задача 1
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.

Пример:

list_1 = [1, 2, 3, 4, 5]
k = 3
Вывод 1

