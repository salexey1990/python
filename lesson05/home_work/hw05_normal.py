# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import sys
import os
import hw05_easy

current_dir = os.getcwd()

def cd(current_dir):
  dir_list = hw05_easy.listDirs(current_dir, False)
  dir_list.append('..')
  dir_name = input('Введите имя директории ')
  if dir_name in dir_list:
    return os.path.join(current_dir, dir_name)
  else:
    print('Введено не правильное имя директории')
    return current_dir

def ls(current_dir):
  hw05_easy.listDirs(current_dir, needFiles=True)

def rm(current_dir):
  dir_name = input('Введите удаляемой директории: ')
  hw05_easy.removeDir(current_dir, dir_name)

def mkdir(current_dir):
  dir_name = input('Введите имя новой директории: ')
  hw05_easy.createDir(current_dir, dir_name)

while True:
  command = input(
    '''
    1. Перейти в папку
    2. Просмотреть содержимое текущей папки
    3. Удалить папку
    4. Создать папку
    q. Завершить работу
    '''
  )

  if command == 'q':
    sys.exit()
  elif command == '1':
    current_dir = cd(current_dir)
  elif command == '2':
    ls(current_dir)
  elif command == '3':
    rm(current_dir)
  elif command == '4':
    mkdir(current_dir)
