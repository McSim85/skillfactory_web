#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Задание 2
Напишите модуль find_athlete.py поиска ближайшего к пользователю атлета. Логика работы модуля такова:
запросить идентификатор пользователя;
если пользователь с таким идентификатором существует в таблице user, то вывести на экран двух атлетов: ближайшего по дате рождения к данному пользователю и ближайшего по росту к данному пользователю;
если пользователя с таким идентификатором нет, вывести соответствующее сообщение.'''

from datetime import datetime, date

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
    session = sessionmaker(engine)
    # возвращаем сессию
    return session()

def user_by_date(user, session):
    '''It finds user by near date to current user'''
    final_user_id = None
    ref_time = date.fromisoformat(user.birthdate)
    final_date = None
    user_dates = {}
    for athelet in session.query(Athelete).all():
        user_dates[athelet.id] = date.fromisoformat(athelet.birthdate)
    
    for user_id, dates in user_dates.items():
        # check, that final_date is not None
        if final_date:
            # check which timedelta longer between current user and final_date
            timedelta_btw_final = final_date - dates
            timedelta_btw_ref = ref_time - dates
            if timedelta_btw_ref < timedelta_btw_final:
#                print('here')
                final_date = dates
                final_user_id = user_id
        else:
            final_date = dates
            final_user_id = user_id

    final = session.query(Athelete).filter(Athelete.id==final_user_id).first()
    return final

def user_by_height(user, session):
    '''It finds user by near date to current user'''
    final_user_id = None
    ref_height = user.height
    final_height = None
    user_heights = {}
    for athelet in session.query(Athelete).filter(Athelete.height!=None).all():
        user_heights[athelet.id] = athelet.height
#    print(user_heights)
    for user_id, height in user_heights.items():
        # check, that final_date is not None
        if final_height:
            # check which delta longer between current user and final_date
            heightdelta_btw_final = final_height - height
            heightdelta_btw_ref = ref_height - height
            if heightdelta_btw_ref < heightdelta_btw_final:
#                print('here')
                final_height = height
                final_user_id = user_id
        else:
            final_height = height
            final_user_id = user_id

    final = session.query(Athelete).filter(Athelete.id==final_user_id).first()
    return final


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
        close_date_user = user_by_date(user_present, querier)
        print('Ближайший к данному пользователю: {} по дате рождения: {}'.format(user_present.first_name + user_present.last_name, close_date_user.name))
        close_height = user_by_height(user_present, querier)
        print('Ближайший к данному пользователю: {} по росту: {}'.format(user_present.first_name + user_present.last_name, close_height.name))
      
    else:
        print('No such user: ', user_present.first_name)


if __name__ == "__main__":
    main()
