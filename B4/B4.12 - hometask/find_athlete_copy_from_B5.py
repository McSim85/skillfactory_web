#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 2
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:
запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение.'''

import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
#import sqlalchemy as sa
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

# базовый класс моделей таблиц 
Base_class = declarative_base()


class User(Base_class):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    CREATE TABLE user(
    "id" integer primary key autoincrement,
    "first_name" text,
    "last_name" text,
    "gender" text,
    "email" text,
    "birthdate" text,
    "height" real);
    """

    # задаем название таблицы
    __tablename__ = 'user'
    # set all column in the table
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    first_name = sqlalchemy.Column(sqlalchemy.Text)
    last_name = sqlalchemy.Column(sqlalchemy.Text)
    gender = sqlalchemy.Column(sqlalchemy.Text)
    email = sqlalchemy.Column(sqlalchemy.Text)
    birthdate = sqlalchemy.Column(sqlalchemy.Text)
    height = sqlalchemy.Column(sqlalchemy.REAL)
    

class Athelete(Base_class):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    CREATE TABLE athelete(
    "id" integer primary key autoincrement,
    "age" integer,
    "birthdate" text,
    "gender" text,
    "height" real,
    "name" text,
    "weight" integer,
    "gold_medals" integer,
    "silver_medals" integer,
    "bronze_medals" integer,
    "total_medals" integer,
    "sport" text,
    "country" text);
    """

    # задаем название таблицы
    __tablename__ = 'athelete'
    # set all column in the table
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    age = sqlalchemy.Column(sqlalchemy.Text)
    birthdate = sqlalchemy.Column(sqlalchemy.Text)
    gender = sqlalchemy.Column(sqlalchemy.Text)
    height = sqlalchemy.Column(sqlalchemy.Float)
    name = sqlalchemy.Column(sqlalchemy.Text)
    weight = sqlalchemy.Column(sqlalchemy.Integer)
    gold_medals = sqlalchemy.Column(sqlalchemy.Integer)
    silver_medals = sqlalchemy.Column(sqlalchemy.Integer)
    bronze_medals = sqlalchemy.Column(sqlalchemy.Integer)
    total_medals = sqlalchemy.Column(sqlalchemy.Integer)
    sport = sqlalchemy.Column(sqlalchemy.Text)
    country = sqlalchemy.Column(sqlalchemy.Text)  

    

def connect_db(db):
    """
    Устанавливает соединение к базе данных, (#создает таблицы, если их еще нет) и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sqlalchemy.create_engine(db)
    # создаем описанные таблицы
    #Base_class.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def convert_date(date):
    """
    Конвертирует строку с датой в формате ГГГГ-ММ-ЧЧ в объект  datetime.date
    """
    date_list = date.split("-")
    date_int = map(int, date_list)
    return datetime.date(*date_int)
    
def user_by_date(user, session):
    """
    Finds athlee by date user
    """
    athletes = session.query(Athelete).all()
    athlete_ids = {}
    for athlete in athletes:
        date = convert_date(athlete.birthdate)
        athlete_ids[athlete.id] = date
    
    user_date = convert_date(user.birthdate)
    min_dist = None
    athlete_id = None
    athlete_db = None

    for id_, db_date in athlete_ids.items():
        dist = abs(user_date - db_date)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_
            athlete_db = db_date
    
    return athlete_id, athlete_db


def user_by_height(user, session):
    """
    Finds athlee by height user
    """
    athletes = session.query(Athelete).all()
    atlhete_id_height = {athlete.id: athlete.height for athlete in athletes}

    user_height = user.height
    min_dist = None
    athlete_id = None
    athlete_height = None

    for id_, height in atlhete_id_height.items():
        if height is None:
            continue

        dist = abs(user_height - height)
        if not min_dist or dist < min_dist:
            min_dist = dist
            athlete_id = id_
            athlete_height = height
    
    return athlete_id, athlete_height


def main():
    '''Main activity of module
    
    Without any error-checking :-( '''
    #Create session object
    querier = connect_db(DB_PATH)
    user_id = int(input('Please, input user ID (int): '))
    # add new user to DB and commit
    user_present = querier.query(User).filter(User.id==user_id).first()
    if user_present:
        print('User ', user_present.first_name, ' has present in DB. Try to find athelets')
        bd_athlete, bd = user_by_date(user_present, querier)
        height_athlete, height = user_by_height(user_present, querier)
        print(
            "Ближайший по дате рождения атлет: {}, его дата рождения: {}".format(bd_athlete, bd)
        )
        print(
            "Ближайший по росту атлет: {}, его рост: {}".format(height_athlete, height)
        )
    else:
        print('No such user')
        
#        print('User /', i.first_name, '/ has successfully added to DB!')


if __name__ == "__main__":
    main()
