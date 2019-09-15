
import time

def time_this(num_runs=10):
    print(num_runs)
    def decorator(func):
        def wrap():

            avg_time = 0
            for _ in range(num_runs):
                t0 = time.time()

                func() # для обертки

                t1 = time.time()
                avg_time += (t1 - t0)
            avg_time /= num_runs
            print("Выполнение заняло %.5f секунд" % avg_time)
            return func() # сама функция со ()
        return wrap # указатель на функцию без ()
    return decorator



#@time_this(num_runs=10)
#def f():
#    for j in range(1000000):
#        pass


# f() - не использую ее, эта функция для примера

@time_this(num_runs=100)
def fibonachi():
    f_list = [1, 2]

    while f_list[-1] + f_list[-2] < 400000000:
        f_list.append(f_list[-1] + f_list[-2])

    return f_list


print(fibonachi())