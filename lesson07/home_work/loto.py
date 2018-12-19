#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

class Card:
   def __init__(self, player='Computer'):
      self.player = player
      self.card = self.make_card()

   def make_card(self):
      numbers = random.sample(range(1, 90), 15)
      strings = [sorted(numbers[i:i + 5]) for i in range(0, 15, 5)]
      for string in strings:
         for i in range(4):
            string.insert(random.randint(0,9), '')
      return strings

   def render_card(self):
      print('{} карта'.format(self.player))
      print('   '.join(map(str,self.card[0])))
      print('   '.join(map(str,self.card[1])))
      print('   '.join(map(str,self.card[2])))

   def check_response(self, response, current):
      for i, string in enumerate(self.card):
         for j, n in enumerate(string):
            if n == current:
               if response == 'y':
                  self.card[i][j] = '-'
                  return 0
               else:
                  return 1
      if response == 'y':
         return 1

   def is_numbers_left(self):
      for string in self.card:
         for n in string:
            if isinstance(n, int):
               return 1
      return 0


class Game:
   def __init__(self):
      self.player = input('Представьтесь пожалуйста ')
      self.pl_card = Card(self.player)
      self.cm_card = Card()
      self.num = (x for x in random.sample(range(1, 90), 89))

   def game(self):
      left = 89
      while left > 0:
         current = next(self.num)
         print('Новый бочонок: {} (осталось {})'.format(current, left))
         print()
         self.pl_card.render_card()
         print()
         self.cm_card.render_card()
         response = input('Зачеркнуть цифру? (y/n) ')
         result = self.pl_card.check_response(response, current)
         if result:
            print('Вы проиграли =(((')
            return
         pl_left = self.pl_card.is_numbers_left()
         if not pl_left:
            print('Вы победили!!!')
            return
         self.cm_card.check_response('y', current)
         cm_left = self.pl_card.is_numbers_left()
         if not cm_left:
            print('Соперник победил')
            return
         left -= 1




game = Game()
game.game()
