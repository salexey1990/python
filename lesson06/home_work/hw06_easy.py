# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


import math

class Triangle:
  def __init__(self, coords):
    self.__coords = coords

  @property
  def x(self):
    return self.__coords[0]

  @x.setter
  def x(self, x):
    self.__coords = x, self.__coords[1], self.__coords[2]

  @property
  def y(self):
    return self.__coords[1]

  @y.setter
  def y(self, y):
    self.__coords = self.__coords[0], y, self.__coords[2]

  @property
  def z(self):
    return self.__coords[2]

  @z.setter
  def z(self, z):
    self.__coords = self.__coords[0], self.__coords[1], z

  @property
  def a(self):
    return math.sqrt((self.z[1]-self.x[1])**2 + (self.z[0]-self.x[0])**2)

  @property
  def b(self):
    return math.sqrt((self.y[1]-self.x[1])**2 + (self.y[0]-self.x[0])**2)

  @property
  def c(self):
    return math.sqrt((self.z[1]-self.y[1])**2 + (self.z[0]-self.y[0])**2)

  @property
  def perimeter(self):
    return self.a + self.b + self.c

  @property
  def height(self):
    p = 0.5 * (self.a + self.b + self.c)
    return (2 / self.a) * (math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))

  @property
  def area(self):
    return 0.5 * self.a * self.height

triangle = Triangle(((-1, 4), (-1, 2), (-7, 3)))

print(triangle.perimeter)
print(triangle.height)
print(triangle.area)



# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

class EquilateralTrapezium:
  def __init__(self, coords):
    self.coords = coords
    self.a = coords[0]
    self.b = coords[1]
    self.c = coords[2]
    self.d = coords[3]

  @property
  def AB(self):
    return math.sqrt((self.b[1]-self.a[1])**2 + (self.b[0]-self.a[0])**2)

  @property
  def BC(self):
    return math.sqrt((self.c[1]-self.b[1])**2 + (self.c[0]-self.b[0])**2)

  @property
  def CD(self):
    return math.sqrt((self.d[1]-self.c[1])**2 + (self.d[0]-self.c[0])**2)

  @property
  def DA(self):
    return math.sqrt((self.a[1]-self.d[1])**2 + (self.a[0]-self.d[0])**2)

  @property
  def AC(self):
    return math.sqrt((self.c[1]-self.a[1])**2 + (self.c[0]-self.a[0])**2)

  @property
  def BD(self):
    return math.sqrt((self.d[1]-self.b[1])**2 + (self.d[0]-self.b[0])**2)

  @property
  def perimeter(self):
    return self.AB + self.BC + self.CD + self.DA

  @property
  def area(self):
    return ((self.DA + self.BC) / 2) * math.sqrt(self.CD ** 2 - ((self.DA - self.BC) ** 2) / 4)

  @property
  def isEquilateral(self):
    return self.AC == self.BD

trapezium = EquilateralTrapezium(((0,0),(1,1),(2,1),(3,0)))
print(trapezium.perimeter)
print(trapezium.area)
print(trapezium.isEquilateral)