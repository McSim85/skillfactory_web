#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Последовательность Фибоначчи определяется рекурсивно как сумма предыдущих двух членов последовательности.
Другими словами, если мы начинаем с 1 и 2, то первые несколько элементов последовательности такие:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, ...

Начиная с 1, 2, рассмотрите первые "несколько" элементов до тех пор, пока они меньше 4000000 (4 миллиона).

Если в вашем "ряду" появился элемент больше 4000000, то прекращайте считать.

Какой получился самый большой элемент последовательности? (то есть ближайший к 4 миллионам элемент последовательности Фибоначчи)

Чему равна сумма всех четных элементов вашей последовательности?
'''

#STEP1
def counter(first, second):
    '''It makes Febonacci sequence from first, second int's.'''
    
    final_list = [first, second]
    result = 0
    
    while result < 4000000:
        result = first + second
        final_list.append(result)
        *_, first, second = final_list
    else: final_list.pop()
    
    return final_list


def summ_even(src_list):
    ''' It counts all even numbers in list'''
    
    final = 0
    for i in src_list:
        if i % 2 == 0:
            final += i
   
    return final


if __name__ == '__main__':
    febonacci = counter(1, 2)
    print('самый большой элемент последовательности: ', febonacci[-1])
    print('сумма всех четных элементов вашей последовательности: ', summ_even(febonacci))
    
    

