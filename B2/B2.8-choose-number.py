#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Используем функцию random.randint для реализации уже знакомой нам игры
“Угадай число” на Python. Сравните её с реализацией этой игры на JavaScript в уроке A5.9. 

Вспомним формальные условия задачи. У нас есть целое число на отрезке от 1 до 100,
у пользователя есть 10 попыток, чтобы его угадать. Если число, выбранное пользователем,
меньше или больше загаданного, выводим соответствующее сообщение и количество оставшихся попыток.

1. Есть начальное случайное число (a) и загадываемое число (b).
2. Количество попыток ограничено - 10.
3. Если a > b или a < b  - нужно вывести сообщение о том, что начальное число больше или меньше загадываемого соответственно и уменьшить число попыток.
4. Если a === b - объявить победу и заменить число a на случайное другое. Также нужно обновить количество попыток (эти действия назовем инициализацией). 
5. Кстати о попытках. Если число попыток упало до нуля - объявить поражение и сделать инициализацию.
'''
import random

tries = 10
start_n = 1
stop_n = 100
propsed = random.randint(start_n, stop_n)
requested_n = int(input('Input the number: '))

while tries:
    if requested_n > propsed:
        print('Inputed number > then propsed')
        tries -= 1
        requested_n = int(input('Input the number: '))
        
    elif requested_n < propsed:
        print('Inputed number < then propsed')
        tries -= 1
        requested_n = int(input('Input the number: '))
        
    elif requested_n == propsed:
        print('Bingo')
        print(propsed)
        break
        
else:
    print('No more tries.\nExit')


