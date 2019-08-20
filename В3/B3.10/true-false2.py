def my_func(sentinel=None, param=14):
    print("s is", sentinel)
    print("P is", param)
    if sentinel is not None:
        print("Так не работает. Указывайте только именованные аргументы")
        return
    return "пароли от всех секретов"

print(1)
my_func(20)
print(2)
my_func(param=20)
print(3)
my_func(sentinel=None)