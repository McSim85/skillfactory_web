#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Веб-сервер принимает GET-запросы по адресу /albums/<artist>
и выводит на экран сообщение с количеством альбомов исполнителя artist
и списком названий этих альбомов.
Веб-сервер принимает POST-запросы по адресу /albums/
и сохраняет переданные пользователем данные об альбоме.
Данные передаются в формате веб-формы. Если пользователь пытается
передать данные об альбоме, который уже есть в базе данных,
обработчик запроса отвечает HTTP-ошибкой 409 и выводит соответствующее сообщение.
Чтобы сформировать POST-запрос к серверу можно воспользоваться уже знакомой нам утилитой http.
Допустим, мы запустили сервер по адресу http://localhost:8080. Тогда запросы будут выглядеть так:

http -f POST http://localhost:8080/albums artist="New Artist" genre="Rock" album="Super"

Дополните список передаваемых параметров, если потребуется.

3. Набор полей в передаваемых данных полностью соответствует схеме таблицы album базы данных.

4. В качестве исходной базы данных использовать файл albums.sqlite3.

5. До попытки сохранить переданные пользователем данные, нужно провалидировать их.
Проверить, например, что в поле "год выпуска" передан действительно год.
'''

from bottle import route
from bottle import run
from bottle import HTTPError
from bottle import request

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///albums.sqlite3"

Base = declarative_base()


class Album(Base):
    """
    Описывает структуру таблицы album для хранения записей музыкальной библиотеки
    """

    __tablename__ = "album"

    id = sa.Column(sa.INTEGER, primary_key=True)
    year = sa.Column(sa.INTEGER)
    artist = sa.Column(sa.TEXT)
    genre = sa.Column(sa.TEXT)
    album = sa.Column(sa.TEXT)

def connect_db(db):
    """
    Устанавливает соединение к базе данных, (#создает таблицы, если их еще нет) и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(db)
    # создаем описанные таблицы
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db(DB_PATH)
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def is_exist(album_data):
    '''Checks exist album_data in db or not and returns True or False'''
    session = connect_db(DB_PATH)
    final_album = session.query(Album).filter_by(**album_data).all()
    if final_album: return True
    else: return False

@route("/albums/<artist>")
def get_albums(artist):
    albums_list = find(artist)
    if not albums_list:
        message = "Альбомов {} не найдено".format(artist)
        result = HTTPError(404, message)
    else:
        album_names = [album.album for album in albums_list]
        result = "Total albums for {} is {}.\nList of albums:\n".format(artist,len(album_names))
        result += "\n".join(album_names)
    return result

def save_album(album_data):
    '''Saves album_data to SQLite DB '''
    session = connect_db(DB_PATH)
    session.add(Album(**album_data))
    session.commit()
    return True

def validate_data(data):
    '''Validates data and return True\False.
    It checks that in data all values is str or None.
    Next, it tries to check that data['year'] is can be int()
    Params:
    data is dict()'''
    ok = True
    all_values = []
    for v in data.values():
        all_values.append(isinstance(v, str) or v is None)
    if all(all_values):
        try:
            if data['year']: int(data['year'])
        except ValueError:
            ok = False
    return ok

@route("/albums", method="POST")
def album():
    album_data = {
        "year": request.forms.get("year"),
        "artist": request.forms.get("artist"),
        "genre": request.forms.get("genre"),
	"album": request.forms.get("album")
    }
    print(album_data)
    if is_exist(album_data):
        album_name = ', '.join([i+': '+v for i,v in album_data.items() if v])
        message = 'Same album has already exist in DB: {}'.format(album_name)
        result = HTTPError(409, message)
    else:
        if validate_data(album_data):
            save_album(album_data)
            result = "Данные успешно сохранены"
        else:
            result = 'Error in data types'

    return result



if __name__ == "__main__":
    run(host="localhost", port=8080, debug=True)
