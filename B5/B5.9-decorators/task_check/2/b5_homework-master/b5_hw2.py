import time
import fibo #импорт модуля fibo - с функцией вычисления ряда Фибоначи

#Описание класса-декоратора
class Timing:
    def __init__(self, f):
        self.num_runs = 100000
        self.func_to_run = f

    def __call__(self, *args, **kwargs):
        avg = 0
        for i in range(self.num_runs):
            t0 = time.time()
            self.func_to_run(*args, **kwargs)
            t1 = time.time()
            avg += (t1 - t0)
        avg /= self.num_runs
        print("Среднее время выполнения: %.5f секунд" % (avg))
        return self.func_to_run(*args, **kwargs)

#Вызов декоратора для функции main, которая в свою очередь вызывает функцию вычисления ряда Фибоначи
@Timing
def main():
    fibo.fibo(4000000000)


if __name__ == "__main__":
    main()