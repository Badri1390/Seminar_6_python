# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

start = int(input("Введите стартовое число: "))
step = int(input("Введите шаг прогрессии: "))
count = int(input("Введите размер массива: "))
lst = []
a = 0
lst.append(start)
for i in range(count - 1):
    start+=step
    lst.append(start)
print(lst)