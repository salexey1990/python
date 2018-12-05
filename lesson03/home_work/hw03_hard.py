# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3


# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

import csv
import os

tariff_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'workers')
hours_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data', 'hours_of')

 
def make_matrix(path):
  arr = []
  with open(path, newline='') as f_obj:
    reader = csv.reader(f_obj, delimiter=' ')

    for row in reader:
      row = list(filter(None, row))
      arr.append(row)
  del arr[0]
  return arr

def calculate_salary(tariff_matrix, hours_matrix):
  salary_matrix = []

  for hours_row in hours_matrix:
    for tariff_row in tariff_matrix:
      if hours_row[0] == tariff_row[0] and hours_row[1] == tariff_row[1]:
        salary_row = []
        salary_row.append(hours_row[0])
        salary_row.append(hours_row[1])
        salary = float(tariff_row[2])
        hours_by_tariff = float(tariff_row[4])
        hours_in_fact = float(hours_row[2])
        salary_per_hour = salary / hours_by_tariff
        if hours_by_tariff >= hours_in_fact:
          salary_row.append(salary_per_hour * hours_in_fact)
        else:
          salary_row.append(salary + (hours_in_fact - hours_by_tariff) * (salary_per_hour * 2))
        salary_matrix.append(salary_row)
        break
  
  return salary_matrix
    
tariff_matrix = make_matrix(tariff_path)
hours_matrix = make_matrix(hours_path)

print(calculate_salary(tariff_matrix, hours_matrix))


# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('А'), ord('Я')+1))))
