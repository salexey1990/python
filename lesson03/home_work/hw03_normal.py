# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
  arr = [1, 1]
  for _ in range(m-1):
    next_int = arr[-1] + arr[-2]
    arr.append(next_int)
  return arr[n:]

print(fibonacci(1, 5))
print(fibonacci(1, 8))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
  for i in range(len(origin_list)):
    for j in range(1, len(origin_list) - i):
      if origin_list[j] < origin_list[j-1]:
        origin_list[j], origin_list[j-1] = origin_list[j-1], origin_list[j]

  return origin_list

print(sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0]))

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

def my_filter(function, iterable):
  return [x for x in iterable if function(x)]

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = my_filter(myFunc, ages)

print(adults)


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

# Имея координаты вершин, можно каждую сторону представить в виде вектора, найти его длину и воспользоваться
# свойством попарного равенства его противоположных сторон

import math

def parallelogram_test(a, b, c, d):
  section_1_length = math.sqrt((b[1]-a[1])**2 + (b[1]-a[1])**2)
  section_2_length = math.sqrt((c[1]-b[1])**2 + (c[1]-b[1])**2)
  section_3_length = math.sqrt((c[1]-d[1])**2 + (c[1]-d[1])**2)
  section_4_length = math.sqrt((d[1]-a[1])**2 + (d[1]-a[1])**2)

  return section_1_length == section_3_length and section_2_length == section_4_length

print(parallelogram_test((-6,1), (0,5), (6,-4), (0,-8)))
print(parallelogram_test((-6,1), (0,5), (6,-4), (0,-88)))

