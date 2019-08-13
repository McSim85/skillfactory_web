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

secret = random.randint(1, 100)

# инициализируем переменную guess
guess = -1
# в переменной attempt будем хранить счетчик использованных пользователем попыток
attempt = 0
# пока предположение пользователя не совпадает с секретом
while guess != secret:
    # просим пользователя ввести очередное предположение и сохраняем его в переменную
    guess_string = input('Угадай загаданное число: ')
    # приводим значение к типу int
    guess = int(guess_string)
    # увеличиваем на единицу счетчик попыток
    attempt += 1
    # проверяем результат и распечатываем пользователю подсказку
    if guess < secret:
        print('Я загадал число больше, попробуй еще раз.')
    elif guess > secret:
        print('Я загадал число меньше, попробуй еще раз.')
# выход из цикла означает, что guess == secret поздравляем пользователя и указываем количество использованных попыток
print('Верно! Количество использованных попыток: ', attempt)

