import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from bottle import HTTPError
from bottle import HTTPResponse

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


def connect_db():
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии
    """
    engine = sa.create_engine(DB_PATH)
    Base.metadata.create_all(engine)
    session = sessionmaker(engine)
    return session()


def find(artist):
    """
    Находит все альбомы в базе данных по заданному артисту
    """
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums

def insert(album_data):
    """
    Вставляет альбом POST-запросом в базу данных по заданным данным
    """
    session = connect_db()
    # Создаем альбом по полученным данным
    album = Album(
        year = album_data["year"],
        artist = album_data["artist"],
        genre = album_data["genre"],
        album = album_data["album"]
    )
    albums = session.query(Album).filter(Album.year == album_data["year"], Album.artist == album_data["artist"],
                                         Album.genre == album_data["genre"], Album.album == album_data["album"]).all()
    if not albums:
        # добавляем новый альбом в сессию если не найдено полного совпадения альбомов
        session.add(album)
        # сохраняем все изменения, накопленные в сессии
        session.commit()
        message = "Альбом: %(year)s - %(artist)s - %(genre)s - %(album)s добавлен в базу" % album_data
        result = HTTPResponse(status=200, body=message)
    else:
        message = "Альбом: %(year)s - %(artist)s - %(genre)s - %(album)s уже существует в базе" % album_data
        result = HTTPError(409, message)
    return result
