#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 1
Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:
имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.

Задание 2
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:
запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение.'''

# импортируем модули стандартной библиотеки uuid и datetime
#import os
import uuid
#import time
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///sochi_athletes.sqlite3"

# базовый класс моделей таблиц - WHAAATTT???
Base_class = declarative_base()


class User(Base_class):
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
    # SET the FIELDS OF TABLE
    # идентификатор пользователя, первичный ключ
    # sa - ALIAS for sqlalchemy
    # set all column in the table
    id = sa.Column(sa.Integer, primary_key=True, autoincrement=True)
    age = sa.Column(sa.Text)
    birthdate = sa.Column(sa.Text)
    gender = sa.Column(sa.Text)
    height = sa.Column(sa.Float)
    name = sa.Column(sa.Text)
    weight = sa.Column(sa.Integer)
    gold_medals = sa.Column(sa.Integer)
    silver_medals = sa.Column(sa.Integer)
    bronze_medals = sa.Column(sa.Integer)
    total_medals = sa.Column(sa.Integer)
    sport = sa.Column(sa.Text)
    country = sa.Column(sa.Text)    

    

def connect_db(db):
    """
    Устанавливает соединение к базе данных, создает таблицы, если их еще нет и возвращает объект сессии 
    """
    # создаем соединение к базе данных
    engine = sa.create_engine(db)
    # создаем описанные таблицы
    Base_class.metadata.create_all(engine)
    # создаем фабрику сессию
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()


def request_info():
    '''Requests info from CLI and returns dict()'''
    
    print('Please, input user info')
    f_name = input('Input First name: ')
    l_name = input('Input Last name: ')
    email = input('Input email: ')
    id = str(uuid.uuid4())
    if valid_email(email):
        one_user = {'id': id,
                    'first_name': f_name,
                    "last_name": l_name,
                    "email": email
                    }
        return one_user
    else:
        print('Invalid email, please try again')
        return False


def valid_email(email):
    '''Проверяет наличие хотя бы одной точки в домене и знака @ в email.
    Возвращает True, если email допустимый и False - в противном случае.'''
    
    if email.count('@') == 1:
        if len(email.split(sep = '@')) > 1 and '.' in email.split(sep = '@')[-1]: return True
        else: return False
    else: return False


def find(session, name):
    """
    Производит поиск пользователя в таблице user по заданному имени name
    """
    # находим все записи в таблице User, у которых поле User.first_name совпадает с параметром name
    query = session.query(User).filter(User.first_name == name)
    # подсчитываем количество таких записей в таблице с помощью метода .count()
    users_cnt = query.count()
    # составляем список идентификаторов всех найденных пользователей
    user_ids = [user.id for user in query.all()]
    # находим все записи в таблице LastSeenLog, у которых идентификатор совпадает с одним из найденных
    last_seen_query = session.query(LastSeenLog).filter(LastSeenLog.id.in_(user_ids))
    # строим словарь вида идентификатор_пользователя: время_его_последней_активности
    log = {log.id: log.timestamp for log in last_seen_query.all()}
    # возвращаем кортеж количество_найденных_пользователей, список_идентификаторов, словарь_времени_активности
    return (users_cnt, user_ids, log)


if __name__ == "__main__":
    pass

