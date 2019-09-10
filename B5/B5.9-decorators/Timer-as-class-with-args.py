#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Вам предлагается написать декоратор для подобной логики, который измерял бы скорость работы функций. Как-то так:

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass
Примечания:

в данном случае внутри вложенной функции (где-то в декораторе) стоит выводить среднее время выполнения;
можно либо зафиксировать число запусков, либо передавать как параметр.
Опционально: вы можете выполнить несколько дополнительных требований и получить за них баллы:

задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера;
задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера, который можно использовать как контекстный менеджер.

Userful links
https://www.youtube.com/watch?v=Ss1M32pp5Ew
https://www.thedigitalcatonline.com/blog/2015/04/23/python-decorators-metaprogramming-with-style/

'''
import time


class Time_this:
    
    def __init__(self, num_runs=100):
        self.num_runs = num_runs

    def __call__(self, func):
#        print('__call__', a, kw)
        def run_wrapper_timer(*args):
#            print('run_wrapper_timer', args)
            avg_time = 0
            for _ in range(self.num_runs):
                t0 = time.time()
                func(*args)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= self.num_runs
            print("Выполнение заняло {} секунд".format(avg_time))
#        print('before take_func return')
        return run_wrapper_timer
    

#@Time_this(num_runs=500)
# ==same-as==
#instance = Time_this(num_runs=500) <= create instance of Time_this class
# instance.__init__(num_runs=500) => creates: self.num_runs
# instance.__call__(counter) => calls with arguments __call__ (<__main__.Time_this object at 0x0316BEB0>, <function counter at 0x031636F0>)
# ????
# 

# !!!like this!!! => ????
@Time_this(num_runs=500)
def counter(first, second):
    '''It makes Febonacci sequence from first, second int's.'''
    final_list = [first, second]
    result = 0
    
    while result < 4000000000000000000000000000000000000:
        result = first + second
        final_list.append(result)
        *_, first, second = final_list
    else: final_list.pop()
    
    return final_list


if __name__ == '__main__':
    febonacci = counter(1, 2)
    

    
    

