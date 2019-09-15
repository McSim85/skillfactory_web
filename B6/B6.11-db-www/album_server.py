#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Написать веб-сервер, который принимает GET-запросы по пути /album/<artist>
и отвечает списком всех альбомов артиста artist. Если артист artist не зарегистрирован
в музыкальной коллекции, то есть в базе данных отсутствуют соответствующие записи,
сервер возвращает 404 ошибку.'''

from bottle import route
from bottle import run
from bottle import HTTPError

import album

@route("/albums/<artist>")
def albums(artist):
    albums_list = album.find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Список альбомов {}\n".format(artist)
        result += "\n".join(album_names)
    return result


if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
    
