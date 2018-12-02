# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]

import math

list_1 = [2, -5, 8, 9, -25, 25, 4]
list_2 = []

for item in list_1:
  if item < 0:
    continue
  sqrt = math.sqrt(item)
  if sqrt == int(sqrt):
    list_2.append(int(sqrt))

print(list_2)


# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)


import locale
from datetime import datetime

#изменяем локаль
locale.setlocale(locale.LC_ALL, ('RU','UTF8'))

print("{:%B %d, %Y} года".format(datetime.strptime('2011-01-03', '%Y-%m-%d')))

# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random

from random import randint
def make_list(n = 10):
  list_1 = []
  for _ in range(n):
    list_1.append(randint(-100, 100))
  return list_1

print(make_list())


# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут: 
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

list_1 = [1, 2, 4, 5, 6, 2, 5, 2]
list_2 = []
list_3 = []

for item in list_1:
  if item in list_2:
    continue
  list_2.append(item)

print(list_2)

import collections

counter=collections.Counter(list_1)

for key, value in counter.items():
  if value == 1:
    list_3.append(key)
print(list_3)