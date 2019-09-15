#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' Написать веб-сервер, который принимает GET-запросы по пути /album/<artist>
и отвечает списком всех альбомов артиста artist. Если артист artist не зарегистрирован
в музыкальной коллекции, то есть в базе данных отсутствуют соответствующие записи,
сервер возвращает 404 ошибку.'''

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



def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

