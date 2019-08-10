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

def init():
    '''Made init of game and return the dict() with params'''
    
    tries = 10
    start_n = 1
    stop_n = 100
    propsed = random.randint(start_n, stop_n)
    return {'tries': tries,
            'start_n': start_n,
            'stop_n': stop_n,
            'propsed': propsed}


def req_num():
    ''' Requests and Returns requested number as int()'''
    return int(input('Input the number: '))


def win(requested_n, propsed):
    '''Check, win or not win and returns True or False '''
    
    if requested_n > propsed:
        print('Inputed number > then propsed')
        return False
        
    elif requested_n < propsed:
        print('Inputed number < then propsed')
        return False
        
    elif requested_n == propsed:
        print('Bingo')
        print(propsed)
        return True

def check_yn(param):
    while True:
        if param == 'y': return True
        elif param == 'n':  return False
        else: print('Please, input (y/n)')
        
    
def main():
    source_param = init()
    print(source_param)
    while True:
        requested_n = req_num()
        if win(requested_n, source_param['propsed']):
            again = input("Whuld you like to start again? (y/n): ")
            if check_yn(again): source_param = init()
            else: break
        else:
            source_param['tries'] -= 1
            print('Left tries: ', source_param['tries'])
            if source_param['tries'] == 0:
                source_param = init()
                print('No more tries. Start again!')


main()


