# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1,
# 4, -2, 10, 2, 0, -9, 8, 10, -9,
# 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

import random
a = int(input("Введите длину массива: "))
lst =[random.randint(-10,30) for i in range(a)]
lst_sorted = []
min = int(input("Задайте минимальное значение: "))
max = int(input("Задайте максимальное значение: "))
for i in range(len(lst)):
    if min <= lst[i] <= max:
        lst_sorted.append(i)
print(lst)
print(lst_sorted)