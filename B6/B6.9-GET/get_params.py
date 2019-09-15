#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bottle import route
from bottle import run
# импортируем объект request
from bottle import request
from bottle import HTTPError

#http://localhost:8080/add?x=3&y=33
# returns
# Сумма 3 и 33 равна 36

@route("/add")
def add():
    # получаем значения GET-параметров x и y
    x = int(request.query.x)
    y = int(request.query.y)
    result = x + y
    return "Сумма {} и {} равна {}".format(x, y, result)


@route("/add2")
def add():
    try:
        x = int(request.query.x)
        y = int(request.query.y)
    except ValueError:
        result = HTTPError(400, "Некорректные параметры")
    else:
        s = x + y
        result = "Сумма {} и {} равна {}".format(x, y, s)
    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)