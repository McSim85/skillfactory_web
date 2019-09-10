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
'''
import time


#template to tests
#def time_this(func):
#    print('here time_this')
#    print(dir())
#    print(func)
#    def run_wrapper_timer(*args):
#        print('here run_timer')
#        print(dir())
#        print(func)
#        print(dir(func))
#        func(*args)
#        print("Finish")
#    print('before return')
#    return run_wrapper_timer

def time_this(func):
    def run_wrapper_timer(*args):
        avg_time = 0
        for _ in range(100):
            t0 = time.time()
            func(*args)
            t1 = time.time()
            avg_time += (t1 - t0)
        avg_time /= 100
        print("Выполнение заняло {} секунд".format(avg_time))
    return run_wrapper_timer

#@time_this
# ==same-as==
#temp = time_this(counter) <= returns run_wrapper_timer
#temp(1,2)  <= run counter
@time_this # !!!like this!!! => time_this(counter)(1,2) =OR=> run_wrapper_timer(1,2) => counter(1,2)
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
#    print(febonacci[-1])
    

    
    

