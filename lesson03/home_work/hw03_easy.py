# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
  _int = number // 1
  _fraction = number % 1
  _rounded_fraction = _fraction * 10 ** ndigits
  _int_rounded_fraction = _rounded_fraction // 1
  _fraction_rounded_fraction = _rounded_fraction % 1
  _rounded_fraction_rounded_fraction = (_fraction_rounded_fraction * 10) // 1
  if _rounded_fraction_rounded_fraction >= 5:
    _int_rounded_fraction += 1
  return((_int_rounded_fraction / 10 ** ndigits) + _int)


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
  as_string = str(ticket_number)
  if len(as_string) != 6:
    return False
  arr = [int(i) for i in as_string]
  return arr[0] + arr[1] + arr[2] == arr[3] + arr[4] + arr[5]


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
