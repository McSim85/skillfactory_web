#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
It reads user list from json and It asks you about users.
Writes to json-file
Перепишем юнит B4.4 еще раз, задавшись следующими целями:
- хранить данные о пользователях в базе данных SQLite;
- разделить регистрационные данные и данные о последней активности пользователей по разным таблицам;
- в режиме поиска выводить данные о количестве пользователей с заданным именем;
- в режиме поиска выводить данные о всех пользователях с заданным именем.
Мы будем хранить данные в базе sqlite3. Для доступа к ней будем пользоваться инструментами библиотеки SQLAlchemy. 
'''

# импортируем модули стандартной библиотеки uuid и datetime
#import os
import uuid
#import time
import datetime

# импортируем библиотеку sqlalchemy и некоторые функции из нее 
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DB_PATH = "sqlite:///users.sqlite3"

# базовый класс моделей таблиц - WHAAATTT???
Base_class = declarative_base()


class User(Base_class):
    """
    Описывает структуру таблицы user для хранения регистрационных данных пользователей
    """
#    print(dir())
    # задаем название таблицы
    __tablename__ = 'user'
    # SET the FIELDS OF TABLE
    # идентификатор пользователя, первичный ключ
    # sa - ALIAS for sqlalchemy
    id = sa.Column(sa.String(36), primary_key=True)
    # имя пользователя
    first_name = sa.Column(sa.Text)
    # фамилия пользователя
    last_name = sa.Column(sa.Text)
    # адрес электронной почты пользователя
    email = sa.Column(sa.Text)


class LastSeenLog(Base_class):
    """
    Описывает структуру таблицу log для хранения времени последней активности пользователя
    """
    # задаем название таблицы
    __tablename__ = 'log'

    # идентификатор пользователя, первичный ключ
    id = sa.Column(sa.String(36), primary_key=True)
    # время последней активности пользователя
    timestamp = sa.Column(sa.DATETIME)
    

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


#class User():
#    '''Read and write info about users'''
#    
#    def __init__(self, db):
#        self.db = db
#        self.users = self.read(self.db)
#    
#    def read(self, filename):
#        '''It reads info about users from filemane
#        and return list() of dict()s about users.
#        filename - str with filename path
#        '''
#        
#        if not os.path.exists(filename) or os.path.getsize(filename) == 0 :
#            return []
#        
#        with open(filename) as db:
#            users = json.load(db)
#        
#        return users
#
#    def save(self, users, filename):
#        '''It writes info about users into filename.
#        users - list() of dict()s with user info
#        filename - str with filename path
#        '''
#        
#        with open(filename, 'w') as db:
#            json.dump(users, db)
#
#    def find(self, user):
#        '''It find user in DB by name '''
#        
#        for a_user in self.users:
#            if a_user['first_name'] == user: return a_user
#            

#

#
#    def add_user(self, user_data):
#        '''Добавляет данные пользователя user_data в список всех пользователей и сохраняет обновленный список '''
#        
#        self.users.append(user_data)
#        self.save(self.users, self.db)
#
#    
#class LastSeenLog():
#    ''' Get and save user time login '''
#    
#    def __init__(self, db):
#        self.db = db
#        self.logs = self.load(self.db)
#    
#    def load(self, j_db):
#        '''Reads info from DB'''
#        
#        if not os.path.exists(j_db) or os.path.getsize(j_db) == 0 :
#            return dict()
#        
#        with open(j_db) as db:
#            logs = json.load(j_db)
#        
#        return logs
#
#    def save(self, data, json_db):
#        '''It saves data to db '''
#        
#        with open(json_db, 'w') as db:
#            json.dump(data, db)
#            
#    def update_timestamp(self, user_id):
#        '''Update info for user_id'''
#        ct = time.time()
#        self.logs[user_id] = ct
#        self.save(self.logs, self.db)
#
#    def find(self, user_id):
#        '''It finds timestamp about user_id'''
#        if self.logs.get(user_id):
#            last_seen_time_stamp = self.logs[user_id]
#            last_seen_date_time = datetime.datetime.fromtimestamp(last_seen_time_stamp)
#            return last_seen_date_time.isoformat()
#
#
#def main():
#    '''Interact with stdin\stdout.
#    '''
#    print('Read all user data')
#    users = User(JSON_USER_FILE)
#    logins = LastSeenLog(LOG_DATA_FILE_PATH)
#    mode = input('Which mode do you prefer? (1 - find user | 2 - add user) ')
#    if mode == '1':
#        who = input('Please, input user\'s name: ')
#        if users.find(who): print('User has founded')
#        else: print('No this user')
#    elif mode == '2':
#        one_user = users.request_info()
#        if one_user: 
#            users.add_user(one_user)
#            print(one_user)
#            print(one_user['id'])
#            logins.update_timestamp(one_user['id'])
#        else: print('Invalid user')
#    else:
#        print('Incorrect mode, please choose 1 or 2')
#        return
#    
#    


if __name__ == "__main__":
    pass

