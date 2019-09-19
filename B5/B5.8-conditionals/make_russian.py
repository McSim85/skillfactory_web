#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Мы не могли не заметить, что студенты нашего курса ценят грамотность и уважают русский язык.
Так вот. Одна из самых популярных проблем в разработке веб-сервисов,
использующих русский язык, — согласование числа с существительными ("У вас 7 сообщения", "Ваш баланс 42 рубль").

Этой проблемы не возникало, когда мы изучали программу, описывающую игру в преферанс.
Все варианты читались нормально. А если у нас языковые конструкции сложнее?
Мы все равно хотим видеть грамотные варианты ответа.

Напишите функцию с названием make_russian, которая принимает на вход число,
а в ответ выдает строку "студент" в соответствующем склонении:

make_russian(42) -> "42 студента"
make_russian(40) -> "40 студентов"
make_russian(333) -> "333 студента"

Функции может попасться на ввод любое число от 1 до 5000 включительно.
'''

def make_russian(num):
    '''It returns str with correct form of word студент.'''
    a = tuple(str(i) for i in range(2,5))
    ov = tuple(str(i) for i in range(5,21))
    ov += ('0',)
    
    if str(num).endswith(ov): return str(num) + ' студентов'
    if str(num).endswith(a):return str(num) + ' студента'
    if str(num).endswith('1'): return str(num) + ' студент'


if __name__ == '__main__':
    for i in range(900,1020):
        print(make_russian(i))
    
    
