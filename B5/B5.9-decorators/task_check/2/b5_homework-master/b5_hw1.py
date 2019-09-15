import time
import fibo #импорт модуля fibo - с функцией вычисления ряда Фибоначи

#Описание декоратора-обертки
def time_this(num_runs=10):
    def decorator(f):
        def func(*args, **kwargs):
            avg_time = 0
            for i in range(num_runs):
                t0 = time.time()
                f(*args, **kwargs)
                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
        return func

    return decorator

#Вызов декоратора для функции main, которая в свою очередь вызывает функцию вычисления ряда Фибоначи
@time_this(1000000)
def main():
    fibo.fibo(4000000000)


if __name__ == "__main__":
    main()