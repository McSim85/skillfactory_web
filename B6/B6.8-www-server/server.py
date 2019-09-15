#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# импортируем необходимые сущности библиотеки bottle
from bottle import route
from bottle import run
from bottle import HTTPError  # Импортируем класс HTTPError

# регистрируем обработчик пути /hello/ с помощью декоратора route
@route("/hello/")
def hello_world():
    return "<H2>Hello World!</H2>"  # Возвращаем приветственное сообщение

# if /upper/test it returns TEST web page
@route("/upper/<param>")
def upper(param):
    return param.upper()

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

@route("/fib/<n>")
def fib_handler(n):
    result = fib(int(n))
    return str(result)

@route("/modify/<param>/<method>")
def modify(param, method):
    # проверяем переданный модификатор и готовим соответствующий результат
    if method == "upper":
        result = param.upper()
    elif method == "lower":
        result = param.lower()
    elif method == "title":
        result = param.title()
    else:
        # если нам передан неизвестный модификатор, готовим ответ для пользователя 
        result = HTTPError(400, "incorrect `method` value")
    return result


if __name__ == "__main__":
    # Запускаем веб-сервер с помощью функции run: указываем адрес узла и порт
    run(host="localhost", port=8080, debug=True)
    # Булев флаг debug=True запускает сервер в режиме отладки
