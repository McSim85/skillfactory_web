from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlalchemy

DB_PATH = 'sqlite:///albums.sqlite3'

Base = declarative_base(DB_PATH)


class AlreadyExists(Exception):
    pass


class Album(Base):
    """Описывает структуру таблицы album для хранения музыкальной библиотеки"""
    __tablename__ = 'album'

    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True)
    year = sqlalchemy.Column(sqlalchemy.INTEGER)
    artist = sqlalchemy.Column(sqlalchemy.TEXT)
    genre = sqlalchemy.Column(sqlalchemy.TEXT)
    album = sqlalchemy.Column(sqlalchemy.TEXT)


def connect_db():
    # Создает объект сессии между базой данных классом (языком)
    engine = sqlalchemy.create_engine(DB_PATH)
    # Создаем сессию
    Sessions = sessionmaker(engine)
    return Sessions()


def find(artist):
    """Выдает список альбомов артиста или None"""
    session = connect_db()
    albums = session.query(Album).filter(Album.artist == artist).all()
    return albums


def add_album(year, artist, album, genre):
    """Добавляет альбом базу данных"""
    assert isinstance(artist, str), 'Incorrect artist'
    assert isinstance(album, str), 'Incorrect album'
    assert isinstance(genre, str), 'Incorrect genre'
    assert isinstance(year, int), 'Incorrect year'

    session = connect_db()
    already_in_db = session.query(Album).filter(Album.artist == artist, Album.album == album).first()

    if already_in_db:
        raise AlreadyExists('Альбом {} артиста {} уже есть в медиатеке'.format(album, artist))

    album = Album(artist=artist, album=album, year=year, genre=genre)
    session.add(album)
    session.commit()
    return album
