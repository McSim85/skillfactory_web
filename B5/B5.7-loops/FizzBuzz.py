#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
STEP1
Напишите функцию, которая принимает на вход число, а в ответ выводит:

Fizz, если число делится на 3;
Buzz, если число делится на 5;
FizzBuzz, если число делится и на 3, и на 5.
Покажите вывод функции для чисел от 1 до 100.

STEP2
Рассмотрим все (целые, натуральные, скучные) числа от 1 до 10. Среди них на 3 и/или 5 делятся 3, 5, 6 и 9. Их сумма будет равна 23.

STEP3
Вопросы
Чему равна сумма всех чисел, делящихся на 3 и/или 5, если мы переберем все натуральные числа от 1 до 1000 (не включительно)? В ответ введите целое число

STEP4
Чему равна сумма всех чисел, делящихся на 3 и/или 5 и/или 7, если мы переберем все натуральные числа от 1 до 10000 (не включительно)? В ответ введите целое число'''

#STEP1
def fizz_buzz(num):
    '''It returns str Fizz if num is divided by 3 to get quotient whithout remainder.
    It returns str Buzz if num is divided by 5 to get quotient whithout remainder.
    It returns str FizzBuzz if num is divided by 3 and 5 to get quotient whithout remainder.'''
    
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else: return False


def main(end):
    '''It print results of checking  natural numbers until end by fizz_buzz'''
    
    for i in range(end)[1:]:
        result = fizz_buzz(i)
        if result: print(str(i) + result)


#STEP2
def fizz_buzz_st2(num):
    '''It returns True if num is divided by 3 and/or 5 to get quotient whithout remainder.
    '''
    
    if num % 3 == 0 or num % 5 == 0:
        return True
    else: return False


def main_st2(end):
    '''It sums all numbers in interval from 1 till end,
    which divided by 3 and/or 5 to get quotient whithout remainder'''
    
    final = 0
    for i in range(end)[1:]:
        result = fizz_buzz_st2(i)
        if result:
            final += i
    
    return final

#STEP4
def fizz_buzz_st4(num, divisioner_list):
    '''It returns True if num is divided by one of divisioner_list to get quotient whithout remainder.
    :num - int
    :divisioner_list - list of int
    '''
    
    for i in divisioner_list:
        if num % i == 0: return True
    
    return False


def main_st4(end):
    '''It sums all numbers in interval from 1 till end,
    which divided by 3 and/or 5 and\or 7 to get quotient whithout remainder'''
    
    final = 0
    for i in range(end)[1:]:
        result = fizz_buzz_st4(i, [3,5,7])
        if result:
#            print(i)
            final += i
    
    return final


if __name__ == '__main__':
    #STEP1
    #    main(100)
    
    #STEP2
    print('Сумма всех (целые, натуральные, скучные) чисел, делящихся на 3 и/или 5, от 1 до 10 равна ', main_st2(10))
    #STEP3
    print('Cумма всех чисел, делящихся на 3 и/или 5, если мы переберем все натуральные числа'
            ' от 1 до 1000 (не включительно) равна ', main_st2(1000))
    #STEP4
    print('Cумма всех чисел, делящихся на 3 и/или 5 и/или 7, если мы переберем все натуральные числа от 1 до 10000 (не включительно)', main_st4(10000))
    

