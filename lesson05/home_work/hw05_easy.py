# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def createDir(path, name):
  try:
    os.mkdir(os.path.join(path, name))
    print('Директория успешно создана')
  except FileExistsError:
    print('Такая директория уже существует')

def removeDir(path, name):
  try:
    os.rmdir(os.path.join(path, name))
    print('Директория успешно удалена')
  except FileNotFoundError:
    print('Такой директории не существует')
  except OSError:
    print('Что-то не так')

# create directories

# for i in range(1,10):
#   createDir(os.getcwd(), 'dir_{}'.format(i))

# remove directories

# for i in range(1,10):
#   removeDir(os.getcwd(), 'dir_{}'.format(i))


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def listDirs(path, needPrint=True, needFiles=False):
  try:
    if needPrint:
      for x in os.listdir(path):
          if os.path.isdir(os.path.join(path, x)): print('dir -', x)
          elif os.path.isfile(os.path.join(path, x)) and needFiles: print('file -', x)
    else:
      return [x for x in os.listdir(path) if os.path.isdir(os.path.join(path, x))]
  except FileNotFoundError:
    print('Такой папки не существует')

# listDirs('.')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

from shutil import copyfile

def copyFile(path, newName):
  copyfile(path, newName)

# copyFile(__file__, '{}.copy.py'.format(__file__[:-3]))