#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''Задание 1
Напишите модуль users.py, который регистрирует новых пользователей. Скрипт должен запрашивать следующие данные:
имя
фамилию
пол
адрес электронной почты
дату рождения
рост
Все данные о пользователях сохраните в таблице user нашей базы данных sochi_athletes.sqlite3.'''

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


def request_info():
    '''Requests info from CLI and returns dict()
    имя
    фамилию
    пол
    адрес электронной почты
    дату рождения
    рост'''
    
    print('Please, input user info')
    f_name = input('Input First name: ')
    l_name = input('Input Last name: ')
    gender = input('Please, input the gender (Male|Female): ')
    email = input('Input email: ')
    birthdate = input('Please, input your birthday (Format: YYYY-MM-DD): ')
    height = input('Please, input your growth (Format: 1.6): ')
    if valid_email(email):
        one_user = {'first_name': f_name,
                    'last_name': l_name,
                    'gender': gender,
                    'email': email,
                    'birthdate': birthdate,
                    'height': float(height)
                    }
#        print(one_user)
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

def main():
    '''Main activity of module
    
    Without any error-checking :-( '''
    #Create session object
    querier = connect_db(DB_PATH)
    #request info about user
    a_user = request_info()
    # add new user to DB and commit
    querier.add(User(**a_user))
    querier.commit()
    for i in querier.query(User).filter(User.first_name==a_user['first_name']).all():
        print('User /', i.first_name, '/ has successfully added to DB!')


if __name__ == "__main__":
    main()

