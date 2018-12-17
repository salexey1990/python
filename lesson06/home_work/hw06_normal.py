# Задание-1:
# Реализуйте описаную ниже задачу, используя парадигмы ООП:
# В школе есть Классы(5А, 7Б и т.д.), в которых учатся Ученики.
# У каждого ученика есть два Родителя(мама и папа).
# Также в школе преподают Учителя. Один учитель может преподавать 
# в неограниченном кол-ве классов свой определенный предмет. 
# Т.е. Учитель Иванов может преподавать математику у 5А и 6Б,
# но больше математику не может преподавать никто другой.

class School:
  def __init__(self, number):
    self.number = number
    self.teachers = []
    self.students = []
    self.classes = [
      
    ]

  def add_teacher(self, teacher):
    for existing_teacher in self.teachers:
      if existing_teacher.subject == teacher.subject:
        return('It`s not possible to hire one more {} teacher'.format(teacher.subject))
    self.teachers.append(teacher)

  def get_teachers_names(self):
    return ['{} is a {} teacher'.format(x.get_full_name(), x.subject) for x in self.teachers]

class Person:
  def __init__(self, name, surname, birth_date):
    self.name = name
    self.surname = surname
    self.birth_date = birth_date

  def get_full_name(self):
    return self.name + ' ' + self.surname

  def set_name(self, new_name):
    self.name = new_name

  def set_surname(self, new_surname):
    self.surname = new_surname


class Student(Person):
  def __init__(self, name, surname, birth_date, class_room):
    Person.__init__(self, name, surname, birth_date)
    self._class_room = {'class_num': int(class_room.split()[0]),
                        'class_char': class_room.split()[1]}

  def next_class(self):
    self._class_room['class_num'] += 1

  @property
  def class_room(self):
    return "{} {}".format(self._class_room['class_num'], self._class_room['class_char'])

class Teacher(Person):
  def __init__(self, name, surname, birth_date, teach_classes, subject):
    Person.__init__(self, name, surname, birth_date)
    self.teach_classes = list(map(self.convert_class, teach_classes))
    self.subject = subject

  def convert_class(self, class_room):
    """
    '<class_num> <class_int>' --> {'class_num': <class_num>, 'class_int': <class_int>}
    """
    return {'class_num': int(class_room.split()[0]),
            'class_char': class_room.split()[1]}

  @property
  def classrooms(self):
    return ["{} {}".format(x['class_num'], x['class_char']) for x in self.teach_classes]

class Parent(Person):
  def __init__(self, name, surname, birth_date, status = 'mam', children = []):
    Person.__init__(self, name, surname, birth_date)
    self.status = status
    self.children = children

  def get_children_name(self):
    return [x.get_full_name() for x in self.children]

school = School(4)
student_a = Student('Ivan', 'Ivanov', '1.1.1990', '1 a')
student_b = Student('Petr', 'Petrov', '1.1.1990', '2 b')
math_teacher = Teacher('Cidr', 'Cidorod', '1.1.1970', ('1 a', '2 b'), 'math')
math_teacher_1 = Teacher('Cidr_1', 'Cidorod_1', '1.1.1970', ('1 a', '2 b'), 'math')
mam_a = Parent('Galina', 'Ivanova', '1.1.1970', children=[student_a])
dad_a = Parent('Igor', 'Ivanov', '1.1.1970', 'dad', [student_a])
print('{} is a {} of {}'.format(mam_a.get_full_name(), mam_a.status, mam_a.get_children_name()))
print('{} is a {} of {}'.format(dad_a.get_full_name(), dad_a.status, dad_a.get_children_name()))
print('{} is a {} ticher in {} classes'.format(math_teacher.get_full_name(), math_teacher.subject, math_teacher.classrooms))
print(school.add_teacher(math_teacher))
print(school.add_teacher(math_teacher_1))
print('{} teach in {} school'.format(school.get_teachers_names(), school.number))

# Выбранная и заполненная данными структура должна решать следующие задачи:
# 1. Получить полный список всех классов школы
# 2. Получить список всех учеников в указанном классе
#  (каждый ученик отображается в формате "Фамилия И.О.")
# 3. Получить список всех предметов указанного ученика 
#  (Ученик --> Класс --> Учителя --> Предметы)
# 4. Узнать ФИО родителей указанного ученика
# 5. Получить список всех Учителей, преподающих в указанном классе
